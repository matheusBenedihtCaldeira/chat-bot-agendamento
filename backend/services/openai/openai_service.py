import os
from dotenv import load_dotenv
from openai import OpenAI
from models.payloads.whatsapp_webhook_models import WhatsAppWebhookModel

load_dotenv()

class OpenAIService:
    def __init__(self):
        self.__client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, message: WhatsAppWebhookModel) -> str:
        prompt = f"""
        Responda de forma amigável e natural a esta mensagem:
        {message.ProfileName}: {message.Body}
        Você:
        """
        try:
            response = self.__client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"[Erro OpenAI]: {str(e)}")
            raise e
