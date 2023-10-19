from flask import Flask, redirect, url_for, request, render_template
import dbman
app = Flask(__name__)
 
 
 
@app.route('/', methods=['POST', 'GET'])
def main():
        print('hi')
        return render_template('main.html')
       # return 'hi'
 
@app.route('/signup', methods=['POST', 'GET'])
def oth():
        if request.method == 'POST':
                name = request.form['nm']
                password = request.form['ps']
                dbman.newuser(name, password)
                print('done')
                return render_template('main.html')
        else:
               print('not made')
               return render_template('signup.html')
        
@app.route('/login', methods=['POST', 'GET'])
def log():
        if request.method == 'POST':
                name = request.form['nm']
                password = request.form['ps']
                dec = dbman.getuser(name, password)
                if dec == 'allgood':
                        print("good")
                        return render_template('main.html', name=name)
                if dec == 'inpass':
                        print('not made')
                        return render_template('main.html', name='incorrect password')
                
                if dec == 'wrongname':
                       return render_template('main.html', name='incorrect name')
        return render_template('login.html')
               
        



if __name__ == '__main__':
    app.run(debug=True, port=5001)