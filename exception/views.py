from django.shortcuts import render_to_response
from models import Sensor, Exemption

def download_all(request, api_key):
    sensor = Sensor.objects.get(api_key=api_key)
    return render_to_response('download.html', {'data': Exemption.objects.all()}, content_type='text/plain')