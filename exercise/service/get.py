import json
import boto3
import logging

dynamodb = boto3.resource('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    """ Function to get a exercise using its type

    Args:
        event (dict): Contains  request consisting of AWS API gateway request.
        context(dict): Not used.

    Returns:
        statusCode: http status code
        body: all the items for a particular type in dynamodb table as json
    
    """
    #table = dynamodb.Table(os.environ['EXERCISE_TABLE'])
    logger.info('got event{}'.format(event))
    table = dynamodb.Table('exercise')
    

    # fetch exercise from the database    
    result = table.get_item(
        Key={
            'type': event['pathParameters']['name']
        }
    )


    # creating a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'])
    }

    return response
    
