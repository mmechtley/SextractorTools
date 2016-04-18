from numpy import append
from astropy.io import fits, ascii


def _read_ascii_head(catfile, keep_cols=None):
    table = ascii.read(catfile, format='sextractor')
    if keep_cols is not None:
        table = table[keep_cols]
    return table


def _read_fits_ldac(catfile, keep_cols=None):
    catalog = None
    fd = fits.open(catfile)
    for hdu in fd[1:]:
        if hdu.header['EXTNAME'] == 'LDAC_OBJECTS':
            if catalog is None:
                catalog = hdu.data
            else:
                catalog = append(catalog, hdu.data)
    fd.close()
    if catalog is None:
        raise ValueError('No LDAC_OBJECTS extensions found')

    if keep_cols is not None:
        return catalog[keep_cols]
    else:
        return catalog


def read_catalog(catfile, keep_cols=None):
    """
    Read in a sextractor catalog and return as numpy record array.
    Supported formats: ASCII_HEAD, FITS_LDAC
    Unsupported: ASCII, ASCII_SKYCAT, ASCII_VOTABLE, FITS_1.0

    :param catfile: Filename of the catalog to open
    :param keep_cols: List of columns to keep, either list of names or list of
                      column numbers (0=first column)
    :return: Catalog data as numpy structured array (numpy.recarray)
    """
    # Try each catalog type in turn
    cat = None
    for read_func in (_read_ascii_head, _read_fits_ldac):
        try:
            cat = read_func(catfile, keep_cols=keep_cols)
            break
        except ValueError:
            pass
    if cat is None:
        raise ValueError('Catalog in unknown format {}'.format(catfile))

    return cat