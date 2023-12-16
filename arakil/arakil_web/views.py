import os

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    print("***********",os.getcwd())
    return render(request, 'index.html')