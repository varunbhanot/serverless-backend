import json
import boto3

dynamodb = boto3.resource('dynamodb')


def handler(event, context):
    """ Function to list all the exercises on the screen

    Args:
        event (dict): Not used.
        context(dict): Not used.

    Returns:
        statusCode: http status code
        body: all the items in dynamodb table as json
    
    """
    #table = dynamodb.Table(os.environ['EXERCISE_TABLE'])
    table = dynamodb.Table('exercise')
    

    # fetch all exercises from the database
    result = table.scan()

    # creating a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }

    return response
    
