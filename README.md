# TaskScript

	Copyright © 2016  Gabriel Agustín Véntola.
	
	**TaskScript is a program that generates a todo list from the comments
	on you source files.**

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
	

## Qué es?? ##
** TaskScript, es un programa que genera una lista de "pendientes" según los comentarios de tus archivos fuente. **

## Por qué existe??##
Es una funcionalidad disponible en muchos IDE y editores avanzados que, por alguna razón, no tenía mi editor favorito.
Muchos dirán que "por qué no uso Sublime Text??".. Yo les diré que vayan a c*gar..
Vi la oportunidad de hacerlo y lo hice en mi tiempo libre. Ahora te lo comparto, usalo si te va.
	
## Requisitos para instalarle: ##
- Notepad++ instalado (obviamente).
- Pythonscript instalado (version 0.9.2.0).
	
## Pasos para instalarle: #
1. Descargá el programa desde https://github.com/tutoGav/TaskScript.
2. Colocá el archivo TaskScript.py en la carpeta /Users/[tu usuario]/AppData/Roaming/Notepad++/plugins/config/PythonScript/scripts/TaskScript.
3. Abrí Notepad++ y agregá el script desde Plugins>Python Script>Configuration.

## Cómo se usa?? ##
Antes que nada, una aclaración: el coso este funciona en base a
"archivos de ubicación". Si sabés lo que son, no hay nada que leer;
sino, seguí leyendo cual es la onda.

1. Andá a Vista>Proyecto>Panel proyecto 1.
2. En el panel, click secundario sobre "ubicación" y "añadir proyecto".
3. Dale un nombre.
4. Click dere.. secundario y "Añadir Archivos ...", "Añadir carpeta" o "Añadir archivos de la carpeta". (ya ves de qué va??).
5. Guardá el archivo de ubicación (click secundario, etc).
6. Cuando tengas todo agregado, y empieces a editar tus fuentes, empezá tus comentarios con "HACER:". (fácil, no??).
7. Guardá todo lo que modificaste y corré el script desde Plugins>Python Script>Scripts>TaskScript (o desde el botón de las viborillas, es más cómodo).
8. Van a aparecer dos ventanas que te van a pedir cosas (ya te vas a dar cuenta qué).
9. IMPORTANTE: a partir de ahí, tu NP++ va a parecer poseído por un bicho, no te asustes, es normal. (Dije que esto no tiene garantía, no??).
10. "Automágicamente" se va a crear la dichosa listita de pendientes.
11. Mandame guita.

## Otra aclaración: ##
Lo hago en mi tiempo libre, el que tengo poco, por estudiar Ingeniería en Sistemas.
Adónde voy con esto??
La idea es que lo pruebes y me avises si tiene un error, que voy a corregir cuando pueda y quiera (casi siempre quiero). Así que no te me rompas las b*las si no lo hago.
Tengo pensada algunas funcionalidades para hacerlo más útil al programa y menos restrictivo con lo de los "archivos de ubicación" (fue una buena restricción de inicio para
empezar rápido; y, además te obligo a que trabajes ordenado no dejes fuentes desparramadas por tu computadora), pero me acordé que tenía rendir y hacer otras cosas, por eso lo dejo así. En algún momento se las voy a agregar