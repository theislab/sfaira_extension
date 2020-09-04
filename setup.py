from setuptools import setup, find_packages
import versioneer

author = 'theislab'
author_email = 'david.fischer@helmholtz-muenchen.de'
description = ""

with open("README.rst", "r") as fh:
     long_description = fh.read()

setup(
    name='sfaira_extension',
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'anndata>=0.7',
        'h5py',
        'numpy>=1.16.4',
        'pandas',
        'scipy>=1.2.1',
        'tqdm',
        'sfaira'
    ],
    extras_require={
        'tensorflow': [
            'tensorflow>=1.15.0',
            'tensorflow-gpu>=1.15.0'
        ],
        'kipoi': [
            'kipoi',
            'git-lfs'
        ],
        'plotting_deps': [
            "seaborn",
            "matplotlib",
            "sklearn"
        ],
        'scanpy': [
            "scanpy"
        ],
        'loompy': [
            "loompy",
        ],
        'docs': [
            'sphinx',
            'sphinx-autodoc-typehints',
            'sphinx_rtd_theme',
            'jinja2',
            'docutils',
        ],
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
