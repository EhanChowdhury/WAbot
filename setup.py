# setup.py

from setuptools import setup, find_packages

setup(
    name="WAbot",  # Replace with your desired package name
    version="0.4",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "webdriver_manager"
    ],
    description="A WhatsApp bot automation library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ehan Chowdhury",
    author_email="nibizsoft@gmail.com",
    url="https://github.com/EhanChowdhury/WAbot",  # Replace with your GitHub or project URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
