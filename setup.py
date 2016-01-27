from distutils.core import setup

setup(
    name='SextractorTools',
    version='1.0',
    packages=[''],
    url='',
    license='BSD',
    author='Matt Mechtley',
    author_email='',
    description='Python tools for manipulating Sextractor source catalogs',
    scripts=['scripts/sexcat_to_ds9'],
    requires=['numpy', 'astropy']
)
