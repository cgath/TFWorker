from setuptools import setup

setup(name='worker-tf',
      version='0.1.0',
      packages=['worker'],
      entry_points={
          'console_scripts': [
              'worker = worker.__main__:main'
          ]
      },
      )
