from setuptools import setup

setup(
    name="Flask-Analytics",
    version="0.0.1",
    license="MIT",
    author="Mihir Singh (@citruspi)",
    author_email="citruspi@riseup.net",
    packages=['flask_analytics'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ]
)
