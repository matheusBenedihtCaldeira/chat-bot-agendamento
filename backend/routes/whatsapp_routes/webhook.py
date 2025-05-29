# FastAPI imports
from fastapi import APIRouter, status, HTTPException, Form, Depends
from fastapi.responses import PlainTextResponse
# Controllers import
from controllers.whatsapp.response import WhatsappResponseController
# Models imports
from models.payloads.whatsapp_webhook_models import WhatsAppWebhookModel

api_whatsapp_webhook = APIRouter(prefix='/whatsapp-webhook')


@api_whatsapp_webhook.post(
    path='',
    tags=['whatsapp-webhook'],
    status_code=status.HTTP_200_OK
)
async def whatsapp_webhook(data: WhatsAppWebhookModel = Depends()):
    res = WhatsappResponseController.response(message=data)
    return
    #return PlainTextResponse("Mensagem recebida com sucesso!", status_code=200)