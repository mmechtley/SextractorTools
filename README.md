SextractorTools
===============

Module for manipulating Sextractor source catalogs. Currently supports opening 
ASCII-Head and FITS-LDAC catalogs, returning a FITS/astropy Table object

sexcat_to_ds9 script
--------------------
The module also includes a command line script to create an SAOImage ds9 region 
file from a Sextractor source catalog.

Future Improvements
-------------------
- Better documentation and options for sexcat_to_ds9 script
- Wrapping the sextractor command-line binary, optionally supplying command 
  line options
- Manipulation of Sextractor configuration files
