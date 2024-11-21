from django.urls import path
from api.views import ShortUrl
urlpatterns = [
    path("short-url/",ShortUrl.as_view()),
]