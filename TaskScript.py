"""
5 tareas encontradas en los siguientes archivos:

Proyecto: Prueba. Tareas: 5
	TaskScript, es un programa que genera una lista de "pendientes"
	según los comentarios de los archivos fuentes.
    Copyright © 2016  Gabriel Agustín Véntola

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Gabriel Véntola"
__copyright__ = "Copyright 2016, TaskScript, Gabriel Véntola"
__credits__ = "Félix Barros"
__license__ = "GPL"
__version__ = "1.0 (beta)"
__maintainer__ = "Gabriel Véntola"

import xml.etree.ElementTree as ET
import os.path
from numbers import Number
script = "TaskScript"

# ----------------------------------- subacciones ------------------------------------
def obtenerProyecto():

	def obtenerPath(msj):
		ruta = notepad.prompt(msj, script + ' ' + __version__).replace('\\', '/')
		if ruta:
			if not os.path.exists(ruta):
				return obtenerPath('Metele de vuelta, porque nada que ver lo que pusiste')
		return ruta
		
	def obtenerArch(ruta):
		pro = notepad.prompt("Poné el nombre del archivo de ubicación".decode('utf8').encode('latin1'), script + ' ' + __version__)
		if pro:
			try:
				return ET.parse(ruta + '/' + pro).getroot()
			except IOError:
				return notepad.messageBox('El archivo no existe, la dirección está mal o metiste cualquier cosa. Querés probar de vuelta??'.decode('utf8').encode('latin1'), 'HICISTE CAGADA!!', 53)
	
	path = obtenerPath("Poné la dirección del proyecto".decode('utf8').encode('latin1'))
	pro = obtenerArch(path)
	
	if pro == 4:
		return obtenerProyecto()
	return path, pro

def crearLista(path):
	import glob
	import datetime
	import locale
	os.chdir(path)
	
	for nodo in notepad.getFiles():
		if 'Tareas' in nodo[0]:
			notepad.activateFile(nodo[0])
			notepad.close()
	for file in glob.glob("Tareas*.*"):
		os.remove(file)
	
	notepad.new()
	locale.setlocale(locale.LC_ALL, "esp")
	editor.addText('Lista de tareas emitida a las ' + datetime.datetime.now().strftime('%H:%M:%S hs del %d de %B, de %Y \r\n'))
	notepad.saveAs(path + '/Tareas.txt')
	return notepad.getCurrentFilename()

def esFuente(arch):
	if not arch:
		return False
	extensiones = {"ini", "inf", "h", "hh", "hpp", "hxx", "c", "cpp", "cxx", "cc", "m", "mm", "vcxproj", "vcproj", "props", "vsprops", "manifest", "java", "cs", "pas", "pp", "inc", "html", "htm", "shtml", "shtm", "hta", "asp", "aspx", "css", "js", "json", "jsm", "jsp", "php", "php3", "php4", "php5", "phps", "phpt", "phtml", "xml", "xhtml", "xht", "xul", "kml", "xaml", "xsml", "sh", "bsh", "bash", "bat", "cmd", "nsi", "nsh", "lua", "pl", "pm", "py", "rc", "as", "mx", "vb", "vbs", "f", "for", "f90", "f95", "f2k", "sql", "nfo", "mak"}
	nombre, ext = arch.split(".")
	if ext in extensiones:
		return True
	else:
		return False

def buscarFuente(nodo):
	archivo = nodo.get("name").replace('\\','/')
	
	if esFuente(archivo):
		if nodo.get("name").find(":") <> -1 :
			cosa = archivo
		else:
			cosa = path + "/" + archivo
		notepad.open(cosa)
		return cosa.lower()
	else:
		return ''

def buscarTareas(arch):
	tareas = []
	if esFuente(arch):
		notepad.activateFile(arch)
		editor.documentStart()
		editor.searchAnchor()
		while editor.searchNext(0, 'HACER:') <> -1:
			linea = editor.lineFromPosition(editor.getCurrentPos())
			tareas.append(editor.getLine(linea))
			linea += 1
			editor.gotoLine(linea)
			editor.searchAnchor()
		notepad.close()
	return tareas
	
def modifLista(lista, archLista, fuente):
	i = 1
	
	notepad.activateFile(archLista)
	# agrego archivo fuente
	editor.documentEnd()
	editor.newLine()
	editor.delLineLeft()
	editor.tab()
	editor.addText(fuente)
	
	editor.newLine()
	# agrego primer linea (cuestiones estéticas)
	editor.addText(tareas[0])
	editor.gotoPos(editor.getLineIndentPosition(editor.lineFromPosition(editor.getCurrentPos() - 1)))
	editor.delWordLeft()
	editor.newLine()
	editor.tab()
	editor.addText(str(i).zfill(2) + ' ')
	editor.documentEnd()
	editor.newLine()
	tareas.pop(0)
	i += 1
		
	for nodo in tareas:
		editor.addText(nodo)
		editor.gotoPos(editor.getLineIndentPosition(editor.lineFromPosition(editor.getCurrentPos() - 1)))
		editor.delWordLeft()
		editor.newLine()
		editor.addText(str(i).zfill(2) + ' ')
		editor.documentEnd()
		i += 1
	del tareas[:]

	editor.delLineRight()
	return i - 1

# HACER: terminar el callback
def ir(args):
	if 'Tareas.txt' in notepad.getCurrentFilename():
		com = ''
		if (not ':/' in editor.getCurLine()) and (not ':\\' in editor.getCurLine()):
			com = editor.getCurLine()[5:-2]
			num = int(editor.getCurLine()[2:4])
			editor.gotoLine(editor.lineFromPosition(editor.getCurrentPos()) - num)
		ar = editor.getCurLine()[1:-2]
		notepad.open(ar)
		console.write(com)
		editor.searchNext(0, com)

def hint(args):
	editor.callTipShow(450, 'Doble click y te vas allá')
	editor.callTipSetHlt(0, 11)

def esconder(args):
	editor.callTipCancel()

# ---------------------------------- fin subacciones --------------------------------
console.clear()
console.write(script + ' Copyright © 2016  Gabriel Agustín Véntola\r\n' + 
    'This program comes with ABSOLUTELY NO WARRANTY; for details go to "LICENSE"' +
	'or the "README.md" file.\r\n' + 'This is LIBRE software, and you are welcome ' +
	'to redistribute it under certain conditions detailed en the "LICENSE" file.\r\n\r\n' +
	'Este programa viene SIN GARANTÍA ALGUNA, lo usás BAJO TU PROPIO RIESGO; ' +
	'para más detalles, leé el archivo "README.md" o el "LICENSE".\r\n' +
	'Esto es software LIBRE, y podés redistribuirlo bajo las condiciones detalladas' +
	'en el archivo "LICENCE".\r\n')
	
a = 0
path, raiz = obtenerProyecto()
# if not isinstance(raiz, Number):
if path:
	lista = crearLista(path)
	for node in raiz.iter("Project"):
		linea = editor.lineFromPosition(editor.getCurrentPos())
		b = 0
		for nodo in node.iter("File"):
			fuente = buscarFuente(nodo)
			tareas = buscarTareas(fuente)
			if tareas:
				a += modifLista(tareas, lista, fuente)
		if b <> a:
			b = a
			editor.gotoLine(linea)
			editor.newLine()
			editor.delLineLeft()
			editor.addText('Proyecto: ' + node.get("name") + '. Tareas: ' + str(b))
			editor.newLine()
			editor.documentEnd()
	editor.gotoLine(1)
	editor.addText(str(a) + ' tareas encontradas en los siguientes archivos:\r\n')
	editor.documentEnd()
	notepad.save()
	editor.setMouseDwellTime(1500)
	# editor.callTipShow(450, 'Doble click y te vas ahí')
	# editor.callTipSetHlt(0, 11)
console.write('Opáma programa!!')
editor.callback(ir, [SCINTILLANOTIFICATION.DOUBLECLICK])
editor.callback(hint, [SCINTILLANOTIFICATION.DWELLSTART])
editor.callback(esconder,[SCINTILLANOTIFICATION.DWELLEND])