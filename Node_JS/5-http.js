const http = require('http');
const fs = require('fs');

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const database = process.argv[2];
    if (!database) {
      res.statusCode = 500;
      res.end('This is the list of our students\nCannot load the database');
      return;
    }

    fs.readFile(database, 'utf8', (err, data) => {
      if (err) {
        res.statusCode = 500;
        res.end('This is the list of our students\nCannot load the database');
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      if (lines.length <= 1) {
        res.statusCode = 200;
        res.end('This is the list of our students\nNo students available');
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
      res.statusCode = 200;
      res.end(response.trim());
    });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server running at http://localhost:1245/');
});

module.exports = app;
