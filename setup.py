from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.1.0'
DESCRIPTION = 'The Colombian Index Tool (Market Rate Exchange) package downloads the Colombian Market Rate from the source: Portal de Datos Abiertos <www.datos.gov.co>, for direct use in Python.'
PACKAGE_NAME = 'cITMre'
AUTHOR = ['Sergio Andrés Sierra Luján', 'David Esteban Rodríguez Guevara']
EMAIL = ['sergiochess95@gmail.com', 'davestss@hotmail.com']
GITHUB_URL = 'https://github.com/SergioFinances/citmre_development_python.git'
MAINTAINERS = [
    {'name': 'David Esteban Rodríguez Guevara', 'email': 'davestss@hotmail.com'}
]

setup(
    name = 'cITMre',
    packages = ['citmre'],
    version = '0.1.1',
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = ['finances', 'econometric', 'stochastic processes'],
    install_requires=[ 
        'requests',
        'pandas',
        'numpy',
        'plotly'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    maintainers=MAINTAINERS
)