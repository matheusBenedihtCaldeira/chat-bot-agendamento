# Utils imports
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class TwilioService:
    def __init__(self):
        self.__account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.__auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.__from_whatsapp_number = os.getenv("WHATSAPP_NUMBER")
        self.client = Client(self.__account_sid, self.__auth_token)

    def send_message(self, to_number: str, message: str):
        try:
            response = self.client.messages.create(
                body=message,
                from_='whatsapp:+14155238886',
                to=to_number
            )
            return response.sid
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
            raise e
