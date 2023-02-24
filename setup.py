from setuptools import find_packages, setup

with open('README.md', 'r') as r:
    long_description = r.read()

setup(
    name = 'frpy',
    version = '0.2.0',
    description = "An api wrapper for Free Rider HD",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
	author = 'Calculamatrise',
    url = "https://github.com/Calculamatrise/frpy",
	download_url = "https://github.com/Calculamatrise/frpy/archive/refs/heads/master.zip",
	keywords = [
		'frhd',
		'wrapper'
	],
	license = 'GPL-3.0 license',
    classifiers = [
		"Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ],
	packages = find_packages(),
    python_requires = '>=3.8',
	install_requires = [
        'requests'
    ]
)

# python -m build
# python -m twine upload -r testpypi dist/*
# python -m twine upload -r pypi dist/*