from setuptools import setup


setup(
    name='convergent-remote',
    version='0.0.0',
    description='A remote',
    url='https://github.com/TxConvergentAdmin/remote',
    author='Shrivu Shankar',
    license='MIT',
    packages=['remote'],
    entry_points = {'console_scripts': ['cvgt-remote=remote.start:main']}
)