export default function getStudentsByLocation(students, city) {
  // verify if it's an array //
  if (!Array.isArray(students)) {
    return [];
  }

  // filter students toa city //
  return students.filter((student) => student.location === city);
}
