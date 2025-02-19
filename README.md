# API + Frontend Demo - Connecting Backend to Frontend

This repository demonstrates different approaches to building and connecting backends with frontends using various frameworks. It provides implementations in **Express**, **FastAPI**, **Dash**, and **Streamlit**, allowing teams to explore different options based on their needs.

Each implementation follows the same **contact management example**, including:

- Listing contacts in a table
- Implementing delete functionality
- Providing a form to add new contacts

Dash and Streamlit also include a **data visualization** feature, allowing you to visualize the contact's age distribution in a histogram.

None of the examples are complete. They all lack certain features only providing a skeleton implementation, so it's up to you to implement them.

## Choosing the Right Framework

- If your team includes both **frontend and backend developers**, **Express (Node.js)** or **FastAPI (Python)** are great choices since they provide REST APIs that can be consumed by a separate frontend.
- If your team is **more data/AI-focused** and prefers an integrated frontend, **Dash** or **Streamlit** are excellent choices, as they allow you to build data visualizations and user interfaces without needing a separate frontend framework.

## Setup & Running the Apps

Each implementation has its own **setup instructions** in its respective folder:

- [Express Setup](./express/README.md)
- [FastAPI Setup](./fastapi/README.md)
- [Dash Setup](./dash/README.md)
- [Streamlit Setup](./streamlit/README.md)

You can navigate into the corresponding folder and follow the instructions in the `README.md` file to get started.

## License

This project is licensed under the **MIT License**, so feel free to use, modify, and distribute it as you see fit.

This repository is based on the original work of [NJannasch](https://github.com/NJannasch/techlabs-dortmund-wd-dsai).
