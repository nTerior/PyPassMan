import setuptools

classifiers = [
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3.9",
    "Operating System :: POSIX",
    "Natural Language :: English"
]

setuptools.setup(
    name="PyPassMan",
    version="1.0.0",
    description="An encrypted and secure password manager",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cephox/PyPassMan",
    author="ce_phox",
    author_email="paul-stier@gmx.de",
    license='GPLv3',
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "pypassman=PyPassMan.pypassman:main"
        ]
    }
)
