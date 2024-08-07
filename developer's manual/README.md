# Data Checklist Manual

## Introduction

This repository contains the Data Checklist.

## Getting Started

### Prerequisites

## Usage

### Gathering Vocabularies

When adding new entries or changes to questions to the Data checklist, make sure to format them in the same way as the existing entries in 'data/Data checklist.xlsx'. This ensures that the entries can be correctly processed by the application.

### Running the Data API

After you have gathered your vocabularies and formatted them correctly, you can run the `data_api.py` script to render an HTML template with the vocabularies.

1. Open your terminal.
2. Navigate to the directory where `data_api.py` is located.
3. Run the following command:

```bash
python3 data_api.py
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
