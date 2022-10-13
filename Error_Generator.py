""This code generate the error and store it in cloud watch log""
import logging

logger=logging.getLogger(__name__)

def lambda_handler(event, context):
    logger.setLevel(logging.DEBUG)
    logger.info(" Generating info sample")
    logger.error("Pushpa Generating error sample")
    
   
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
