from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from src.utils.settings import settings
from typing import List
class EmailSchema(BaseModel):
    email:list[EmailStr]
conf = ConnectionConfig(
    # MAIL_USERNAME = "alarah188@gmail.com",
    # MAIL_PASSWORD = "xuvo rmbp hmzb uppq",
    # MAIL_FROM = "alarah188@gmail.com",
    # MAIL_PORT = 587,
    # MAIL_SERVER = "smtp.gmail.com",
    # MAIL_FROM_NAME = "kainats wishes",
    # MAIL_STARTTLS = True,
    # MAIL_SSL_TLS = False,
    # USE_CREDENTIALS = True,
    # VALIDATE_CERTS = True
    
    MAIL_USERNAME = settings.MAIL_USERNAME,
    MAIL_PASSWORD = settings.MAIL_PASSWORD,
    MAIL_FROM = settings.MAIL_FROM,
    MAIL_PORT = settings.MAIL_PORT,
    MAIL_SERVER = settings.MAIL_SERVER,
    MAIL_FROM_NAME = "kainats wishes",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)
    
async def send_email(emails:List[str]):
    html = """<p>Hi, Thanks for Registration. Our Team will connect you soon !</p> """

    message = MessageSchema(
        subject="Registration Confirmation",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    #return {"message": "email has been sent"}
    print("email has sent")