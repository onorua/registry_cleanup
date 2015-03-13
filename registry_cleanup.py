#!/usr/bin/env python
import requests
from requests.auth import HTTPBasicAuth
import sys
import os
import argparse

def get_url(url, image, tag=None):

    if 'v1/repositories' not in url:
        url = url+"/v1/repositories/{}/tags".format(image)
    else:
        url = url.format(image)

    if tag:
        url = url + "/{}".format(tag)
    return url


def do_cleanup(local, layer):
    if '/data/images/' in local:
        pass
    elif '/data/' in local:
        local = os.path.normpath(local+'/images/')
    elif 'data' not in local:
        local = os.path.normpath(local+'/data/images/')
    os.system("rm -rf {}".format(os.path.normpath(local+"/"+layer)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', dest='user', help="registry username")
    parser.add_argument('-p', '--password', dest='password', help="registry password")
    parser.add_argument('-o', '--url', dest='url', required=True, help="registry main URL")
    parser.add_argument('-i', '--image', dest='image', required=True, help="image to delete")
    parser.add_argument('-t', '--tag', dest='tag', help="image tag to delete")
    parser.add_argument('-l', '--local', dest='local', help="local images registry")

    args = parser.parse_args()

    image = args.image
    tag = args.tag
    user = args.user
    passwd = args.password
    url = args.url
    local = args.local

    if 'https://' not in url:
        url = 'https://'+url

    auth = HTTPBasicAuth(user, passwd)
    req = requests.get(get_url(url, image), auth=auth)
    content = req.json()

    for k, v in content.items():
        if tag and tag == k:
            do_delete = False
            cleanup = requests.get(url+"/v1/images/{}/ancestry".format(v),
                                   auth=auth).json()
            for i in cleanup:
                if not local:
                    print i
                else:
                    do_delete = True
                    do_cleanup(local, i)
            if do_delete:
                requests.delete(get_url(url, image, tag), auth=auth)
        elif not tag:
            print k

main()
