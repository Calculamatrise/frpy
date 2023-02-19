from setuptools import *

with open("README.md", "r") as r:
    long_description = r.read()

setup(
    name="frpy", # Replace with your own username
    version="0.2.0",
    author="Calculamatrise",
    author_email="calculamatrise@gmail.com",
    description="An api for FRHD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Calculamatrise/frpy/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        'requests'
    ],
    python_requires='>=3.8'
)
