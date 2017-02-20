from django.shortcuts import render, redirect
from usage.list_usage import get_credentials, get_session, get_usage, get_tenant_usage, get_volumes, get_hypervisor_stats
from datetime import date, timedelta, datetime, time
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import json

def fix_arrays(array):
    return_array = []
    for item in array:
        return_array.append(item._info)
    return return_array

def detail(request, start, end, tenant_id):
    session = get_session(get_credentials())
    start_time = datetime.strptime(start, '%Y-%m-%d')
    end_time = datetime.strptime(end, '%Y-%m-%d')
    if request.user.is_authenticated:
        data = get_tenant_usage(session=session, tenant_id=tenant_id, start=start_time, end=end_time)
        return HttpResponse(json.dumps(data._info), content_type="application/json")
    else:
        return redirect('/usage/')

def usages(request, start, end):
    session = get_session(get_credentials())
    start_time = datetime.strptime(start, '%Y-%m-%d')
    end_time = datetime.strptime(end, '%Y-%m-%d')
    raw_usages = get_usage(session=session, start=start_time, end=end_time)
    return_usage = []
    for usage in raw_usages:
        return_usage.append(usage._info)
    return HttpResponse(json.dumps(return_usage), content_type="application/json")

def volumes(request):
    session = get_session(get_credentials())
    raw_volumes = get_volumes(session=session)
    return HttpResponse(json.dumps(fix_arrays(raw_volumes)), content_type="application/json")

def hypervisor_stats(request):
    session = get_session(get_credentials())
    return HttpResponse(json.dumps(get_hypervisor_stats(session=session)), content_type="application/json")

