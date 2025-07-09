from setuptools import setup, find_packages

setup(
    name='cliper',
    version='0.0.1',
    description='a clipboard history tool',
    author='Omar Arabi',
    packages=find_packages(),
    entry_points={
        'console_scripts':
            ['cliper = cliper.main:main']
    }
)