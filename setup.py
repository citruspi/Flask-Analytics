from setuptools import setup

setup(
    name="Flask-Analytics",
    version="0.6.0",
    author="Mihir Singh (@citruspi)",
    author_email="hello@mihirsingh.com",
    description="Analytics snippets generator extension for the Flask framework",
    url='https://github.com/citruspi/Flask-Analytics',
    packages=['flask_analytics', 'flask_analytics.providers'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'License :: Public Domain',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet'
    ]
)
