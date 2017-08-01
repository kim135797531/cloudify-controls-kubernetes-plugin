# coding=utf-8
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import kubernetes

# Cloudify 기본 import
from cloudify import ctx
from cloudify.exceptions import NonRecoverableError, RecoverableError
from cloudify.decorators import operation

from control_kubernetes import kubernetes_client


@operation
def test_get_pods(params, **kwargs):
    client = kubernetes_client.get_client()
    pods = client.list_pod_for_all_namespaces(watch=False)

    ctx.logger.info('Listing pods...')
    for i in pods.items:
        ctx.logger.info('{}\t{}\t{}'.format(i.status.pod_ip,
                                            i.metadata.namespace,
                                            i.metadata.name))

    ctx.instance.runtime_properties['some_property'] = params


@operation
def create_container(params, **kwargs):
    pass


@operation
def start(params, **kwargs):
    pass


@operation
def stop(params, **kwargs):
    pass


@operation
def remove_container(params, **kwargs):
    pass


# def get_image():
# def pull():
# def import_image():
