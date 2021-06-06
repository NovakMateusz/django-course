import calendar

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


MONTHS = [calendar.month_name[i].lower() for i in range(1, 13)]


def monthly_challenge(request, month):
    if month in MONTHS:
        return HttpResponse(f"Hello {month.capitalize()}!")
    return HttpResponseNotFound('This month is not supported!')
