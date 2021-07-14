from setuptools import setup

setup(
    name='graphene_mongo_async',
    version='0.0.1',
    packages=['graphene_mongo_async'],
    install_requires=[
        'motor',
        'graphene',
        'importlib; python_version >= "3.6"',
    ],
)
