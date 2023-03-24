from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework import generics

def fpl_page(request):
    return render(request,"fpl_api.html", {})

@api_view(['GET'])
def fpl_api(request):
    try:
        response = requests.get("https://fixturedownload.com/feed/json/epl-2022")
        return JsonResponse(response.json(), safe=False)
    except:
        return render(request, "fpl_api.html",{})

class FPLAPI(generics.ListAPIView):
    queryset = requests.get("https://fixturedownload.com/feed/json/epl-2022")


# Create your views here.
