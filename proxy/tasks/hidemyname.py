import requests

from proxy.models import Resource


RESOURCE = Resource.objects.get(name='hidemyname')


def fetch_proxy_hosts():
    res = requests.get(RESOURCE.url)

    print(res)
    print(res.text)


fetch_proxy_hosts()
