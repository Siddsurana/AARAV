from twilio.rest import Client

def make_call():
    account_sid = 'AC9e3f1ed74a768a16e9a27517603ffa06'
    auth_token = 'c642892191df308998de00b66fdc059f'
    # Twilio Phone Number
    twilio_phone_number = '+13344234208'
    sahil_phone_number = '+919607118530'  # Update with Sahil's actual phone number

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Make a phone call
    call = client.calls.create(
        to=sahil_phone_number,
        from_=twilio_phone_number,
        url='http://demo.twilio.com/docs/voice.xml'  # TwiML URL, you can replace with your own
    )
    print("Calling Sahil...")
