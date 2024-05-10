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

client = OpenAI(
    api_key=API_KEY
)

app = Flask(__name__)


messages = [
    {'role': 'system', 'content': config.system_role},
    {'role': 'assistant', 'content': config.assistant},
    # {'role': 'system', 'content': config.data_dev},
    # {'role': 'user', 'content': config.expected_response}
]

#############
#  Routes  #
#############
@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']


    messages.append({'role': 'user', 'content': user_message}) #user message is added onto messages dictionary

    response = client.chat.completions.create( #creating the AI message
        model='gpt-3.5-turbo', #ai model used
        messages=messages, #this allows ai to use ALL the messages sent so far
        max_tokens=200
    )
    ai_reply = response.choices[-1].message.content #defining the latest ai message
    messages.append({'role': 'system', 'content': ai_reply}) #ai message is added onto messages

    return jsonify({'reply': ai_reply}) #printing latest ai message

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