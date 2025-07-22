# OpenAI imports
from openai import OpenAI
# Config imports
from config.settings import Settings

class OpenAIService:
    def __init__(self):
        self.__client = OpenAI(api_key=Settings().OPENAI_API_KEY)

    def generate_response(self, messages: list[dict]) -> str:
        try:
            response = self.__client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"[Erro OpenAI]: {str(e)}")
            raise e
