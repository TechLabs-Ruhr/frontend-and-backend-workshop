import os
import json
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL

CONTACTS_FILE = "../contacts.json"

def load_contacts(filename=CONTACTS_FILE):
    with open(filename, 'r') as f:
        return json.load(f)

contacts = load_contacts()

def generate_contact_table(contacts):
    header = html.Tr([
        html.Th("ID"),
        html.Th("First Name"),
        html.Th("Last Name"),
        html.Th("Age"),
        html.Th("Phone Number"),
        html.Th("Address"),
        html.Th("Actions")
    ])
    
    rows = []
    for c in contacts:
        rows.append(
            html.Tr([
                html.Td(c["id"]),
                html.Td(c["firstName"]),
                html.Td(c["lastName"]),
                html.Td(c["age"]),
                html.Td(c["phoneNumber"]),
                html.Td(c["address"]),
                html.Td(
                    html.Button("Delete", id={'type': 'delete-button', 'index': c["id"]})
                )
            ])
        )
    table = html.Table([header] + rows, style={'width': '100%', 'border': '1px solid black', 'borderCollapse': 'collapse'})
    return table

def generate_age_histogram(contacts):
    if not contacts:
        return {}
    df = pd.DataFrame(contacts)
    bins = list(range(0, 101, 10))
    df['age_bucket'] = pd.cut(df['age'], bins=bins, right=False)
    hist = df['age_bucket'].value_counts().sort_index().reset_index()
    hist.columns = ['age_bucket', 'count']
    hist['age_bucket'] = hist['age_bucket'].astype(str)
    fig = px.bar(hist, x='age_bucket', y='count',
                 labels={'age_bucket': 'Age Bucket', 'count': 'Count'},
                 title="Number of Contacts per Age Bucket")
    return fig

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dash Demo - Contacts"),
    
    html.H2("Contact List"),
    html.Div(id='contact-table-div'),
    
    html.Div(id='delete-message', style={'color': 'red', 'margin': '10px 0'}),
    html.Div(id='add-message', style={'color': 'red', 'margin': '10px 0'}),
    
    html.H2("Age Distribution"),
    dcc.Graph(id='age-histogram'),
    
    html.H2("Add New Contact"),
    html.Div([
        dcc.Input(id='input-firstName', type='text', placeholder='First Name'),
        dcc.Input(id='input-lastName', type='text', placeholder='Last Name'),
        dcc.Input(id='input-age', type='number', placeholder='Age', min=0, max=120, value=30),
        dcc.Input(id='input-phoneNumber', type='text', placeholder='Phone Number'),
        dcc.Input(id='input-address', type='text', placeholder='Address'),
        html.Button('Add Contact', id='add-contact-button')
    ], style={'marginTop': '20px', 'display': 'flex', 'gap': '10px', 'flexWrap': 'wrap'})
])

@app.callback(
    [Output('contact-table-div', 'children'),
     Output('age-histogram', 'figure')],
    Input('delete-message', 'children')
)
def update_display(_):
    table = generate_contact_table(contacts)
    histogram = generate_age_histogram(contacts)
    return table, histogram

@app.callback(
    Output('delete-message', 'children'),
    Input({'type': 'delete-button', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def handle_delete(delete_n_clicks):
    global contacts
    ctx = callback_context
    if not ctx.triggered:
        return ""
    
    triggered_prop = ctx.triggered[0]['prop_id']
    try:
        id_str = triggered_prop.split('.')[0]
        button_id = json.loads(id_str)
        delete_id = button_id.get('index')
    except Exception as e:
        return f"Error parsing button id: {e}"
    
    if not any(c['id'] == delete_id for c in contacts):
        return f"Contact with id {delete_id} not found."
    
    contacts = [c for c in contacts if c['id'] != delete_id]
    
    return f"Contact with id {delete_id} deleted successfully."

@app.callback(
    Output('add-message', 'children'),
    Input('add-contact-button', 'n_clicks'),
    State('input-firstName', 'value'),
    State('input-lastName', 'value'),
    State('input-age', 'value'),
    State('input-phoneNumber', 'value'),
    State('input-address', 'value'),
    prevent_initial_call=True
)
def handle_add(add_n_clicks, firstName, lastName, age, phoneNumber, address):
    print(f"Adding contact: {firstName} {lastName}")
    print(f"Age: {age}")
    print(f"Phone number: {phoneNumber}")
    print(f"Address: {address}")
    return "Add contact not implemented (501)"

if __name__ == '__main__':
    app.run_server(debug=True)
