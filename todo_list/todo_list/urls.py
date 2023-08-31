"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URL maršrutas į Django administravimo sąsają. Paprastai naudojamas projekto administratorių.
    path('admin/', admin.site.urls),
    
    # Čia įtraukiami visi URL maršrutai iš 'base' aplikacijos.
    # T.y., kai lankytojas pasiekia pagrindinį svetainės adresą, jis bus nukreiptas į 'base.urls' failą
    # ir bus ieškoma tinkamo URL maršruto tame faile.
    path('', include('base.urls')),
]

