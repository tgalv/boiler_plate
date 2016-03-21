from setuptools import setup, find_packages

setup(
    name="boiler_plate",
    version = "0.1",
    author="Fix Me",
    author_email="fix.me@landregistry.gsi.gov.uk",
    packages=find_packages(),
    install_requires=["flask"],
    tests_require=["flask"],
    test_suite="boiler_plate.test_suite.suite",
    entry_points={'console_scripts':
                  ['boiler_plate = boiler_plate.main:main']}
)
