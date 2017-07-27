# coding=utf-8
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.


from setuptools import setup


setup(

    # Do not use underscores in the plugin name.
    name='cloudify-controls-kubernetes-plugin',

    version='0.1',
    author='Dongmin Kim, Hanyeong Lee',
    author_email='kim135797531g@gmail.com, esteir4216@naver.com',
    description='Control Kubernetes from Cloudify',

    packages=['control_kubernetes'],

    license='LICENSE',
    zip_safe=False,
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        "cloudify-plugins-common>=4.1"
        # TODO: kubernetes python 플러그인 넣기
        # 'kubernetes-py>=x.x.x'
    ],
    test_requires=[
        "cloudify-dsl-parser>=4.1"
        "nose"
    ]
)