import os
from dotenv import load_dotenv
from google import genai

# 1. This looks for the .env file and loads the variables into your system memory
load_dotenv()

# 2. Retrieve the key safely using os.getenv
api_key = os.getenv("GEMINI_API_KEY")

# 3. Initialize the client using the variable
client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="System check: Is the .env working?"
    )
    print(f"Model Response: {response.text}")
    print("✅ Success: API key loaded from .env file.")
except Exception as e:
    print(f"❌ Error: {e}")