const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.type('text').send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  if (!database) {
    res.type('text').send('This is the list of our students\nCannot load the database');
    return;
  }

  fs.readFile(database, 'utf8', (err, data) => {
    if (err) {
      res.type('text').send('This is the list of our students\nCannot load the database');
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    if (lines.length <= 1) {
      res.type('text').send('This is the list of our students\nNo students available');
      return;
    }

    const students = lines.slice(1);
    const fields = {};
    let totalStudents = 0;

    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');
      if (field && firstname) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
        totalStudents++;
      }
    });

    let response = 'This is the list of our students\n';
    response += `Number of students: ${totalStudents}\n`;
    for (const [field, names] of Object.entries(fields)) {
      response += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }
    res.type('text').send(response.trim());
  });
});

app.listen(1245, () => {
  console.log('Server running at http://localhost:1245/');
});

module.exports = app;
