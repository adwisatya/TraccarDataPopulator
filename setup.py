from distutils.core import setup, Extension
import subprocess
subprocess.run(["pandoc","--from=markdown","--to=rst","--output=README","README.md"])

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'TraccarDataPopulator',
  packages = ['TraccarDataPopulator'],
  version = '0.2',
  license='MIT',
  description = 'This library used for populating data for traccar server in order to speedup development process or troubleshooting a traccar server',
  long_description=long_description,
  author = 'Aryya Widigdha',
  author_email = 'aryya.widigdha@yahoo.com',
  url = 'https://github.com/adwisatya/TraccarDataPopulator',
  download_url = 'https://github.com/adwisatya/TraccarDataPopulator/archive/refs/tags/v0.1.tar.gz',
  keywords = ['traccar', 'osmand', 'traccar data populator'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
