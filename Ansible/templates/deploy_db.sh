#!/usr/bin/env bash
. ./CCC-grp-30-openrc.sh; ansible-playbook --ask-become-pass deploy_db.yaml -i inventory/hosts.ini