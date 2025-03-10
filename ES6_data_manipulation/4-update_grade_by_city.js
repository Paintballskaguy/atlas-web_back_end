export default function updateStudentGradeByCity(students, city, newGrades) {
  // Check if the input is an array //
  if (!Array.isArray(students) || !Array.isArray(newGrades)) {
    return [];
  }

  const studentsInCity = students.filter((student) => student.location === city);

  return studentsInCity.map((student) => {
    // Find the grade object for the current student //
    const gradeObj = newGrades.find((grade) => grade.studentId === student.id);

    // if a grade is found, assign. else set grade to N/A //
    return { ...student, grade: gradeObj ? gradeObj.grade : 'N/A' };
  });
}
