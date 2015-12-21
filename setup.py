from setuptools import setup

setup(
    name="Flask-Analytics",
    version="0.5.2",
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet'
    ]
)
