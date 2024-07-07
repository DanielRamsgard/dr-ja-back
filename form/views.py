from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from . import send_res

# Create your views here.
@csrf_exempt
def form(request):
    if request.method == "POST":
        form = json.loads(request.body)
        send_res(form)