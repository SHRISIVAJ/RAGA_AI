import openai

class LanguageAgent:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def generate_narrative(self, data):
        prompt = f"Generate a market brief from the following data: {data}"
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose an appropriate model from OpenAI
            prompt=prompt,
            max_tokens=200
        )
        return response.choices[0].text.strip()
