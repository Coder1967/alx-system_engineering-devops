#!/usr/bin/python3
from fabric.api import put, env
""" fabfile to help transport the task file"""
env.hosts = ['3.237.30.57', '3.89.160.202', '100.25.148.210']

def deploy():
    put('0-block_all_incoming_traffic_but', '~/')
