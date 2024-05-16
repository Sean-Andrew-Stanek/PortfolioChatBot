"""
This module containes an Azure Function which processes HTTP requests.
The function will respond to a list of old messages and a new message
and return a new response from the OpenAI API based on parameters found
within the config.py file.
"""


import os
import json
from openai import OpenAI
import azure.functions as func
import config



app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="get_message")
def get_message(req: func.HttpRequest) -> func.HttpResponse:
    """
    This function handles the request.
    It extracts messages and new_messages to make a new API request.
    It returns the new line of messages including the API response.

    Args: 
        req (funct.HttpRequest):
            JSON object:
                messages: Previous Messags
                new_message: New request to API
        
    Returns:
        func.HttpResponse:
            JSON object:
                messages: new list of messages

    """

    #############
    #  API KEY  #
    #############

    api_key = os.getenv('API_KEY')

    if not api_key:
        return func.HttpResponse(
            json.dumps({
                'status': 'error',
                'message': 'API Key not found.'
            }),
            status_code=400,
            mimetype='application/json'
        )



    #####################
    #  Initializations  #
    #####################

    client = OpenAI(api_key=api_key)


    ##############
    #  Function  #
    ##############

    try:
        data = req.get_json()

        ###  Verifies request format
        if data['messages'] is None or data['new_message'] is None:
            return func.HttpResponse(
                json.dumps({
                    'status': 'error',
                    'message': 'Error with request form'
                }),
                status_code=400,
                mimetype='application/json'
            )

        ###  appends the new_message to the old messages
        ###  TODO: Handle no new message or parse it for "hidden request"
        if data['messages'] == '':
            messages = config.MESSAGES
        else:
            messages = data['messages']
        messages.append(data['new_message'])

        #Fetch from the API
        response = client.chat.completions.create(
            model= config.MODEL,
            messages=messages,
            max_tokens= config.MAX_TOKENS
        )

        # Adds the new response to the messages so it can be resent in the next request
        ai_reply = response.choices[-1].message.content
        messages.append({'role': 'system', 'content': ai_reply})

        return func.HttpResponse(
            json.dumps(
                {
                    'reply': ai_reply,
                    'messages': messages
                }
            ),
            status_code=400,
            mimetype='application/json'
        )

    except json.JSONDecodeError:
        return func.HttpResponse(
            json.dumps(
                {
                    'status': 'error',
                    'message': 'Invalid request.'
                },
                status_code=400,
                mimetype='application/json'
            )
        )
