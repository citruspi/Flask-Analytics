from setuptools import setup

setup(
    name="Flask-Analytics",
    version="0.0.1",
    author="Mihir Singh (@citruspi)",
    author_email="hello@mihirsingh.com",
    url='https://github.com/citruspi/Flask-Analytics',
    packages=['flask_analytics'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'License :: Public Domain',
    ]
)
