__all__ = ['processing','processing.compute_subswath_xspectra', 'compute_subswath_intraburst_xspectra',
           'compute_subswath_interburst_xspectra']
try:
    from importlib import metadata
except ImportError: # for Python<3.8
    import importlib_metadata as metadata
__version__ = metadata.version('xsarslc')