import spotify

from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import urllib
from twilio import twiml
#Account SID and AUth Token from twilio

client = Client('ACa47d92b43a2077a8f96070db71c126a0','4be7fd81452e67a0077f3449c65ae100')

app = Flask(__name__)


# A route to respond to SMS messages and kick off a phone call.
@app.route('/sms', methods=['POST'])
def inbound_sms():
    print("Inside sms")
    response = MessagingResponse()
    response.message('Thanks for texting! Searching for the requested song'
                     'Your song is just a call away!Wait for it!! :)')

    # Grab the song title from the body of the text message.
    song_title = urllib.parse.quote(request.form['Body'])

    # Grab the relevant phone numbers.
    from_number = request.form['From']
    to_number = request.form['To']
   # response.message(song_title)
    # Create a phone call that uses our other route to play a song from Spotify.
    client.api.account.calls.create(to=from_number, from_=to_number,url='http://5e6f1eb6.ngrok.io/call?track={}'.format(song_title))

    return str(response)


# A route to handle the logic for phone calls.
@app.route('/call', methods=['POST'])
def outbound_call():
    print("inside call")
    song_title = request.args.get('track')
    track_url = spotify.get_track_url(song_title)
    #response.message(track_url)
    response = VoiceResponse()
    #response = twiml.Response()
    response.play(track_url)
    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


