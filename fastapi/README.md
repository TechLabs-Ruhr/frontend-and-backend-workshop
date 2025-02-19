# FastAPI API Demo - Contacts

This repository demonstrates a simple API built with FastAPI for managing contacts. The API serves sample contact data and provides endpoints for retrieving, adding, and deleting contacts. The latter endpoints are provided as skeletons (returning a 501 error) so it's up to you to implement the actual functionality.

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
uvicorn main:app --reload
```

4. Open the app

Open [http://localhost:8000](http://localhost:8000) in your browser to see the app.

FastAPI also automatically generates OpenAPI documentation for your API. You can view it at [http://localhost:8000/docs](http://localhost:8000).
