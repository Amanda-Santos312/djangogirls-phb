from django.urls import path
from . import views #Importei rodas as views do blog

urlpatterns = [
    path('', views.post_list, name='post_list'), #nome identificador
]
