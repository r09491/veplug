from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()
    
setup(name='victron_plug',
      version='0.1',
      description='Victron serial VE.Direct decoder',
      url='https://github.com/r09491/vesocket',
      author='r09491',
      author_email='r09491@gmail.com',
      license='MIT',
      long_description=long_description,
      packages=['victron_plug', 'victron_converters'],
      install_requires=[
      ],
      zip_safe=False)
