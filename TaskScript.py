import xml.etree.ElementTree as ET
import os.path
from numbers import Number
script = "Tuto's taskScript v1 Beta"

# ----------------------------------- subacciones ------------------------------------
def obtenerProyecto():

	def obtenerPath(msj):
		ruta = notepad.prompt(msj, script)
		if ruta:
			if not os.path.exists(ruta):
				return obtenerPath('Metele de vuelta, porque nada que ver lo que pusiste')
		return ruta
		
	def obtenerArch(ruta):
		pro = notepad.prompt("Poné el nombre del archivo de ubicación".decode('utf8').encode('latin1'), script)
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
	editor.addText(str(i).zfill(2))
	editor.documentEnd()
	editor.newLine()
	tareas.pop(0)
	i += 1
		
	for nodo in tareas:
		editor.addText(nodo)
		editor.gotoPos(editor.getLineIndentPosition(editor.lineFromPosition(editor.getCurrentPos() - 1)))
		editor.delWordLeft()
		editor.newLine()
		editor.addText(str(i).zfill(2))
		editor.documentEnd()
		i += 1
	del tareas[:]

	editor.delLineRight()
	return i - 1
	
# ---------------------------------- fin subacciones --------------------------------
console.clear()
console.write(script + ', reservados todos los derechos\r\n')
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
console.write('Opáma programa!!')