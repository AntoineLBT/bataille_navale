import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="battleship",  # Replace with your own username
    version="1.0.0",
    author="Antoine LE BOUT",
    author_email="antoine.lebout@gmail.com",
    description="Partial battleship implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntoineLBT/bataille_navale",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": ["battleship=view.view:main"],
    },
)
