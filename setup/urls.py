
from django.contrib import admin
from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('imagem/', imagem )
]
