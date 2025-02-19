const fs = require("fs");
const express = require("express");
const app = express();
const port = 3000;

const contacts = JSON.parse(fs.readFileSync("../contacts.json", "utf8"));

app.use(express.json());

app.use(express.static("public"));

app.get("/api/contacts", (req, res) => {
  res.status(501).json({ error: "Not implemented" });
});

app.post("/api/contacts", (req, res) => {
  res.status(501).json({ error: "Not implemented" });
});

app.delete("/api/contacts/:id", (req, res) => {
  res.status(501).json({ error: "Not implemented" });
});

app.listen(port, () => {
  console.log(`Express app listening at http://localhost:${port}`);
});
