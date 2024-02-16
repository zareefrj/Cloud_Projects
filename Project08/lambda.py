# import the JSON utility package
import json

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

# extract the name from the Lambda service's event object
    name = event['name']
    # return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': json.dumps('Happy Valentine''s Day to my favourite girl: ' + name)
    }