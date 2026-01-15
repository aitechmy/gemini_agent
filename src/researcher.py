from google.genai import types

class ResearchAgent:
    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.persona = (
            "You are a Hybrid Research Intelligence Agent. Your goal is to combine "
            "knowledge from a local PDF with the latest 2026 state-of-the-art information. "
            "Use the Google Search tool to find citations or benchmarks that post-date the PDF."
        )

    def analyze_paper(self, file_obj):
        # We rename the prompt to be hybrid-focused
        prompt = (
            "1. Deeply analyze this PDF's methodology and results.\n"
            "2. Use Google Search to find if there are any newer 2025 or 2026 developments "
            "on this specific topic.\n"
            "3. Synthesize a report highlighting what is in the paper vs what is new in 2026."
        )
        
        response = self.client.models.generate_content(
            model=self.config.MODEL_ID,
            config=types.GenerateContentConfig(
                system_instruction=self.persona,
                # This line enables the 2026 web search capability
                tools=[types.Tool(google_search=types.GoogleSearch())],
                thinking_config=types.ThinkingConfig(
                    include_thoughts=True, 
                    thinking_budget=self.config.THINKING_BUDGET
                ),
                temperature=0.3
            ),
            contents=[file_obj, prompt]
        )
        return response.text