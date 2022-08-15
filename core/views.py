from django.http import HttpResponse
from rest_framework.decorators import api_view
import json

from src.main_handler import MainHandler

HEADERS = {
    'Access-Control-Allow-Origin': '*',
};

@api_view(['GET'])
def home(request):
    return HttpResponse("Python AI server works on nginx!", headers=HEADERS)

@api_view(['GET'])
def search(request):
    ids = MainHandler.search(request.query_params)

    return HttpResponse(json.dumps(ids), headers=HEADERS)
