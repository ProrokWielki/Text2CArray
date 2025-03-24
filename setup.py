from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(name='Text2CArray',
      version='0.1.0',
      description='Script for generating C arrays from text.',
	    long_description=long_description,
	    long_description_content_type='text/markdown',  # This is important!
      url='https://github.com/ProrokWielki/Text2CArray',
      author='Pawel Warzecha',
      author_email='pawel.warzecha@yahoo.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'pyyaml',
          'numpy',
          'setuptools-git',
          'gitpython',
          'Pillow'
          ],
      zip_safe=False)
