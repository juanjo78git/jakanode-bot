"""
Requires
"""

from setuptools import find_packages, setup

setup(
    name="jakanode-bot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "anyio==4.8.0",
        "certifi==2025.1.31",
        "h11==0.14.0",
        "httpcore==1.0.7",
        "httpx==0.28.1",
        "idna==3.10",
        "python-dotenv==1.0.1",
        "python-telegram-bot==21.10",
        "sniffio==1.3.1",
        "typing_extensions==4.12.2",
    ],
    description="Jakanode-bot project built with Python.",
    author="Jakanode",
    author_email="jakanode@jakanode.com",
)
