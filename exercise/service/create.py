import json
import boto3
import logging

dynamodb = boto3.resource('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    """ Function to create a new exercise

    Args:
        event (dict): Contains  request consisting of AWS API gateway request.
        context(dict): Not used.

    Returns:
        statusCode: http status code
        body: item which got created
    
    """
    #table = dynamodb.Table(os.environ['EXERCISE_TABLE'])
    logger.info('got event{}'.format(event))
    table = dynamodb.Table('exercise')
    

    # fetch exercise from the database    
    table.put_item(
       Item = json.loads(event['body'])
    )


    # creating a response
    response = {
        "statusCode": 201,
        "body": json.dumps('Item')
    }

    return response
    
