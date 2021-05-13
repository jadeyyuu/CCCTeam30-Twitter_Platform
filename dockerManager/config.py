# -*- coding: utf-8 -*-

DOCKER_DOMAIN = {
    'instance_1': dict(
        domain='172.26.130.42',
        port=8866
    ),
    'instance_2': dict(
        domain='172.26.131.236',
        port=8866
    ),
    'instance_3': dict(
        domain='172.26.134.19',
        port=8866
    ),
    'instance_4': dict(
        domain='172.26.129.75',
        port=8866,
    ),
}

COUCH_DB_PORTS = {
    '5984/tcp': 5984,
    '5895/tcp': 5985,
    '5896/tcp': 5986,
    '5897/tcp': 5987,
}

COUCH_DB_VOLUMES = {
    '/home/ubuntu/couchdb/etc/docker.ini': {'bind': '/opt/couchdb/etc/local.d/docker.ini', 'mode': 'rw'},
    '/home/ubuntu/couchdb/etc/vm.args': {'bind': '/opt/couchdb/etc/vm.args', 'mode': 'rw'},
    '/home/ubuntu/couchdb/etc/default.ini': {'bind': '/opt/couchdb/etc/default.ini', 'mode': 'rw'},
    '/data/': {'bind': '/opt/couchdb/data', 'mode': 'rw'}
}

COUCH_DB_USER = 'admin'
COUCH_DB_PASSWORD = '123456'
COUCH_DB_ENV = ['COUCHDB_USER={}'.format(COUCH_DB_USER), 'COUCHDB_PASSWORD={}'.format(COUCH_DB_PASSWORD)]

DJANGO_PORTS = {
    '8080/tcp': 8080
}

DJANGO_VOLUMES = {
    '/home/ubuntu/backend/': {'bind': ''}
}

NGINX_PORTS = {
    '80/tcp': 80
}

INFLUXDB_PORTS = {
    '8083/tcp': 8083,
    '8086/tcp': 8086
}

INFLUXDB_VOLUMES = {
    '/data/influxdb/': {'bind': '/data/data/', 'mode': 'rw'},
}

INFLUXDB_ENV = {
    'ADMIN_USER': 'admin',
    'INFLUXDB_INIT_PWD': 'password'
}

GRAFANA_PORTS = {
    '3000/tcp': 3000
}

GRAFANA_VOLUMES = {
    '/data/grafana/': {'bind': '/var/lib/grafana', 'mode': 'rw'},
    '/home/ubuntu/config/grafana.ini': {'bind': '/etc/grafana/grafana.ini', 'mode': 'rw'}
}

GRAFANA_ENV = {
    'GF_AUTH_PROXY_ENABLED': True,
    'GF_AUTH_ANONYMOUS_ENABLED': True,
    'GF_SMTP_ENABLED': True,
    'GF_SMTP_HOST': 'smtp.gmail.com:465',
    'GF_SMTP_USER': 'patrickliuyx@gmail.com',
    'GF_SMTP_PASSWORD': '123456',
    'GF_SMTP_SKIP_VERIFY': True,
    'GF_SMTP_FROM_ADDRESS': 'patrickliuyx@gmail.com',
    'GF_SMTP_FROM_NAME': 'Grafana',
    'GF_SECURITY_ADMIN_USER': 'ccc30',
    'GF_SECURITY_ADMIN_PASSWORD': 'ccc30',
    'GF_SERVER_DOMAIN': '172.26.129.75',
}

RESTART = {"Name": "always"}

SMTP_PORTS = {
    '25/tcp': 10025
}

SMTP_ENV = {
    'RELAY_NETWORKS': ':0.0.0.0/0'
}

CADVISOR_PORTS = {
    '8082/tcp': 8082
}

CADVISOR_ENV = {
    'storage_driver': 'influxdb',
    'storage_driver_db': 'cAdvisor',
    'storage_driver_host': '172.26.129.75:8086'
}

CADVISOR_COMMAND = [
    '-storage_driver', 'influxdb',
    '-storage_driver_db', '',
    '-storage_driver_host', '172.26.129.75:8086'
]

CADVISOR_VOLUMES = {
    '/': {'bind': '/rootfs', 'mode': 'ro'},
    '/var/run': {'bind': '/var/run', 'mode': 'rw'},
    '/sys': {'bind':'/sys', 'mode': 'ro'},
    '/var/lib/docker/': {'bind': '/var/lib/docker', 'mode': 'ro'}
}