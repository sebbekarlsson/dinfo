from setuptools import setup


setup(
    name='dinfo',
    version='1.0',
    install_requires=[
        ''
    ],
    packages=[
        'dinfo'
    ],
    entry_points={
        'console_scripts': [
            'dinfo = dinfo.bin:run'
        ]
    }
)
