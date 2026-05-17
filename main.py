import os
from dotenv import load_dotenv
from google import genai
import argparse

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
args = parser.parse_args()

# Send a prompt and print the response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=args.user_prompt
)

# Guard: verify usage metadata exists
if response.usage_metadata is None:
    raise RuntimeError("No usage metadata in response. The API request may have failed.")



print(f"User prompt: {args.user_prompt}")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(f"Response:\n{response.text}")



def main():
    print("Hello from agentjem!")


if __name__ == "__main__":
    main()
