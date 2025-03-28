from setuptools import setup, find_packages

setup(
    name="torchplotlib",
    version="0.1.0",
    description="wrapper for matplotlib to plot tensor",
    author="João Pedro Pires",
    author_email="jppirest@gmail.com",
    packages=find_packages(),
    install_requires=[
        "torch",
        "matplotlib",
        "numpy"
    ],
)
