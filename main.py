from flask import Flask, request, jsonify;
import os
import config
import openai


#############
#  API KEY  #
#############

# Attempt to get the API key from the environment
API_KEY = os.getenv('API_KEY')

# If not env, try to get it locally.  If that fails, it throws an error and halts the code.
if not API_KEY:
    try:
        from chat_gpt_api_key import API_KEY
    except ImportError:
        raise RuntimeError('API_KEY not found.  Either set your environment variable or create a file called chat_gpt_api_key.py and set your API_KEY there.')

openai.api_key = API_KEY

app = Flask(__name__)

messages = [{'role': 'system', 'content': config.system_role}]

#############
#  Routes  #
#############

@app.route('/')
def home():
    messages.append({'role': 'user', 'content': 'What do you think about the weather?'})
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = messages
    )
    reply = response['choices'][0]['message']['content']
    messages.append({'role':'assistant', 'conent': reply})
    return reply




############
#  Return  #
############

@app.route('/get-next-line')
def getNextLine():
    return ''

##################
#  Server Start  #
##################

if __name__ == '__main__':
    app.run(debug=True)