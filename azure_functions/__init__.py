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


app = func.FunctionApp()

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    This function handles the request.
    It extracts messages and new_messages to make a new API request.
    It returns the new line of messages including the API response.

    Args: 
        req (funct.HttpRequest):
            JSON object:
                messages: Previous messages formatted the same way as the response
                new_message: String of the newest user message
        
    Returns:
        func.HttpResponse:
            JSON object:
                reply: String of the newest openAI response content
                messages: Formatted version of non-default openAI messages for future use

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


    ########################
    #  Request Processing  #
    ########################

    def request_error(trace_code):
        return func.HttpResponse(
            json.dumps(
                {
                    'status': 'error',
                    'message': 'Invalid request.',
                    'trace code': trace_code
                }),
            status_code=400,
            mimetype='application/json'
        )


    try:
        data = req.get_json()

    ###  Verifies JSON type
    except json.JSONDecodeError:
        return request_error(1)

    ###  Verifies request keys
    if 'messages' not in data or 'new_message' not in data:
        return request_error(2)

    ###  Verifies request new_message is a string
    if not isinstance(data['new_message'], str):
        return request_error(3)

    ###  Verifies messages format
    if not isinstance(data['messages'], list):
        return request_error(4)

    for i, item in enumerate(data['messages']):
        if not isinstance(item, dict):
            return request_error(f'message {i}')
        if 'role' not in item or 'content' not in item:
            return request_error(f'message {i}')

    ### TODO: Limit the size of user_messages
    ### TODO: Remove messages which exceed the limit
    character_count = 0
    reversed_messages = {'new_message': data['new_message'], 'messages': []}
    for message in reversed(data['messages']):
        content_length = len(message['content'])
        if character_count + content_length > 500:
            break
        character_count += content_length
        reversed_messages['messages'].append(message)


    modified_data=reversed_messages.copy()
    modified_data['messages'].append({'role': 'user', 'content': data['new_message']})
    
    ###  Combine all messages
    messages = config.MESSAGES.copy()
    messages.extend(modified_data['messages'])

    


    #Fetch from the API
    response = client.chat.completions.create(
        model= config.MODEL,
        messages=messages,
        max_tokens= config.MAX_TOKENS
    )

    ### ai_reply = easy to read string response
    ### user_messages = stores entire conversation on front end in returnable format
    ai_reply = response.choices[-1].message.content
    messages.append({'role': 'system', 'content': ai_reply})

    return func.HttpResponse(
        json.dumps(
            {
                'reply': '', #ai_reply,
                'messages': messages #user_messages
            }
        ),
        status_code=400,
        mimetype='application/json'
    )
