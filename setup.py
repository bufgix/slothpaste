import pathlib
from setuptools import setup

from slothpaste import __version__

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="sloth-paste",
    version=__version__,
    description="A simple file content sharing app.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bufgix/slothpaster",
    author="Bufgix",
    author_email="ooruc471@yandex.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["slothpaste"],
    include_package_data=True,
    install_requires=["requests", "beautifulsoup4", "pygments", "colorama", "pyperclip"],
    entry_points={
        "console_scripts": [
            "sloth=slothpate.__main__:main",
        ]
    },
)