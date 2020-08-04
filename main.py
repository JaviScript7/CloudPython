#Importación de librerias para trabajars
import os
from os import remove
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template

#Declaracion  de variable que hace referencia a la carpeta contenedora para alojar los archivos
FILE_CONTAINER = './cont/'

app = Flask(__name__, template_folder='templates')
app.debug = True
app.config['FILE_CONTAINER'] = FILE_CONTAINER

#Hace referencia al index de nuestra página  
@app.route('/')
def mostrar_cont():
    dir = FILE_CONTAINER
    with os.scandir(dir) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
    return render_template('index.html',ficheros=ficheros)
    
#Funcion para subir archivos 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
       #Comprobar si la solicitud de publicación tiene la parte del archivo
        if 'file' not in request.files:
            print('No se cargo ningun archivo')
            return redirect(request.url)
        file = request.files['file']
        #Si el usuario no selecciona un archivo
        if file.filename == '':
            print('No se cargo ningun archivo')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['FILE_CONTAINER'], filename))
            print("Archivo guardado con exito")
            #Se redirecciona a la pagina principal
            return redirect('/')

#Función para la eliminacion de archivos 
@app.route('/removefile/<filename>')
def remove_file(filename):
    file_path = FILE_CONTAINER + filename
    remove(file_path)
    print("Archivo eliminado con exito")
    return redirect('/')

#Funcion para la descarga de archivos
@app.route('/download_file/<filename>')
def return_files_tut(filename):
    file_path = FILE_CONTAINER + filename
    print(file_path)
    return send_file(file_path, as_attachment=True, attachment_filename='')

if __name__ == "__main__":
    app.run(host='192.168.0.114')
