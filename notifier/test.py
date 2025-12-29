from dotenv import load_dotenv
load_dotenv("api.env")  

from notifier.email_notifier import send_whatsapp, send_sms

print(send_whatsapp(" WhatsApp sandbox test succesful!", "+918855881858"))
# print(send_sms(" SMS test succesful!", "+918855881858"))
