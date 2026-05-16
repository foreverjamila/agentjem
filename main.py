import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Guard: fail early if API key is missing
if api_key is None:
    raise RuntimeError("API key not found. Make sure your .env file exists and contains the key.")

# Create Gemini client
client = genai.Client(api_key=api_key)

prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

# Send a prompt and print the response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# Guard: verify usage metadata exists
if response.usage_metadata is None:
    raise RuntimeError("No usage metadata in response. The API request may have failed.")



print(f"User prompt: {prompt}")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(f"Response:\n{response.text}")



def main():
    print("Hello from agentjem!")


if __name__ == "__main__":
    main()
