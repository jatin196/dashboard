from django.shortcuts import render
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say

account = "AC28f187dda98d32485426e56a25b44796"
token = "45da807c452e42d18050cdb445b12b76"
client = Client(account, token)
# response = VoiceResponse()
# response.say('Hello World')
from_whatsapp_number='whatsapp:+19294292974'
to_whatsapp_number='whatsapp:+917011259363'

client.messages.create(from_=from_whatsapp_number ,to=to_whatsapp_number, body="join whose-screen")
# # print(message.sid)
# response = VoiceResponse()
# response.say('Chapeau!', voice='woman', language='fr-FR')
#
#
# call = client.calls.create(to="+917011259363",
#                            from_="+19294292974",
#                            response=response,
#                            # url="https://www.youtube.com/watch?v=X-orLZrVaqw"
#                            )
#
#
#
#
# print(response)

#
# from twilio.twiml.voice_response import Dial, VoiceResponse, Say
#
# response = VoiceResponse()
# response.dial('415-123-4567')
# response.say('Goodbye')
#
# print(response)


