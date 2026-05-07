from django.urls import path
from .views import predict_ner, home

urlpatterns = [
    path('', home),
    path('predict/', predict_ner),
]