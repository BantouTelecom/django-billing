from setuptools import setup

setup(
    name='django-billing',
    version='0.1.5',
    author='Gabriel Grant',
    packages=[
        'billing',
        'billing.processor',
        'billing.processor.simple_account',
        'billing.templatetags',
        'billing.tests',
        'billing_management',
        'billing_management.management',
        'billing_management.management.commands',
    ],
    # django.utils.translation.trans_real tries to access <app>.__file__,
    # which does not exist when namespace packages are declared that way.
    # Let's use the "old" way until django.utils.translation is fixed.
    #namespace_packages=['billing', 'billing.processor'],
    license='AGPL',
    long_description=open('README').read(),
    install_requires=[
        'python-pricing',
        'django-annoying',
        'django-model-utils',
        'South',
        'jsonfield',
        'ordereddict',
    ],
    dependency_links = [
    	'http://github.com/gabrielgrant/python-pricing/tarball/master#egg=python-pricing',
    ]
)
