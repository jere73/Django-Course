"""PlatziGram views."""
# Django
from django.http import HttpResponse
# Utilities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hi, Current server time is {now}'.format(now=str(now)))

def sorted(request):
   
    numbers = request.GET['numbers']
    lista = [int(x) for x in numbers.split(",")]
    lista.sort()

    data = {
        'status': 'ok',
        'numbers': lista,
        'message': 'Numbers were sorted successfully!'
    }

    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here.'.format(name)
    else:
        message = 'Hello {}, welcome to Platzigram.'.format(name)

    return HttpResponse(str(message))
