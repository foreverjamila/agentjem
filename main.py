import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
import sys

# Load environment variables from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Guard: fail early if API key is missing
if api_key is None:
    raise RuntimeError("API key not found. Make sure your .env file exists and contains the key.")

# Create Gemini client
client = genai.Client(api_key=api_key)


# Set up argument parser
parser = argparse.ArgumentParser(description="AgentJem — AI-powered CLI")
parser.add_argument("user_prompt", type=str, help="The prompt to send to Gemini")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


# Structure the conversation as a list of messages
messages = [
    types.Content(
        role="user", 
        parts=[types.Part(text=args.user_prompt)]
    )
]

# Send a prompt and print the response
# Agent loop — max 20 iterations
for _ in range(20):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt, 
            temperature=0
        )
    )

    # Guard: verify usage metadata exists
    if response.usage_metadata is None:
        raise RuntimeError("No usage metadata in response. The API request may have failed.")


    # Only print metadata if --verbose flag is set
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    # Add Gemini's response to conversation history
    if response.candidates:
        for candidates in response.candidates:
            messages.append(candidates.content)

    # If no function calls — Gemini is done, print final answer
    if not response.function_calls:
        print(f"Final response:\n{response.text}")
        sys.exit(0)


    # Execute each function call and collect results 
    function_responses = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose=args.verbose)
        # Validate the result
        if not function_call_result.parts:
            raise Exception("No parts in function call result")
        if function_call_result.parts[0].function_response is None:
            raise Exception("No function response in result")
        if function_call_result.parts[0].function_response.response is None:
            raise Exception("No response data in function response")
        # Print result if verbose
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result.parts[0])
            
    # Add function results to conversation history
    messages.append(types.Content(role="user", parts=function_responses))

# If we reach here, max iterations hit
print("Error: Maximum iterations reached without a final response.")
sys.exit(1)




def main():
    pass


if __name__ == "__main__":
    main()
