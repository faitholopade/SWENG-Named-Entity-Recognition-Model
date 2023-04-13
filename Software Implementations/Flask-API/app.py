from flask import Flask,render_template,request
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_trf')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
    if request.method == 'POST':
        choice = request.form['taskoption']
        rawtext = request.form['rawtext']
        doc = nlp(rawtext)
        d = []
        for ent in doc.ents:
            d.append((ent.label_, ent.text))
            df = pd.DataFrame(d, columns=('named entity', 'output'))
            org_named_entity = df.loc[df['named entity'] == 'ORG']['output']
            person_named_entity = df.loc[df['named entity'] == 'PERSON']['output']
            gpe_named_entity = df.loc[df['named entity'] == 'GPE']['output']
            money_named_entity = df.loc[df['named entity'] == 'MONEY']['output']
        if choice == 'organization':
            results = org_named_entity
            num_of_results = len(results)
        elif choice == 'person':
            results = person_named_entity
            num_of_results = len(results)
        elif choice == 'geopolitical':
            results = gpe_named_entity
            num_of_results = len(results)
        elif choice == 'money':
            results = money_named_entity
            num_of_results = len(results)


    return render_template("index.html",results=results,num_of_results = num_of_results)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
