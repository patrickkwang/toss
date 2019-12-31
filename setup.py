"""Setup file for toss package."""
from setuptools import setup

setup(
    name='toss',
    version='1.0.0',
    author='Patrick Wang',
    author_email='patrick@covar.com',
    url='https://github.com/patrickkwang/toss',
    description='Terms-of-Service Server',
    packages=['toss'],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    python_requires='>=3.8',
)
