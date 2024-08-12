###################################################
# Script name:    data_api.py
# Number lines:  55                     
# Version:           2024-04-11
# Software:         Python 3.12.2 (2024-02-06)
#                         Visual Studio Code (1.88.0)
# OS:                   Windows 11 Enterprise (2023-11-07, Build 22631.3296)
# Machine:          Dynabook Tecra
# Programmer:	  Esther Liu, ORCID ID https://orcid.org/0000-0001-9138-5986
# Validated by:  	Not validated
# Rcode licence:	None
# Data license:          None
# Purpose:  	       - Read data from an Excel file, convert it to a list of dictionaries, and render a Static HTML template.
# Merging:             - Generate a Static HTML file.
###################################################

from flask import Flask, render_template
import pandas as pd
import os

# Get the directory of the current script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

def separate_lists(lst):
    last_num = int(lst[-1]['Data Checklist Questions'][0])
    question_range = range(1,last_num + 1)
    separated_lst = []
    for i in question_range:
        separated_lst.append([item for item in lst if item['Data Checklist Questions'][0] == str(i)])
    return separated_lst
    

@app.route('/')

def data_checklist():
    # Read data from Excel file
    df = pd.read_excel('data/Data checklist.xlsx', sheet_name="DATA CHECKLISTS")
    categories = pd.read_excel('data/Data checklist.xlsx', sheet_name="Data checklist modules")
    categories = categories.iloc[:,0].dropna().to_list()[1:]
    
    # Convert DataFrame to list of dictionaries
    appendix = df.where(pd.notnull(df), '').to_dict(orient='records')
    appendix_headers = appendix.pop(0)
    separated_lst = separate_lists(appendix)
    colour_lst = ["#e6194B", "#f58231", "#ffe119", "#bfef45", "#3cb44b", "#42d4f4", "#4363d8", "#911eb4", "#f032e6"]
    
    
    # Render the index.html template
    rendered_html = render_template('template.html', colour_lst=colour_lst, categories=categories, separated_lst=separated_lst, appendix=appendix, appendix_headers=appendix_headers)
    
    df.to_excel("data/blank_data_checklist.xlsx", index=False, header=False)
    # Ensure the 'docs' folder exists
    if not os.path.exists('docs'):
        os.makedirs('docs')

    # Save the rendered HTML to 'docs/index.html'
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    return 'Static HTML file generated successfully'

if __name__ == '__main__':
    app.run(debug=True)