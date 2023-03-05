from setuptools import find_packages, setup

setup(
    name="findmysound",
    packages=find_packages(include=["findmysound"]),
    version="0.1.0",
    description="Find My Sound helps you find a sound that you isolated in a video or an audio track.",
    author="Renaud Jester",
    license="MIT",
    setup_requires=["pytest-runner"],
    tests_require=["pytest==7.2.2"],
    test_suite="tests",
)
