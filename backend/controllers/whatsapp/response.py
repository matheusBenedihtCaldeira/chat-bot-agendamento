# Services imports
from services.openai.openai_service import OpenAIService
from services.twilio.twilio_service import TwilioService
# Models
from models.payloads.whatsapp_webhook_models import WhatsAppWebhookModel

class WhatsappResponseController:

    @staticmethod
    def response(message: WhatsAppWebhookModel) -> str:
        gpt_service = OpenAIService()
        twilio_service = TwilioService()

        response = gpt_service.generate_response(message=message)
        sid = twilio_service.send_message(to_number=message.From, message=response)
        return