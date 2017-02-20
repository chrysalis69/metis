from django.shortcuts import render, redirect
from django.template import loader
from usage.list_usage import get_credentials, get_session, get_usage, get_tenant_usage
from datetime import date, timedelta, datetime, time
from django.http import HttpResponse

def index(request):
    start = datetime.combine((date.today() - timedelta(weeks=4)), time.min)
    end = datetime.combine((date.today() + timedelta(days=1)),time.min)
    return redirect('/usage/'+start.strftime('%Y-%m-%d')+'/'+end.strftime('%Y-%m-%d')+'/') 

def usages(request, start, end):
    template = loader.get_template('usage/index.html')
    start_time = datetime.strptime(start, '%Y-%m-%d')
    end_time = datetime.strptime(end, '%Y-%m-%d')
    return HttpResponse(template.render({
        'time_range': {
            'from': start_time.strftime('%Y-%m-%d'),
            'to': end_time.strftime('%Y-%m-%d')
            }
        }, request))

def detail(request, start, end, tenant_id):
    template = loader.get_template('usage/tenant_details.html')
    session = get_session(get_credentials())
    start_time = datetime.strptime(start, '%Y-%m-%d')
    end_time = datetime.strptime(end, '%Y-%m-%d')
    return HttpResponse(template.render(get_tenant_usage(session=session, tenant_id=tenant_id, start=start_time, end=end_time)._info, request))

