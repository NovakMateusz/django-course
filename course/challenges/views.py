import calendar

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

MONTHS = [calendar.month_name[i].lower() for i in range(1, 13)]


def index(request):
    anchors_urls = [reverse('month-challenges', args=[item]) for item in MONTHS]
    anchors_tags = [f'<a href="{anchors_urls[i]}">{item}</a>' for i, item in enumerate(MONTHS)]
    list_of_months = [f"<li>{item}</li>" for item in anchors_tags]
    response_html = f"<h1><ul>{''.join(list_of_months)}</ul></h1>"
    return HttpResponse(response_html)


def monthly_challenge_by_number(request, month):
    try:
        month_redirect = MONTHS[month - 1]
        redirect_url = reverse('month-challenges', args=[month_redirect])
        return HttpResponseRedirect(redirect_url)
    except IndexError:
        return HttpResponseNotFound('This month is not supported!')


def monthly_challenge(request, month):
    if month in MONTHS:
        return HttpResponse(f"Hello {month.capitalize()}!")
    return HttpResponseNotFound('This month is not supported!')


def test_rendering_template(request):
    return HttpResponse(render_to_string('challenges/test.html'))

