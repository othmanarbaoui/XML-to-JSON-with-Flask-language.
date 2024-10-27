from flask import Flask, render_template, request
import xmltodict
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Accueil.html')

@app.route('/transfer', methods=['POST'])
def transfer_text():
    xmlText = request.form.get('textarea1', '')
    try :
        xmlDic= xmltodict.parse(xmlText)
        jsonText = json.dumps(xmlDic , indent=2)
        return render_template('Accueil.html', xmlText=xmlText , jsonText =jsonText , erreur=None)
    except Exception as e :
        return render_template('Accueil.html', xmlText=xmlText , jsonText =str(e) , erreur ='erreur')

if __name__ == '__main__':
    app.run(debug=True )
