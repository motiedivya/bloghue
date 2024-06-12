from pydantic import BaseModel

class Notification(BaseModel):
    recipient_email: str
    subject: str
    message: str
