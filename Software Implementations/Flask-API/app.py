from flask import Flask,render_template,request
import pandas as pd
import spacy
from spacy import displacy
import en_core_web_trf
from flaskext.markdown import Markdown
nlp = spacy.load('../Spacy/output_cpu_kenneth/model-best')

app = Flask(__name__)
Markdown(app)

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""

@app.route('/')
def index():
	return render_template("index.html", num_of_results = 0, displacy_text="")

@app.route('/process',methods=["POST"])
def process():
	if request.method == 'POST':
		choice = request.form['taskoption']
		rawtext = request.form['rawtext']
		doc = nlp(rawtext)
		d = []
		displacy_text = ""
		for ent in doc.ents:
			d.append((ent.label_, ent.text))
			df = pd.DataFrame(d, columns=('named entity', 'output'))
			ORG_named_entity = df.loc[df['named entity'] == 'ORG']['output']
			PERSON_named_entity = df.loc[df['named entity'] == 'PERSON']['output']
			GPE_named_entity = df.loc[df['named entity'] == 'GPE']['output']
			MONEY_named_entity = df.loc[df['named entity'] == 'MONEY']['output']
			CARDINAL_named_entity = df.loc[df['named entity'] == 'CARDINAL']['output']
			DATE_named_entity = df.loc[df['named entity'] == 'DATE']['output']
			TIME_named_entity = df.loc[df['named entity'] == 'TIME']['output']
			PRODUCT_named_entity = df.loc[df['named entity'] == 'PRODUCT']['output']
			TECH_ISSUE_named_entity = df.loc[df['named entity'] == 'TECH_ISSUE']['output']
			NON_TECH_ISSUE_named_entity = df.loc[df['named entity'] == 'NON_TECH_ISSUE']['output']
			TECH_RESOLUTION_named_entity = df.loc[df['named entity'] == 'TECH_RESOLUTION']['output']
			NON_TECH_RESOLUTION_named_entity = df.loc[df['named entity'] == 'NON_TECH_RESOLUTION']['output']
			HARDWARE_named_entity = df.loc[df['named entity'] == 'HARDWARE']['output']
			SOFTWARE_named_entity = df.loc[df['named entity'] == 'SOFTWARE']['output']
			SPEC_named_entity = df.loc[df['named entity'] == 'SPEC']['output']
			SHORT_FORM_named_entity = df.loc[df['named entity'] == 'SHORT_FORM']['output']
			ID_named_entity = df.loc[df['named entity'] == 'ID']['output']
		if choice == "displacy_render":
			html = displacy.render(doc, style="ent")
			html = html.replace("\n\n", "\n")
			displacy_text = HTML_WRAPPER.format(html)
			num_of_results = 0
			results = []
		elif choice == 'all':
			#Map the named entity and output to a list
			results = [f"{a} : {b}" for a,b in zip(df['output'], df['named entity'])]
			num_of_results = len(results)
		elif choice == 'organization':
			results = ORG_named_entity
			num_of_results = len(results)
		elif choice == 'person':
			results = PERSON_named_entity
			num_of_results = len(results)
		elif choice == 'geopolitical':
			results = GPE_named_entity
			num_of_results = len(results)
		elif choice == 'money':
			results = MONEY_named_entity
			num_of_results = len(results)
		elif choice == 'cardinal':
			results = CARDINAL_named_entity
			num_of_results = len(results)
		elif choice == 'date':
			results = DATE_named_entity
			num_of_results = len(results)
		elif choice == 'time':
			results = TIME_named_entity
			num_of_results = len(results)
		elif choice == 'product':
			results = PRODUCT_named_entity
			num_of_results = len(results)
		elif choice == 'tech_issue':
			results = TECH_ISSUE_named_entity
			num_of_results = len(results)
		elif choice == 'non_tech_issue':
			results = NON_TECH_ISSUE_named_entity
			num_of_results = len(results)
		elif choice == 'tech_resolution':
			results = TECH_RESOLUTION_named_entity
			num_of_results = len(results)
		elif choice == 'non_tech_resolution':
			results = NON_TECH_RESOLUTION_named_entity
			num_of_results = len(results)
		elif choice == 'hardware':
			results = HARDWARE_named_entity
			num_of_results = len(results)
		elif choice == 'software':
			results = SOFTWARE_named_entity
			num_of_results = len(results)
		elif choice == 'spec':
			results = SPEC_named_entity
			num_of_results = len(results)
		elif choice == 'short_form':
			results = SHORT_FORM_named_entity
			num_of_results = len(results)
		elif choice == 'id':
			results = ID_named_entity
			num_of_results = len(results)
		
	
	return render_template("index.html",results=results,num_of_results = num_of_results, displacy_text=displacy_text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
