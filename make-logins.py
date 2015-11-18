#!/usr/bin/python

import json
import boto.ec2


conn = boto.ec2.connect_to_region('us-east-1')

instances = {}
only_instances = conn.get_only_instances()

for instance in only_instances:
    instances[instance.id] = {'ip': instance.private_ip_address}
    instances[instance.id]['public_ip'] = instance.ip_address

all_tags = conn.get_all_tags()

for tag in all_tags:
    if tag.res_id in instances:
        instance_id = tag.res_id
        instances[tag.res_id][tag.name] =  tag.value

for instance in instances.values():
    if 'Login' in instance:
       login = instance['Login']
    elif 'opsworks:stack' in instance:
        login = 'jeff'
    else:
        login = 'ubuntu'

    if 'Port' in instance:
        port = "-p %s " % instance['Port']
        ip = instance['public_ip']
    else:
        port = ""
        ip = instance['ip']

    print "%s:%s %s@%s" % (instance['ip'], port, login, ip)


