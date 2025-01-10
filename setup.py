# setup.py

from setuptools import setup, find_packages

setup(
    name="WAbot",  # Replace with your desired package name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "undetected-chromedriver",
        "webdriver_manager",
        "beautifulsoup4",
        "pyperclip"
    ],
    description="A WhatsApp bot automation library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/WAbot",  # Replace with your GitHub or project URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
