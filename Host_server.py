from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/main/', methods=['GET', 'POST'])
def main():
    try:
        f=open('data.txt','x')
        f.close()
    except:
        pass
    if request.method == 'GET':
        username = request.form.get('username')
        data=open('datalog.txt','r').read()
        if data is None:
            data="nothing"
        return f'{username}:{data}'
    if request.method == 'POST':
        data = request.form.get('data')
        username = request.form.get('username')
        f=open('datalog.txt','a')
        f.write(username+":"+data+"\n")
        f.close()
        return (f'{username}:{data}')

app.run('0.0.0.0',debug=True)
