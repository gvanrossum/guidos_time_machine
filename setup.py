from setuptools import setup

classifiers = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Python Software Foundation License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development",
]

setup(
    name="guidos_time_machine",
    version="0.0",
    description="Guido's time machine",
    author="Guido van Rossum",
    author_email="guido@python.org",
    license="PSF",
    packages=["guidos_time_machine"],
    classifiers=classifiers,
)
