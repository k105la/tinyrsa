import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()



setup(name='tinyrsa',
      version='0.0.1',
      description='A tiny library for doing simple RSA encryption/decryption',
      author='Akil Hylton',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages = ['tinyrsa'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['gmpy2, numpy'],
      python_requires='>=3.8',
      include_package_data=True)
