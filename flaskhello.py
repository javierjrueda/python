from flask import Flask

app = Flask(__name__)

@app.route("/")
def saludo():
	return "Mi primer programa flask"

@app.route('/articulos/')
def articulos():
	return "Estos son los articulos"
	
@app.route('/acercade')
def acercade():
	return "Acerca de este sitio"

@app.route('/articulos/<numero>')
def mostrar_articulos(numero):
	return('<h1>Este es el artículo nº: {}</h1>'.format(numero))

@app.route('/<usuario>')
def ruta_dinamica(usuario):
    return('<p>Hola, {}.</p>'.format(usuario))


if __name__ == "__main__":
  app.run()