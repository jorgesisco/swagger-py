"""Setup script
"""

import os

from setuptools import setup

setup(
    name="swaggerpy",
    version="0.2.2",
    license="MIT",
    description="Library for accessing Swagger-enabled API's",
    author="Jorge Sisco",
    author_email="jorgesisco17@gmail.com",
    url="https://github.com/jorgesisco/swagger-py",
    packages=["swaggerpy"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    tests_require=["nose", "tissue", "coverage", "httpretty"],
    install_requires=["requests", "websocket-client"],
    entry_points="""
    [console_scripts]
    swagger-codegen = swaggerpy.codegen:main
    """
)
