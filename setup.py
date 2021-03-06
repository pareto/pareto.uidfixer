from setuptools import setup, find_packages
import os

version = '0.7'

setup(name='pareto.uidfixer',
      version=version,
      description="Find relative hrefs in HTML fields, and replace then with resolveuid ones.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pareto'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pareto.plonehtml',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
