from setuptools import setup

setup(
    name='pybackend',
    version='0.1',
    packages=['pybackend'],
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'pybackend=pybackend.__main__:main',
        ],
    },
)
