# FastAPI imports
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
# Routes imports
from routes.whatsapp_webhook.routes import api_whatsapp_webhook

# Instancia APP
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


api = APIRouter(prefix='/api')
# Rotas
api.include_router(api_whatsapp_webhook)

app.include_router(api)
