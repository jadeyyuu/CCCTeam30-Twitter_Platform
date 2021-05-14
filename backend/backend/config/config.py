# coding: utf-8
"""
CouchDB
This file including the basic configuration information
"""

HTTP_X_API_KEY = 'HTTP_X_API_KEY'
API_KEY = '227415ba68c811e9b1a48c8590c7151e'

COUCHDB_URL = 'http://{}:{}@{}:{}/'
COUCHDB_DOMAIN = '172.26.130.42'
COUCHDB_DOMAINS = ['172.26.130.42', '172.26.131.236', '172.26.134.19']
COUCHDB_USERNAME = 'admin'
COUCHDB_PASSWORD = 'password'
COUCHDB_PORTS = 5984
COUCHDB_TWEET_DB = 'origin_tweet'
COUCHDB_TRACK_DB = 'track'
COUCHDB_TIME_DB = 'time_{}_{}_{}_{}_{}'

OBJECT_STORAGE_URL = 'https://swift.rc.nectar.org.au/v1/AUTH_0ca7fac1451c4f519376f20812279bfc'
OBJECT_STORAGE_PREURL = 'https://swift.rc.nectar.org.au/v1/AUTH_0ca7fac1451c4f519376f20812279bfc'
OBJECT_STORAGE_CONTAINER = 'twitter_pic'
JSON_STORAGE_CONTAINER = 'results'

OS_AUTH_URL = 'https://keystone.rc.nectar.org.au:5000'
OS_TENANT_ID = 'unimelb-comp90024-group-7'
OS_USERNAME = 'yuxuanl2@student.unimelb.edu.au'
OS_PASSWORD = 'NjNkMjk0Y2Y0MGYwYjlj'
OS_VERSION = '3'

INFLUXDB_DOMAIN = '172.26.129.75'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = 'admin'
INFLUXDB_PASSWORD = 'password'
INFLUXDB_DATABASE = 'backend'

FOOD_TAGS = ['']