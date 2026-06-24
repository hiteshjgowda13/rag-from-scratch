import os
from dotenv import load_dotenv
from google import genai

class LLM:
    # when initialised loads the gemini api key
    def __init__(self):
        load_dotenv()

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )
    # takes the prompt and gives output prompt is context
    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text