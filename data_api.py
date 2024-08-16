'''
 Script name:    data_api.py
 Number lines:   65                    
 Date updated:   8/16/2024        
 Software:       Python 3.11.0 64-bit 
                 Visual Studio Code (1.92.1)
                 
 OS:             Windows 11 Enterprise (2/8/2024, Build 22631.3880)
 Machine:        Dynabook Tecra
 Authors:	     Emily Chu, ORCID ID https://orcid.org/0009-0001-8417-0837 ;Esther Liu, ORCID ID https://orcid.org/0000-0001-9138-5986
 Validated by:   Not validated
 Data license:   None
 Purpose:  	     - Read data from an Excel file, convert it to a list of dictionaries, and render a Static HTML template.
 Input:          Data checklist.xlsx
 Output:         - index.html 
'''

from flask import Flask, render_template
import pandas as pd
import os
import re

# Get the directory of the current script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

'''
Separates the list of dictionaries into a list of lists for each module based on last module number
input: list of dictionaries
output: list of lists of dictionaries
'''
def separate_lists(lst):
    last_num = lst[-1]['Data Checklist Questions'].split('-')[0]
    last_num = int(re.findall('\d+', last_num)[0])
    question_range = range(1,last_num + 1)
    separated_lst = []
    for i in question_range:
        separated_lst.append([item for item in lst if item['Data Checklist Questions'][0] == str(i)])
    return separated_lst
    

@app.route('/')

def data_checklist():
    # Read questions data from Excel file 
    df = pd.read_excel('data/Data checklist.xlsx', sheet_name="DATA CHECKLISTS")
    # Read module names from Excel sheet
    categories = pd.read_excel('data/Data checklist.xlsx', sheet_name="Data checklist modules")
    # Get only main module names
    categories = categories.iloc[:,0].dropna().to_list()[1:]
    
    # Convert DataFrame to list of dictionaries
    appendix = df.where(pd.notnull(df), '').to_dict(orient='records')
    # Get "column names"
    appendix_headers = appendix.pop(0)
    
    # Separate into the main modules
    separated_lst = separate_lists(appendix)
    
    # Colours for the main modules (add if needed for new modules)
    # current colours from https://sashamaps.net/docs/resources/20-colors/
    colour_lst = ["#e6194B", "#f58231", "#ffe119", "#bfef45", "#3cb44b", "#42d4f4", "#4363d8", "#911eb4", "#f032e6", '#469990', '#dcbeff', '#000075', '#aaffc3', '#9A6324', '#808000']
    
    # Render the index.html template
    rendered_html = render_template('template.html', colour_lst=colour_lst, categories=categories, separated_lst=separated_lst, appendix=appendix, appendix_headers=appendix_headers)
    
    # Create blank_data_checklist.xlsx for print to excel function 
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