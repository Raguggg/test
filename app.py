from unicodedata import name
from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('form.html')
    pass
# @app.route('/sub',methods=['POST'])
# def subb():
#         n = request.form('roll')
#         return render_template('endfile.html',rrr=n)

@app.route('/', methods =["POST"])
def gfg():
    name = request.form['name']
    f_name = request.form['f-name']
    m_name = request.form['m-name']
    dob = request.form['dob']
    email = request.form['email']
    number = request.form['number']
    address = request.form['address']
    state = request.form['state']
    city = request.form['city']
    gender = request.form['gender']
    return render_template('endfile.html' , 
                        name=name,
                        f_name=f_name,
                        m_name=m_name,
                        dob=dob,
                        email=email,
                        number=number,
                        address=address,
                        state=state,
                        city=city,
                        gender=gender
                        
                        
                        
                         )






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)