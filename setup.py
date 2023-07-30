from setuptools import find_packages, setup

VERSION = "0.0.16"
DESCRIPTION = ""
LONG_DESCRIPTION = ""

setup(
    name="photondemo",
    version=VERSION,
    author="Charlie Day",
    url="https://github.com/charliemday/photondemo",
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],  # add any additional packages that
    # needs to be installed along with your package
    keywords=["python"],
    classifiers=[],
)




