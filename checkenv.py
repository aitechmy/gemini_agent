import os
from pathlib import Path
from dotenv import load_dotenv

# Get the absolute path of the directory where THIS script is located
#base_dir = Path(__file__).resolve().parent
#env_path = base_dir / ".env"

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# Force load with an absolute path and verbose=True to see errors
#load_dotenv(dotenv_path=env_path, verbose=True)

key = os.getenv("GEMINI_API_KEY")
print(os.environ.get("GEMINI_API_KEY", "<not in environ>"))


if key:
    print(f"✅ Key successfully loaded: {key[:4]}...{key[-4:]}")
else:
    print(f"❌ Still failed. Checked path: {env_path}")