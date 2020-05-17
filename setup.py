from setuptools import setup

setup(
  name='Bird LG Proxy',
  version='1.0',
  packages=['bird_lgproxy'],
  entry_points = {
    'console_scripts': ['bird-lgproxy=bird_lgproxy.lgproxy:main']
  },
  install_requires = [
    'flask',
  ],
)
