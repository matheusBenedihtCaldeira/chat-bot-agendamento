from fastapi import Form

class WhatsAppWebhookPayload:
    def __init__(
        self,
        From: str = Form(...),
        Body: str = Form(...),
        ProfileName: str = Form(...)
    ):
        self.From = From
        self.Body = Body
        self.ProfileName = ProfileName
