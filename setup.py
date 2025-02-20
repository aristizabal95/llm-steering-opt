from setuptools import setup

setup(
   name='steering_opt',
   version='0.1',
   description='A library for optimizing steering vectors in LLMs.',
   author='Jacob Dunefsky',
   author_email='jacob.dunefsky@yale.edu',
   packages=['steering_opt'],  #same as name
   install_requires=['mdmm', 'numpy', 'torch']
)