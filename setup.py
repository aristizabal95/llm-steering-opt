from setuptools import setup, find_packages

setup(
   name='steering_opt',
   version='0.1',
   description='A library for optimizing steering vectors in LLMs.',
   author='Jacob Dunefsky',
   author_email='jacob.dunefsky@yale.edu',
   packages=find_packages(),
   install_requires=[
       'mdmm==0.1.3',
       'numpy==2.2.3', 
       'torch==2.3.1',
       'transformers==4.45.2'
   ]
)
