from setuptools import setup, find_packages

setup(
    name="torchplotlib",
    version="0.0.1",
    description="wrapper for matplotlib to plot torch tensors",
    author="João Pedro Pires",
    author_email="jppirest@gmail.com",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy"
    ],
)
