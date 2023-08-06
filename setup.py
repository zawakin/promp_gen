#!/usr/bin/env python
from __future__ import unicode_literals

import os
import io
from setuptools import setup, find_packages


def setup_package():
    package_name = "auto_prompt_gen"
    root = os.path.abspath(os.path.dirname(__file__))

    # Read in package meta from about.py
    about_path = os.path.join(root, package_name, "about.py")
    with io.open(about_path, encoding="utf8") as f:
        about = {}
        exec(f.read(), about)

    # Get readme
    readme_path = os.path.join(root, "README.md")
    with io.open(readme_path, encoding="utf8") as f:
        readme = f.read()

    setup(
        name=package_name,
        description=about["__summary__"],
        long_description=readme,
        long_description_content_type="text/markdown",
        author=about["__author__"],
        author_email=about["__email__"],
        url=about["__uri__"],
        version=about["__version__"],
        license=about["__license__"],
        packages=find_packages(),
        keywords=["prompt", "generator", "auto_prompt_gen",
                  "ai_art", "art", "dalle", "dalle2", "midjourney", "dalle3"],
        install_requires=['numpy', 'pandas'],
        zip_safe=True,
    )


if __name__ == "__main__":
    setup_package()
