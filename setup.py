from setuptools import setup, find_packages

setup(name='redfish',
      version='1.0.0',
      description='Redsfish Python Library',
	  author = 'DMTF',
	  author_email = 'DMTF@DMTF.com',
	  license='BSD 3-clause "New" or "Revised License"',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Communications'
      ],
      keywords='Redfish',
      url='https://github.com/DMTF/python-redfish-library',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=[
          'jsonpatch',
          'jsonpath_rw',
          'jsonpointer',
          'urlparse2',
      ])
