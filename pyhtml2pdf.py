#!/usr/bin/python
# -*- coding: latin-1 -*-
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

"Módulo para convertir html a pdf"

__author__ = "Mariano Reingart <reingart@gmail.com>"
__copyright__ = "Copyright (C) 2014 Mariano Reingart"
__license__ = "GPL 3.0"
__version__ = "1.01a"

import os
import sys
import traceback
from xhtml2pdf import pisa


class PyHTML2PDF:
    "Interfaz para convertir HTML a PDF"
    _public_methods_ = ['Convertir', 'Mostrar',
                        ]
    _public_attrs_ = ['Version', 'Excepcion', 'Traceback']
        
    _reg_progid_ = "PyHTML2PDF"
    _reg_clsid_ = "{D3A46EBE-5D35-43AF-8AFA-ABC3B4D0EB3E}"


    def __init__(self):
        self.Version = __version__
        self.Exception = self.Traceback = ""
            
    def Convertir(self, html, pdf):
        "Convertir un archivo html a pdf"

        try:
       
            # abrir y leer archivo de origen (html)
            source = open(html, "r+b").read()

            # abrir archivo destino (pdf)
            target = open(pdf, "w+b")
            
            # convertir:
            status = pisa.CreatePDF(source, dest=target)
            
            target.close()
            self.Excepcion = status.err
            
            return True
        
        except Exception, e:
            raise
            ex = traceback.format_exception( sys.exc_type, sys.exc_value, sys.exc_traceback)
            self.Traceback = ''.join(ex)
            self.Excepcion = traceback.format_exception_only( sys.exc_type, sys.exc_value)[0]
            return False


    def Mostrar(self, pdf):
        "Arbir un pdf"
        if sys.platform=="linux2":
            os.system("evince ""%s""" % pdf)
        else:
            os.startfile(pdf)

            
if __name__ == '__main__':

    if "--register" in sys.argv or "--unregister" in sys.argv:
        import win32com.server.register
        win32com.server.register.UseCommandLine(PyHTML2PDF)
    else:
        
        pyhtml2pdf = PyHTML2PDF()

        archivo_html = sys.argv[1]
        archivo_pdf = sys.argv[2]
        
        ok = pyhtml2pdf.Convertir(archivo_html, archivo_pdf)

        print "Ok:", ok
        print "Excepcion", pyhtml2pdf.Excepcion            

        if not ok or not '--mostrar' in sys.argv:
            pass
        else:
            pyhtml2pdf.Mostrar(archivo_pdf)
