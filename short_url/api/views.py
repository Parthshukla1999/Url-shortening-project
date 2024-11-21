from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from api.models import UrlLinks
from api.serializer import LinkSerialisers
import requests
# Create your views here.


class ShortUrl(APIView):
    def post(self, request):
        url = request.data["url"]
        api_url = f"https://tinyurl.com/api-create.php?url={url}"
        response = requests.get(api_url)
        UrlLinks.objects.create(
          full_url=url,
          short_url=response
        )
        return {"data":response,"message":"short url created.","status":status.HTTP_200_OK}

