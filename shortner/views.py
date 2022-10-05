from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import ShortURL

# Create your views here.
def redirect(request, our_short_url):
    ShortURLObject = get_object_or_404(ShortURL, shorten_url=our_short_url)
    return HttpResponseRedirect(ShortURLObject.original_url)

def index(request):
    return HttpResponse("Type /gooogle in url bar after domain name")