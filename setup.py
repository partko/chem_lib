
import os
from setuptools import setup


setup(
    name = "chemhelper",
    version = "0.0.4",
    description = "Simple library for chemistry",
    author = "Vladimir Partko",
    author_email = "partko.vl.3@gmail.com",
    license = "MIT",
    packages = ["chemhelper", os.path.join("chemhelper", "chem")]
    )

