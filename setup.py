from setuptools import setup, find_packages

from boiler_plate import __version__

setup(
    name="boiler_plate",
    version = __version__,
    author="Fix Me",
    author_email="fix.me@landregistry.gsi.gov.uk",
    packages=find_packages(),
    install_requires=["flask"],
    tests_require=["flask"],
    test_suite="boiler_plate.test_suite.suite",
    entry_points={'console_scripts':
                  ['boiler_plate = boiler_plate.run:main']}
)
