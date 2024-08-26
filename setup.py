from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='poker-h',
  version='1.0.2',
  author='Gimer',
  author_email='bashinsky04@gmail.com',
  description='This is a library that will help you create a poker game.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/windgim',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='poker pokerh poker-h holdem texas game ',
  project_urls={
    'GitHub': 'https://github.com/windgim'
  },
  python_requires='>=3.6'
)