#ciekawe czy coś się stanie
from django.shortcuts import render

def home(request):
    import json
    import requests

    try:
        api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Warsaw&APPID=6eccd0c1abcd929aca44f63dd104bfaf")
        api = json.loads(api_req.content)
        #temp=api['main']['Temp']
        #temp= int(temp)
        #temp=temp-273
    except exception as e:
        e = "error"

    return render(request,"home.html",{'api':api})
def O_mnie(request):
    return render(request,"O_mnie.html",{})