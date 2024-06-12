from fastapi import FastAPI, Request
from .log import logger, init_logger

app = FastAPI()

init_logger()

@app.post("/log/")
async def log_message(request: Request):
    log_data = await request.json()
    level = log_data.get("level", "info").upper()
    message = log_data.get("message", "")

    if level == "DEBUG":
        logger.debug(message)
    elif level == "INFO":
        logger.info(message)
    elif level == "WARNING":
        logger.warning(message)
    elif level == "ERROR":
        logger.error(message)
    elif level == "CRITICAL":
        logger.critical(message)
    else:
        return {"error": "Invalid log level"}, 400

    return {"message": "Log entry created"}
