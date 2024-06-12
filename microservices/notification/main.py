from fastapi import FastAPI, Depends, HTTPException, status
from . import schemas, services, auth

app = FastAPI()

@app.post("/notifications/", response_model=schemas.Notification)
def create_notification(notification: schemas.Notification, current_user: str = Depends(auth.get_current_user)):
    services.send_email(notification)
    return notification
