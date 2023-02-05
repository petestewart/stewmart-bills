from setuptools import find_packages, setup

setup(
    name='stewmart-email-checker',
    description='checks emails and parses for bills',
    author='Pete Stewart',
    author_email='petestew@gmail.com',
    verison='0.0.1',
    packages=find_packages(exclude=['tests*']),
    entry_points={
        'console_scripts': [
            'stewart_email_checker=stewart_email_checker.cli:main'
        ]
    }
)