from setuptools import setup


setup(
    name='avenyn-lunch',
    version='1.4',
    author='ianertson',
    author_email='ianertson@gmail.com',
    install_requires=[
        'requests',
        'bs4'
    ],
    packages=[
        'avenyn_lunch'
    ],
    entry_points={
        'console_scripts': [
            'avenyn-lunch = avenyn_lunch.bin:run'
        ]
    }
)
