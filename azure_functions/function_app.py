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
        if(data['messages'] is None or data['new_message'] is None):
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

        if(messages)



    except json.JSONDecodeError as e:
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
