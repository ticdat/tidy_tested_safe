import tts_diet
from setuptools import setup, find_packages

setup(
   name = 'self_serve_ticdat',
   packages = find_packages(),
   version = tts_diet.__version__,
   author = 'Pete Cacioppi',
   author_email= 'peter.cacioppi@gmail.com',
   url = 'https://github.com/ticdat/tidy_tested_safe/tree/master/tts_diet',
   platforms = 'any',
)