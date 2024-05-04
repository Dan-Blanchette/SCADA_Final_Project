import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from django.conf import settings
from home import utils, models


def home(request):
        
    return render(
                    request,
                    "home/home.html",
                    {
                    }
    )


def live_graphs(request):
    return render(
                    request,
                    'home/live-graphs.html',
                    {

                    }
    )