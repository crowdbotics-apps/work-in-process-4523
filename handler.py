import json


def hello(event, context):
    body = {
        "message": "Congratulations! You just released your first serverless function - work_in_process_4523 - with Crowdbotics! Reward yourself! Grab a cup of coffee!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
