from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name = 'pastebinfs',
    version = '0.1',
    description = 'Using Pastebin pastes as if they were files',
    long_description = readme(),
    keywords = 'pastebin file file-like',
    url = 'http://github.com/K0IN/pastebinfs',
    author = 'K0IN',
    author_email = 'thisk0in@gmail.com',
    license = 'MIT',
    packages = find_packages(),
    zip_safe = False,
    install_requires = [
        'requests',
])