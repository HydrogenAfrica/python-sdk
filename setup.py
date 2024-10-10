import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hydrogenpay_python",
    version="1.0.0",
    author="Hydrogen",
    author_email="support@hydrogenpay.com",
    description="Python library for Hydrogen for process payments through card transactions and account transfers, ensuring faster delivery of goods and services.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HydrogenAfrica/python-sdk",
    license="MIT",
    packages=setuptools.find_packages(),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'pycryptodome',
        'requests'
    ]
)
