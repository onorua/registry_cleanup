# registry_cleanup
Docker private registry cleanup script


## build image
docker build -t registry-cleanup . 

## cleanup your registry
you can setup username and password to easy remove the same images on different registries:
```
USERNAME='username'
PASSWD='your password'
URL="https://private-registry.org"
```

In case you simply want to check available tags in the registry for paritcular image:

``` bash
docker run -i -t --rm=true -v /var/container_data/registry/otlabs-registry:/opt/registry registry-cleanup -u $USERNAME -p $PASSWD -o  "$URL" -i {image_name to delete}
```

for example:
```
docker run -i -t --rm=true -v /var/container_data/registry/otlabs-registry:/opt/registry registry-cleanup -u $USERNAME -p $PASSWD -o  "$URL" -i otlabs/tsmue-spdeploy_installmariadb
56
b-64-RELEASE
```

To show image layer IDs you can do following:
```
docker run -i -t --rm=true -v /var/container_data/registry/otlabs-registry:/opt/registry registry-cleanup -u $USERNAME -p $PASSWD -o  "$URL" -i {image to delete} -t {tag to delete}
```

to continue previous example:
```
docker run -i -t --rm=true -v /var/container_data/registry/otlabs-registry:/opt/registry registry-cleanup -u $USERNAME -p $PASSWD -o  "$URL" -i otlabs/tsmue-spdeploy_installmariadb -t 56 
ded863887b1fb9fcf2b55b1149cf40dd027425441d219739696e785fd3059164
d4f5fd91f89429c3dad82412888e98a28d5ef17b4ac25b881ebddcc8fd1c571d
b6610e084a91fdb169c303e8198665a99fb8c3121c77daa0aea9601826ca7276
36ab2486d0a0c7954b564fdae2a6290bfc9a4638ae09a781c661b3b97bde95f4
5990951d75f1eb7cc3f16c78b76c132b86733db462454ebc7c8e31eb45ba389e
613481da19c78d7d643d45a8458f250bf0395bfdaa9aa903593a3f569b989dd5
f35d750f8e6805c6bdf304ebde0bc1a4ef613089b631e57375dbcee72daf7fee
4042b94e97867daf42994a059b3d171a2f9f7d9c12a4d443dd3a1f812c9c05c9
61208b168031900bd70325956a2df853eb834b0c651571850031e73fe88d23da
037cd6cea0a7c029055b5ade3a37281b995c9b60f11977ff6e0d0fbed0d0ed49
4bb3d10a3af5422d7fe60327e8bfc14ef04b85964dc6f6f162d71ed1b198f27a
56a04651b0b35d040323209950abaa9244aee25026dbc78cdcd6f5802e4eb368
8f86117dd1caf853ce8f0cfa84a88ca569c742eba8b06a605c4537a2b8cd2597
d2b29e763fd595ce8f63a92bb34ac9c067684e1d3d87e2c3947aabff56704961
4e1fe3bb4024e9ba399290c53c0a8f36cf830958b8b2e18a4399e285b3a198d7
4b78ac109edf2b1eb9ff9b02d64e916113c334a1b74a29385705ca88add23bd5
2950d92d98a0dea4dd52b603b05f1851b5338572303f78f1105d0d55ff8feb4b
3ed44a189f6f4bcc2d57c1df5600286f515a8bca5bcd8ccc16bc2bbafeeadf58
e54ca5efa2e962582a223ca9810f7f1b62ea9b5c3975d14a5da79d3bf6020f37
6c37f792ddacad573016e6aea7fc9fb377127b4767ce6104c9f869314a12041e
83ff768040a07b1d8bdc142a98841e37428a2e18f2ed944e4dcfd99170618251
2f4b4d6a4a069aba521ca0067b9263e29d7de84d121ff60ee101242bcc36c13b
d7ac5e4f18124966d8e8a06a0c4c4236328ba8fb13b6e44cb017ad524aac865c
511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158
```

if you are sure that you want to delete this image with all layers from registry, it's necessary to run it on registry server itself with -l parameter where you put registry data:
```
docker run -i -t --rm=true -v /var/container_data/registry/otlabs-registry:/opt/registry registry-cleanup -u $USERNAME -p $PASSWD -o  "$URL" -i {image to delete} -t {tag to delete} -l /opt/registry
```

for instance, if you would like to delete image from pevious example:
```
docker run -i -t --rm=true -v /var/container_data/registry/otlabs-registry:/opt/registry registry-cleanup -u $USERNAME -p $PASSWD -o  "$URL" -i otlabs/tsmue-spdeploy_installmariadb -t 56 -l /opt/registry
```
