from setuptools import setup, find_packages

from boiler_plate import __version__

setup(
    name="boiler_plate",
    version = __version__,
    author="Fred Bloggs",
    author_email="fred.bloggs@landregistry.gsi.gov.uk",
    packages=find_packages(),
    install_requires=["flask"],
)
