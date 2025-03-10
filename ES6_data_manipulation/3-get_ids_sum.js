export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return 0;
  }

  // reduce to check total of student IDs. //
  return students.reduce((sum, student) => sum + student.id, 0);
}
