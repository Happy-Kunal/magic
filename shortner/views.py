from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .models import ShortURL

# Create your views here.
def redirect_to(request, our_short_url):
    ShortURLObject = get_object_or_404(ShortURL, shorten_url=our_short_url)
    return redirect(ShortURLObject)

def index(request):
    return HttpResponse("Type /gooogle in url bar after domain name")