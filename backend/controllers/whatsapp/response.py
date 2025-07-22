# Services imports
from services.openai.service import OpenAIService
from services.twilio.service import TwilioService
# Models imports
from models.whatsapp_webhook_models.payloads import WhatsAppWebhookPayload
# Repository imports
from repositories.user_repository import UserRepository
from repositories.conversation_repository import ConversationRepository
# SQLAlchemy imporst
from sqlalchemy.orm import Session


class WhatsappResponseController:

    @staticmethod
    def response(message: WhatsAppWebhookPayload, db: Session) -> str:
        gpt_service = OpenAIService()
        twilio_service = TwilioService()
        user_repository = UserRepository(db=db)
        conversation_repository = ConversationRepository(db=db)

        user = user_repository.get_user_by_number(number=message.From)
        if not user:
            user = user_repository.add_user(
                profile_name=message.ProfileName,
                number=message.From
            )

        conversation_repository.add_message(
            user_id=user.id,
            message=message.Body,
            role="user"
        )

        history = conversation_repository.get_user_conversation_history(user_id=user.id)

        messages = [
            {"role": conv.role, "content": conv.message}
            for conv in history
        ]

        messages.insert(0, {
            "role": "system",
            "content": (
                "Você é um atendente virtual de um salão de cabeleireiro feminino. "
                "Seu papel é ajudar os clientes a agendar horários, informar serviços disponíveis, "
                "esclarecer dúvidas sobre preços, horários de funcionamento e procedimentos. "
                "Seja educado, prestativo e use uma linguagem amigável e profissional."
            )
        })

        response = gpt_service.generate_response(messages=messages)
        sid = twilio_service.send_message(to_number=message.From, message=response)
        return sid
