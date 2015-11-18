#!/bin/bash
salt_ips=$(mktemp)
aws_ips=$(mktemp)
tmpfile=$(mktemp)
ssh salt@10.0.17.64 'salt \* grains.get ipv4' | grep '.- 10'|awk '{print $2}' >> $tmpfile
ssh salt@10.0.17.147 'salt \* grains.get ipv4' | grep '.- 10'|awk '{print $2}' >> $tmpfile
sort $tmpfile > $salt_ips
~/src/ops.awstools/awstools/list-all-ec2-ips.sh| sort > $aws_ips
comm -3 -2 $aws_ips $salt_ips
