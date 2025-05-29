const express = require("express");
const { exec } = require("child_process");
const path = require("path");

const app = express();
app.use(express.json());
app.use(express.static("public")); // serve index.html

app.post("/predict", (req, res) => {
  const inputs = req.body.input;  // e.g. [0,89,2,288.28,1,9,2,2022,10]
  const command = `python predict.py ${inputs.join(" ")}`;

  exec(command, (err, stdout, stderr) => {
    if (err) {
      console.error(stderr);
      return res.status(500).send("Prediction failed.");
    }
    res.json({ prediction: stdout.trim() });
  });
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
