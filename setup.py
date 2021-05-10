#!/usr/bin/env python
"""Setup, configuration, and metadata file for the modeldata package."""
from setuptools import find_packages
from setuptools import setup


install_requires = ["pandas"]
doc_requires = [
    "nbsphinx",
    "recommonmark",
    "sphinx",
    "sphinx_rtd_theme",
    "sphinxcontrib.napoleon",
]
test_requires = ["pytest"]
dev_requires = ["black", "flake8", "mypy", "pre-commit"] + doc_requires + test_requires

setup(
    name="modeldata",
    version="0.1.0",
    license="proprietary",
    description="Data sets useful for teaching machine learning",
    url="https://github.com/bradleyboehmke/modeldata",
    author="Brad Boehmke",
    author_email="bradleyboehmke@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={"docs": doc_requires, "tests": test_requires, "dev": dev_requires},
    test_suite="tests",
    package_data={"modeldata": ["data/*.csv"]},
    include_package_data=True,
    project_urls={
        "Source": "https://github.com/bradleyboehmke/modeldata",
        "Bug Reports": "https://github.com/bradleyboehmke/modeldata/issues",
    },
)
