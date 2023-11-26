from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()
    
setup(name='vesocket',
      version='0.0',
      description='Victron VE.Direct socket decoder for Python',
      url='https://github.com/r09491/vesocket',
      author='r09491',
      author_email='r09491@gmail.com',
      license='MIT',
      long_description=long_description,
      packages=['vesocket'],
      install_requires=[
      ],
      zip_safe=False)
