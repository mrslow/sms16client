from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sms16client',
    version='0.1.0',
    description='Client for sms16 HTTP API.',
    long_description=readme,
    author='Anton Shchetikhin',
    author_email='animal2k@gmail.com',
    url='https://github.com/mrslow/sms16client',
    license=license
)

