from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.2.0'

install_requires = [
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    # No dependances yet
]


setup(name='setr',
    version=version,
    description="Search for ExtraTerrestrial Ranges",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: W3C License",
        "License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2"
    ],
    keywords='Ranges, Speed',
    author='Zach Aysan',
    author_email='zachaysan@gmail.com',
    url='https://github.com/zachaysan/setr',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['setr=setr:main']
    }
)
