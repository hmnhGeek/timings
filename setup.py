from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='timings',
      version='1.1',
      description='Convert time from seconds.',
      author='Himanshu Sharma',
      license='MIT',
      packages=['timings'],

      include_package_data=True,
      zip_safe=False,
      entry_points = {
        'console_scripts': ['timings-run=timings.command_line:main']})
