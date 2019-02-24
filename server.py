from flask import (flask, render_template)

#create the application instance
app = flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')

def home():
	"""
	This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
	return render_template('home.html')

#If we're running in stand alone mode, run de application
if __name__ == '__main__':
	app.run(debug=True)