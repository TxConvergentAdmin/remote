from setuptools import setup


setup(
    name='convergent-remote',
    version='0.0.3',
    description='A remote.',
    url='https://github.com/TxConvergentAdmin/remote',
    author='Shrivu Shankar',
    license='MIT',
    packages=['remote'],
    entry_points = {'console_scripts': ['start-remote=remote.run:main']},
    include_package_data=True
)