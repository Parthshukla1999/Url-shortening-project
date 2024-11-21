from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from api.models import UrlLinks
from api.serializer import LinkSerialisers
import requests
from rest_framework.response import Response
# Create your views here.


class ShortUrl(APIView):
    def post(self, request):
        url = request.data["url"]
        api_url = f"https://tinyurl.com/api-create.php?url={url}"
        response = requests.get(api_url)
        UrlLinks.objects.create(
          full_url=url,
          short_url=response.text
        )
        return Response({"data":response,"message":"short url created.","status":status.HTTP_200_OK})
    
class getOldUrlBy_id(APIView):
    def get(self, request, id):
        try:
            link = UrlLinks.objects.get(id = id)
        except UrlLinks.DoesNotExist:
            return Response({"data":None,"message":"not able to get","status":status.HTTP_400_BAD_REQUEST})
        serializer = LinkSerialisers(link)
        return Response({"data":serializer.data,"message":"Fetch","status":status.HTTP_200_OK})
    
class deleteUrl(APIView):
    def delete(self, request,id):
        try:
            link = UrlLinks.objects.get(id = id)
        except UrlLinks.DoesNotExist:
            return Response({"data":None,"message":"not able to get","status":status.HTTP_400_BAD_REQUEST})
        link.delete()
        return Response({"data":None,"message":"Deleted","status":status.HTTP_200_OK})
    
class UpdateUrl(APIView):
    def put(self, request, id):
        try:
            link = UrlLinks.objects.get(id = id)
        except UrlLinks.DoesNotExist:
            return Response({"data":None,"message":"not able to get","status":status.HTTP_400_BAD_REQUEST})
        serializer = LinkSerialisers(link,data=request.data,partial =True)
        return Response({"data":serializer.data,"message":"Fetch","status":status.HTTP_200_OK})



