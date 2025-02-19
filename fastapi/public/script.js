document
  .getElementById("load-contacts")
  .addEventListener("click", loadContacts);
document
  .getElementById("add-contact-form")
  .addEventListener("submit", addContact);

function displayError(message) {
  const errorsDiv = document.getElementById("errors");
  errorsDiv.textContent = message;
}

function clearErrors() {
  document.getElementById("errors").textContent = "";
}

function loadContacts() {
  clearErrors();
  fetch("/api/contacts")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Error ${response.status}: ${response.statusText}`);
      }
      return response.json();
    })
    .then((data) => {
      const tbody = document.querySelector("#contacts-table tbody");
      if (data.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6">No contacts found.</td></tr>';
        return;
      }
      tbody.innerHTML = data
        .map(
          (contact) => `
        <tr>
          <td>${contact.id}</td>
          <td>${contact.firstName}</td>
          <td>${contact.lastName}</td>
          <td>${contact.phoneNumber}</td>
          <td>${contact.address}</td>
          <td>${contact.age}</td>
          <td>
            <button onclick="deleteContact(${contact.id})">Delete</button>
          </td>
        </tr>
      `
        )
        .join("");
    })
    .catch((err) => {
      displayError(err.message);
    });
}

function addContact(event) {
  event.preventDefault();
  clearErrors();

  const newContact = {
    firstName: document.getElementById("firstName").value.trim(),
    lastName: document.getElementById("lastName").value.trim(),
    phoneNumber: document.getElementById("phoneNumber").value.trim(),
    address: document.getElementById("address").value.trim(),
    age: document.getElementById("age").value.trim(),
  };

  fetch("/api/contacts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(newContact),
  })
    .then((response) => {
      if (!response.ok) {
        return response.json().then((errData) => {
          throw new Error(
            `Error ${response.status}: ${errData.error || response.statusText}`
          );
        });
      }
      return response.json();
    })
    .then((data) => {
      alert("Contact added successfully!");
      loadContacts();
    })
    .catch((err) => {
      displayError(err.message);
    });
}

function deleteContact(contactId) {
  clearErrors();

  fetch(`/api/contacts/${contactId}`, {
    method: "DELETE",
  })
    .then((response) => {
      if (!response.ok) {
        return response.json().then((errData) => {
          throw new Error(
            `Error ${response.status}: ${errData.error || response.statusText}`
          );
        });
      }
      return response.json();
    })
    .then((data) => {
      alert("Contact deleted successfully!");
      loadContacts();
    })
    .catch((err) => {
      displayError(err.message);
    });
}
