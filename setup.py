from setuptools import setup

setup(
    name='guitarparty',
    version='0.1',
    description='A Python library for interfacing with the guitarparty.com API',
    author='Guitarparty.com',
    author_email='support@guitarparty.com',
    url='http://www.guitarparty.com/developers/',
    packages=['guitarparty'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
    ],
    keywords='guitarparty rest api client service',
    license='MIT',
    install_requires=[
        'setuptools', 'requests',
    ],
)
