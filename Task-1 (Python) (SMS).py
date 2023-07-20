from twilio.rest import Client

def send_sms(account_sid, auth_token, twilio_phone_number, receiver_phone_number, message):
    try:
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=receiver_phone_number
        )
        print("SMS sent successfully!")
    except Exception as e:
        print(f"Error sending SMS: {e}")

account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"
twilio_phone_number = "your_twilio_phone_number"  # Should be in the format: "+1234567890"
receiver_phone_number = "recipient_phone_number"  # Should be in the format: "+1234567890"
message = "This is a test SMS sent from Python using Twilio."

send_sms(account_sid, auth_token, twilio_phone_number, receiver_phone_number, message)
