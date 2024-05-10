from flask import Flask, request, jsonify, render_template;
import os
import config
from openai import OpenAI


#############
#  API KEY  #
#############

API_KEY = os.getenv('API_KEY')

# If not env, try to get it locally.  If that fails, it throws an error and halts the code.
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

app = Flask(__name__)

messages = config.messages

#############
#  Routes  #
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

    #Add user input to messages
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
    return jsonify({'reply': ai_reply}) 

##################
#  Server Start  #
##################

if __name__ == '__main__':
    app.run(debug=True)