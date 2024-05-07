from flask import Flask, request, jsonify;
import os

# Attempt to get the API key from the environment
API_KEY = os.getenv('API_KEY')

# If not env, try to get it locally.  If that fails, it throws an error and halts the code.
if not API_KEY:
    try:
        from chat_gpt_api_key import API_KEY
    except ImportError:
        raise RuntimeError('API_KEY not found.  Either set your environment variable or create a file called chat_gpt_api_key.py and set your API_KEY there.')


app = Flask(__name__)

@app.route('/')
def home():
    return ''




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