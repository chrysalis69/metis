# Metis
## For African Research Cloud

This project provide a dashboard to view usage of resources inside a openstack cloud. It requires an account with admin access to retrieve the info using various openstack apis.

### Getting Started
1. Create a environment file with credentials
```
METIS_KEYSTONE_USERNAME=
METIS_KEYSTONE_PASSWORD=
METIS_KEYSTONE_AUTH_URL=
METIS_KEYSTONE_TENANT_NAME=
```
2. Run docker providing the env file
```
docker run --env-file <my_envfile.env> -p 8000:8000 chrysalis69/metis
```
