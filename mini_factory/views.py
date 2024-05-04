import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from django.conf import settings
from mini_factory import utils, models


def control_mode(request):
        
    return render(
                    request,
                    "mini_factory/control_mode.html",
                    {
                    }
    )


def data_table(request):
        
    return render(
                    request,
                    "mini_factory/data_table.html",
                    {
                    }
    )