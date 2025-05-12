from setuptools import setup

setup(
    name="mock_project",
    version="0.1.0",
    install_requires=[
        "django==3.1.7",
        "requests>=2.0.0",
        "numpy"
    ],
    extras_require={
        "dev": [
            "pytest",
            "flake8",
            "black"
        ]
    }
)