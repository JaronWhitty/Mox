
from setuptools import setup
setup(name='mox_events',
      version='1.0',
      description='Find time and magnitude of mox events',
      long_description='',
      author='Jaron C Whittington',
      author_email='jaronwhitty@gmail.com',
      url='https://github.com/JaronWhitty/Mox',
      license='MIT',
      setup_requires=['pytest-runner',],
      tests_require=['pytest', 'python-coveralls', 'coverage'],
      install_requires=[
          "pandas",
          "numpy",
          "scipy"
      ],
      packages = ['find_mox_events'],
      include_package_data=True,
      scripts=['find_mox_events/find_mox_events.py'],
              
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Other Audience',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ],
)
