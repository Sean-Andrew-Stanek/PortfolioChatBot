from flask import Flask, request, jsonify, render_template, session;
import os
import config
from openai import OpenAI


#############
#  API KEY  #
#############

API_KEY = os.getenv('API_KEY')

# Checks for the API key in the env and locally.  Otherwise stops.
if not API_KEY:
    try:
        from chat_gpt_api_key import API_KEY
    except ImportError:
        raise RuntimeError('API_KEY not found.  Either set your environment variable or create a file called chat_gpt_api_key.py and set your API_KEY there.')

#####################
#  Initializations  #
#####################

client = OpenAI(
    api_key=API_KEY
)

app = Flask(__name__, static_folder='static')

#############
#  Routes   #
#############

### Home Route
@app.route('/')
def home():
    return render_template('chat.html')


### Chat with Bot
@app.route('/chat', methods=['POST'])
def chat():

    #Retrieve the data
    data = request.json
    user_message = data['message']

    # Create message field 
    # Looks locally, then from the request and then to the base parameters
    messages = session.get('messages')
    if(messages is None):
        messages = data['messages']
        if(messages is None):
            ############################################
            ### EDIT YOUR BASE MESSAGE VARIABLE HERE ###
            ############################################
            messages= config.sean_messasges         
    messages.append({'role': 'user', 'content': user_message})

    #Fetch from the API
    response = client.chat.completions.create( 
        model= config.model,
        messages=messages, 
        max_tokens= config.max_tokens
    )

    # Log new response and send it to the front end.
    ai_reply = response.choices[-1].message.content 
    messages.append({'role': 'system', 'content': ai_reply}) 
    
    #return latest message and all messages
    return jsonify({'reply': ai_reply, 'messages': messages}) 

##################
#  Server Start  #
##################

if __name__ == '__main__':
    app.run(debug=True)