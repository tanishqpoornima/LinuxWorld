from twilio.rest import Client

def send_whatsapp_message(account_sid, auth_token, twilio_phone_number, receiver_whatsapp_number, message):
    try:
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=message,
            from_='whatsapp:' + twilio_phone_number,
            to='whatsapp:' + receiver_whatsapp_number
        )
        print("WhatsApp message sent successfully!")
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")

account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"
twilio_phone_number = "your_twilio_phone_number"  # Should be in the format: "+1234567890"
receiver_whatsapp_number = "whatsapp_recipient_number"  # Should be in the format: "+1234567890"
message = "This is a test WhatsApp message sent from Python using Twilio."

send_whatsapp_message(account_sid, auth_token, twilio_phone_number, receiver_whatsapp_number, message)
