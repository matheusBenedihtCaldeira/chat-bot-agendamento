# FastAPI imports
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
# Controllers import
from controllers.whatsapp.response import WhatsappResponseController
# Models imports
from models.whatsapp_webhook_models.payloads import WhatsAppWebhookPayload
# Core imports
from core.database import get_session
from sqlalchemy.orm import Session
api_whatsapp_webhook = APIRouter(prefix='/whatsapp-webhook')

@api_whatsapp_webhook.post(
    path='',
    tags=['whatsapp-webhook'],
    status_code=status.HTTP_200_OK
)
async def whatsapp_webhook(data: WhatsAppWebhookPayload = Depends(), db: Session = Depends(get_session)):
    try:
        res = WhatsappResponseController.response(message=data, db=db)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "msg": "Resposta enviada com sucesso!",
                "sid": res
            }
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
