from fastapi import FastAPI, HTTPException
from .producer import publish_message

app = FastAPI()

@app.post("/queue/")
def send_message_to_queue(message: str):
    try:
        publish_message(message)
        return {"message": "Message sent to queue"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
