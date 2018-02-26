from setuptools import setup, find_packages

setup(name='NCP_OAuth',
      description="""This is for OAuth of NAVER Cloud Platform\thttps://github.com/ultimatelife/NCP_OAuth.git""",
      version='0.14',
      url='https://github.com/ultimatelife/NCP_OAuth.git',
      author='geonwoo.kim',
      keywords=['NCP', 'naver cloud platform', 'ncp-oauth', 'ncp'],
      author_email='drama0708@gmail.com',
      license='Naver Cloud Platform',
      python_requires='>=3.6',
      classifiers=[
          'Programming Language :: Python :: 3.6'
      ],
      packages=find_packages(),
      install_requires=[
          'requests>=2.17.3'
      ]
      )
