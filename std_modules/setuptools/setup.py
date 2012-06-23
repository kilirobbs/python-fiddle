# http://habrahabr.ru/post/127441/

from setuptools import setup, find_packages
 
setup(
    name='home.news',
    version='0.1',
    description='News for Django',
    author='Elias',
    namespace_packages=['home'],
    packages=find_packages(),
    platforms='any',
    zip_safe=False,
    include_package_data=True,
    dependency_links=['git+ssh://git@git.example.com/app-admintools@v0.1#egg=admintools-0.1'],
    install_requires=['admintools==0.1'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
    ],
)