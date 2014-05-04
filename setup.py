from distutils.core import setup
from nsis import build_installer, Target
import py2exe

import pyhtml2pdf

setup( 
    name="PyHTML2PDF",
    version=pyhtml2pdf.__version__,
    description="Interfaz PyHTML2PDF %s",
    long_description=pyhtml2pdf.__doc__,
    author="Mariano Reingart",
    author_email="reingart@gmail.com",
    url="http://www.sistemasagiles.com.ar",
    license="GNU GPL v3",
    com_server = [Target(module=pyhtml2pdf, modules='pyhtml2pdf', create_exe=True, create_dll=True)],
    console=[Target(module=pyhtml2pdf, script="pyhtml2pdf.py", dest_base="pyhtml2pdf-cli")],
    #zipfile=None,
    options={ 
        'py2exe': {
        'includes': [],
        'optimize': 0,
        'bundle_files': 3,
        'includes': ['reportlab.rl_config', ], # TODO: fix reportlab, html5lib packaging
        'excludes': ["pywin", "pywin.dialogs", "pywin.dialogs.list", "win32ui","distutils.core","py2exe","nsis"],
        'skip_archive': True,
    }},
    data_files = [(".", ["licencia.txt", "prueba.html"]),],
    #cmdclass = {"py2exe": build_installer}
)
