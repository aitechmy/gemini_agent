from google.genai import types

class ResearchAgent:
    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.persona = (
            "You are a Senior Research Analyst. Your task is to extract "
            "technical parameters and methodologies from scientific papers. "
            "Be descriptive, use a formal tone, and ignore fluff."
        )

    def analyze_paper(self, file_obj):
        prompt = "Perform a deep technical mining of this paper. Focus on the Methodology and Results."
        
        # In 2026, Gemini 2.5 Flash uses 'thinking_config' for reasoning
        response = self.client.models.generate_content(
            model=self.config.MODEL_ID,
            config=types.GenerateContentConfig(
                system_instruction=self.persona,
                # Thinking budget allows the agent to 'plan' the extraction
                thinking_config=types.ThinkingConfig(
                    include_thoughts=True, 
                    thinking_budget=self.config.THINKING_BUDGET
                ),
                temperature=0.2
            ),
            contents=[file_obj, prompt]
        )
        return response.text