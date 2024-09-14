import logging
from time import time

logging.basicConfig(filename='api.log', level=logging.INFO)

def log_request(user_id, endpoint, inference_time):
    logging.info(f"User: {user_id}, Endpoint: {endpoint}, Time: {inference_time}s")
