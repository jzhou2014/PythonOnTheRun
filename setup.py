from setuptools import find_packages, setup
#https://setuptools.pypa.io/en/latest/userguide/quickstart.html
#https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
setup(
    name="move-python",
    version="1.0.0",
    packages=find_packages(),
    description="Move Python study guide",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
