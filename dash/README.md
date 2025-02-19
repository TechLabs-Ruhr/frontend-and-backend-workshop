# Dash API Demo - Contacts

This repository demonstrates a simple web application built with Dash for managing contacts. The app reads contact data from a JSON file (`contacts.json`) and displays them in a table along with a histogram showing the number of contacts per age bucket. Additionally, the app includes functionality to delete contacts, while adding contacts is currently a skeleton implementation, so it's up to you to implement it.

## Setup Instructions

1. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

3. Run the API

```bash
python app.py
```

4. Open the app

Open [http://localhost:8050](http://localhost:8050) in your browser to see the app.
