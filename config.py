import os
from pathlib import Path
from dotenv import load_dotenv

# Inside class Config:
from google.genai import types



class Config:
    def __init__(self):
        # Path Management
        self.BASE_DIR = Path(__file__).resolve().parent
        self.LIT_DIR = self.BASE_DIR / "literature"
        self.OUTPUT_DIR = self.BASE_DIR / "outputs"
        
        # Create directories if they don't exist
        self.LIT_DIR.mkdir(exist_ok=True)
        self.OUTPUT_DIR.mkdir(exist_ok=True)

        # API & Model Settings
        load_dotenv(dotenv_path=self.BASE_DIR / ".env")
        self.API_KEY = os.getenv("GEMINI_API_KEY")
        
        # Use Gemini 2.5 Flash for its advanced reasoning and PDF support
        self.MODEL_ID = "gemini-2.5-flash" 
        self.THINKING_BUDGET = 16000 # Reasoning tokens (0 to 24,576)
        self.RPM_DELAY = 7 # 7 seconds to safely stay under 10 RPM (Free Tier)
        
        self.TOOLS = [
            types.Tool(
                google_search=types.GoogleSearch() # Enables live web access
            )
        ]     

        if not self.API_KEY:
            raise ValueError("CRITICAL: GEMINI_API_KEY not found in .env")