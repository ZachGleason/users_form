from flask import Flask, render_template, request, redirect
app = Flask(__name__)   
from user import User                  
    
@app.route('/new')                           
def index():
    return render_template('index.html')  

@app.route('/results')                           
def success():
    users = User.get_all()
    return render_template('results.html', users = users)  

@app.route('/process', methods=["POST"])
def process():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
    }
    User.save(data)
    return redirect('/results')

if __name__=="__main__":
    app.run(debug=True)  