import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from django.conf import settings
from schneider_plc import utils, models


def control_mode(request):

    return render(
                    request,
                    "schneider_plc/control_mode.html",
                    {
                    }
    )


def data_table(request):

    return render(
                    request,
                    "schneider_plc/data_table.html",
                    {
                    }
    )