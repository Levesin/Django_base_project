from django.urls import path
from . import views

app_name = 'basic'

urlpatterns = [
    path("basiс/", views.AboutUsView.as_view(), name="basic"),
    path('', views.index, name='index')
]
