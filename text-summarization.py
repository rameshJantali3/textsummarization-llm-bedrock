import json
import boto3
import logging

bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # logger.info(f"Received event: {json.dumps(event)}")
    # # Check if the event is already a dictionary or needs parsing
    # if isinstance(event.get('body'), str):
    #     event = json.loads(event['body'])
    
    print(event)
    user_prompt = event['prompt']
    
    if not user_prompt:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing "prompt" in request payload'})
        }
    
    body = {
        "prompt": user_prompt, "max_gen_len": 512, "temperature": 0.2,"top_p": 0.9
        }
    
    kwargs = {
        "modelId": "meta.llama3-8b-instruct-v1:0",
        "contentType": "application/json",
        "accept": "application/json",
        'body': json.dumps(body)
    }
    
    response = bedrock_runtime.invoke_model(**kwargs)
    resp_json = json.loads(response.get('body').read())
    
    return {
        'statusCode': 200,
        'body': json.dumps(resp_json)
    }
