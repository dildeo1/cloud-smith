from setuptools import setup, find_packages

setup(
    name="example-package", 
    version="0.1.0", 
    author="Farhan Sayeed",
    author_email="fs10956@gmail.com",
    description="Example package for Cloudsmith assessment.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},    
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.25.0",
    ]
)