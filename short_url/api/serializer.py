from rest_framework import serializers
from api.models import UrlLinks

class LinkSerialisers(serializers.ModelSerializer):
    class Meta:
        model = UrlLinks
        fields = ["id","full_url","short_url","created_at"]


        