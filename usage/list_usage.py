from keystoneauth1.identity import v2
from keystoneauth1 import session
from novaclient import client as nova_client
from django.conf import settings
from datetime import date, timedelta, datetime, time
from keystoneclient import client as keystone_client
from cinderclient import client as cinder_client

def get_credentials():
    return settings.KEYSTONE_CREDENTIALS

def get_session(credentials):
    auth = v2.Password(**credentials)
    sess = session.Session(auth=auth)
    return sess

def get_usage(session, start=datetime.combine((date.today() - timedelta(days=28)), time.min), end=datetime.combine((date.today() + timedelta(days=1)),time.min)):
    nova = nova_client.Client(version='2.0', session=session)
    return nova.usage.list(start=start, end=end)

def get_tenant_usage(session, tenant_id, start=datetime.combine((date.today() - timedelta(days=28)), time.min), end=datetime.combine((date.today() + timedelta(days=1)),time.min)):
    nova = nova_client.Client(version='2.0', session=session)
    return nova.usage.get(tenant_id=tenant_id, start=start, end=end)

def get_project_name(session, tenant_id):
    keystone =  keystone_client.Client(session=session)
    return keystone.tenants.get(tenant_id).name

#def get_simple_usage(session, usages):
#    simple_usage = []
#    for usage in usages:
#        simple_usage.append({
#            'id': usage.tenant_id,
#            'name': get_project_name(session=session, tenant_id=usage.tenant_id),
#            'ram': "%.2f" % usage.total_memory_mb_usage,
#            'cpu': "%.2f" % usage.total_vcpus_usage,
#            'disk': "%.2f" % usage.total_local_gb_usage
#            })
#   
#    return simple_usage

def get_volumes(session, tenant_id=None):
    cinder = cinder_client.Client(version='2', session=session)
    return cinder.volumes.list(search_opts={'all_tenants': 1})

def get_hypervisor_stats(session):
    nova = nova_client.Client(version='2.0', session=session)
    return nova.hypervisor_stats.statistics()._info
