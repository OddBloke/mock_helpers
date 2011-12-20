from distutils.core import setup


setup(
    name='mock_helpers',
    version='0.1.1',
    author='Daniel Watkins',
    author_email='daniel@daniel-watkins.co.uk',
    url='http://pypi.python.org/pypi/mock_helpers',
    description='A number of helpers for use with python-mock.',
    packages=['mock_helpers'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Testing",
    ],
    requires=['mock'],
)
