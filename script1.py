from flask import Flask
from flask import render_template #Return a HTML template. It acesses an HTML file stored somewhere in the application. And display the HTML on the requested URL.

app = Flask(__name__) #Store flask application

@app.route('/')#Decorator, the URL. Home page
def home(): #Define what the web page do
    #return "Home page is here."
    return render_template("home.html")#Return to a HTML file which has stored in a local folder.

@app.route('/about/')#Decorator, the URL. Second page
def about(): #Define what the web page do
    #return "This is 'about' page"
    return render_template("about.html")

if __name__ == "__main__" :
    app.run(debug = True)