"""my_first_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def home_page(request):
    # http://127.0.0.1:8000/
    context = {'name': 'Mims Bot'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def portfolio(request):
    random_number = randint(0, 100)
    image_url = "https://picsum.photos/400/600/?image={}".format(random_number)
    context = {'gallery_image': image_url}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)


def gallery(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0, 100)
        image_urls.append(("https://picsum.photos/400/600/?image={}".format(random_number)))

    context = {'gallery_images': image_urls, "gallery_image": "https://vignette.wikia.nocookie.net/rickandmorty/images/9/92/Roy.png/revision/latest?cb=20160919070029"}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def base_route(request):
    return HttpResponse('<h1>Hi</h1><p>this is the base route page</p>')


urlpatterns = [
    path('home/', home_page),
    path('portfolio/', portfolio),
    path('gallery', gallery),
    path('', base_route)
]
