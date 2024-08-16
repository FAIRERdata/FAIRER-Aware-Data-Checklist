# Data Checklist Manual

## Introduction

This repository contains the Data Checklist. Data checklists are a useful data management tool for data providers and for data repositories, as well as for data stewards and managers who need to approve data without having been involved in their production. The Data Checklist can serve as a preliminary check for essential data do's and don'ts.

## Getting Started

### Prerequisites

Before you can use the Data Checklist repository, you need to download the repository and install some Python packages. 

1. Download a ZIP file of the FAIRER-Aware-Data-Checklist repository and extract all files

2. Open the extracted FAIRER-Aware-Data-Checklist folder in VScode or code editor of choice. Make sure the terminal is navigated to the repository folder.

3. Install the required Python packages, `flask`, `pandas`, and `openpyxl`:

```bash
pip3 install flask pandas
```
If the above does not work, try this: 
```bash
py -m pip install flask pandas openpxyl
```
## Usage

### Gathering Entries

When adding new entries or changes to questions to the Data checklist, make sure to format them in the same way as the existing entries in 'data/Data checklist.xlsx'. This ensures that the entries can be correctly processed by the application. Particularly order the questions from least to greatest (i.e. 1-9 if 9 is the last module).

If new question modules are added, check if there is a new colour to represent the module in variable `colour_lst` in `data_api.py`.

### Running the Data API

After you have gathered your vocabularies and formatted them correctly, you can run the `data_api.py` script to render an HTML template with the vocabularies.

1. Open your terminal.
2. Navigate to the directory where `data_api.py` is located.
3. Run the following command:

```bash
python3 data_api.py
```
If the above does not work, try:
```bash
py data_api.py
```

### Viewing the Generated HTML

After running the `data_api.py` script, you can view the generated HTML to make sure it was created successfully.

1. Open a web browser and navigate to `http://localhost:5000`. This is where the Flask server is running.
2. If the HTML was generated successfully, you should see your vocabularies displayed in the browser.
3. If there was an error generating the HTML, you will see an error log in the browser. You can use this log to troubleshoot any issues.

The generated HTML file is saved as `docs/index.html`. This file is a preview of the designated deployment.

### Refreshing the Deployment

If you make changes to any of the code and would like to see those changes reflected in the deployment, you can do so by refreshing `http://localhost:5000`.

1. After making your changes, save your files and ensure the Flask server is still running.
2. Open a web browser and navigate to `http://localhost:5000`. Refresh the page.
3. Open `docs/index.html` in your web browser and refresh the page. You should now see the updated version of the HTML.

### Editing template.html

If needed, new elements for the website (index.html) should be added to template.html. Note that the IDE used may detect errors in template.html due to template variables if the language detection mode is set to html itself. However, the code will run successfully even with these "errors." Changing the language detection mode to Django html or Jinja html will remove the errors.
