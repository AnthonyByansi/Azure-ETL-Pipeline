import logging

import azure.functions as func
from main import main

def main_wrapper(req: func.HttpRequest, outputDocument: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return main(req, outputDocument)
