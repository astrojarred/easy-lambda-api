import json
import logging

from api import paths
from api.route import routes

# set up logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):

    logger.debug("NEW CALL:")
    logger.debug(f"Got event: {event}")
    logger.debug(f"Got context: {context}")

    error = False


    params = event.get("queryStringParameters")
    path = event.get("rawPath")

    logger.debug(f"Parameters: {params}")
    logger.debug(f"Path: {path}")

    if path not in routes.keys():
        logger.error(f"Route {path} not found. Returning 404.")
        error_message =  f"Route {path} not found."
        error_code = 404
        error = True
    
    if not error:
        try:
            result = routes[path](**params)

        except Exception as e:
            logger.error(f"Issue running the function {path} with params {params}.")
            logger.error(f"Details: {e}")
            error_message = e
            error_code = 400
            error = True

    if error:
        logger.debug(f"Unable to run {path} with result: {error_message}")
        return {
            'statusCode': error_code,
            'body': {"ok": False, "result": str(error_message)}
        }


    logger.debug(f"Successfully ran {path} with result: {result}")
    return {
            'statusCode': 200,
            'body': {"ok": True, "result": result}
        }
