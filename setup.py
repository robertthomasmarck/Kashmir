from setuptools import setup, find_packages

setup(
    name='kashmir',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'kashmir = kashmir:cli',
        ],
    },
)