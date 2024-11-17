from setuptools import setup, find_packages

setup(
    name="env_extractor",
    version="0.1",
    packages=find_packages(),  # This will find all packages (including env_extractor)
    install_requires=[
        "argparse",  # for argument parsing
    ],
    entry_points={
        'console_scripts': [
            'env-extractor = env_extractor.main:main',  # Point to the main.py in the root
        ],
    },
    author="Sharan",
    author_email="ksharam2001@gmail.com",
    description="A command-line tool to extract environment variables from Python files",
    url="https://github.com/sudoSharun/env-scraperr",  # Replace with your GitHub repo URL
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    long_description=open('README.md').read(),  # Long description from the README file
    long_description_content_type='text/markdown',
)
