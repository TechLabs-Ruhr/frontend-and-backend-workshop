import json
import streamlit as st
import pandas as pd

CONTACTS_FILE = "../contacts.json"

def load_contacts(filename=CONTACTS_FILE):
    with open(filename, "r") as f:
        return json.load(f)

def display_contacts(contacts):
    st.write("### Contact List")

    col_id, col_first, col_last, col_age, col_phone, col_address, col_actions = st.columns(
        [1, 2, 2, 1, 2, 3, 2]
    )
    col_id.write("ID")
    col_first.write("First Name")
    col_last.write("Last Name")
    col_age.write("Age")
    col_phone.write("Phone Number")
    col_address.write("Address")
    col_actions.write("Actions")

    for contact in contacts:
        cols = st.columns([1, 2, 2, 1, 2, 3, 2])
        cols[0].write(contact.get("id"))
        cols[1].write(contact.get("firstName"))
        cols[2].write(contact.get("lastName"))
        cols[3].write(contact.get("age"))
        cols[4].write(contact.get("phoneNumber"))
        cols[5].write(contact.get("address"))
        if cols[6].button("Delete", key=f"delete_{contact.get('id')}"):
            st.error("Delete not implemented (501)")

def display_age_distribution(contacts):
    st.write("### Age Distribution")
    if contacts:
        df = pd.DataFrame(contacts)
        bins = list(range(0, 101, 10))
        df["age_bucket"] = pd.cut(df["age"], bins=bins, right=False)
        hist = df["age_bucket"].value_counts().sort_index()
        hist_df = hist.reset_index()
        hist_df.columns = ["age_bucket", "count"]
        hist_df["age_bucket"] = hist_df["age_bucket"].astype(str)
        st.bar_chart(hist_df.set_index("age_bucket"))
    else:
        st.write("No contacts available for plotting.")

def add_contact_form():
    st.write("### Add New Contact")
    with st.form("add_contact_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        phone_number = st.text_input("Phone Number")
        address = st.text_input("Address")
        submitted = st.form_submit_button("Add Contact")
        if submitted:
            st.error("Add contact not implemented (501)")

def main():
    st.title("Streamlit Demo - Contacts")

    contacts = load_contacts()

    display_contacts(contacts)
    display_age_distribution(contacts)
    add_contact_form()


if __name__ == "__main__":
    main()
