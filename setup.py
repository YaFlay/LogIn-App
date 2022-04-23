import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Login app",
    version="1.0.1",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/YaFlay/reader",
    author="YaFlay",
    author_email="yaflay@vk.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["login"],
    include_package_data=True,
    install_requires=[
        'os', 'random', 'tkinter', 'simplecrypt', 'email', 'smtplib'
    ],
    entry_points={"console_scripts": ["login_app=login.__main__:main"]},
)