from setuptools import setup, find_packages

setup(
    name="mock_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "numpy"
    ],
    extras_require={
        "dev": ["pytest", "flake8"]
    },
)
