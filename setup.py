from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()
    
setup(name='veplug',
      version='0.1',
      description='Victron VE.Direct decoder for Python',
      url='https://github.com/r09491/vesocket',
      author='r09491',
      author_email='r09491@gmail.com',
      license='MIT',
      long_description=long_description,
      packages=['veplug', 'veconverters'],
      install_requires=[
      ],
      zip_safe=False)
