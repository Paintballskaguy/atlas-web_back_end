export default function getListStudentIds(students) {
  // verify it's an array. //
  if (!Array.isArray(students)) {
    return [];
  }

  // map function to pull the ID //
  return students.map((student) => student.id);
}
