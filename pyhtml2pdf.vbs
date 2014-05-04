' 
' Ejemplo de Uso de Interfaz PyHTML2PDF para Windows Script Host
' 2014(C) Mariano Reingart <reingart@gmail.com>
' Licencia: GPLv3
'  Requerimientos: scripts pyhtml2pdf.py registrado
 
' Crear el objeto WSAA (Web Service de Autenticación y Autorización) AFIP
Set PyHTML2PDF = Wscript.CreateObject("PyHTML2PDF")
Wscript.Echo "Version", PyHTML2PDF.Version

scriptdir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
ok = PyHTML2PDF.Convertir(scriptdir & "\prueba.html", scriptdir & "\prueba.pdf")
Wscript.Echo "Excepcion", PyHTML2PDF.Excepcion
Wscript.Echo "Traceback", PyHTML2PDF.Traceback

If ok Then
    ok = PyHTML2PDF.Mostrar(scriptdir & "\prueba.pdf")
End If
