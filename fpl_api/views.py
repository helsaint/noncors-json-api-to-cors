from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework import generics

def fpl_page(request):
    return render(request,"fpl_api.html", {})

@api_view(['GET'])
def fpl_api(request):
    response = requests.get("https://fantasy.premierleague.com/api/fixtures/")
    return JsonResponse(response.json(), safe=False)

class FPLAPI(generics.ListAPIView):
    queryset = requests.get("https://fantasy.premierleague.com/api/fixtures/")


# Create your views here.
