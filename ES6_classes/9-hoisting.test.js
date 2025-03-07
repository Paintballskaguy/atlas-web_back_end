import { listOfStudents, StudentHolberton } from './9-hoisting.js';

describe('listOfStudents', () => {
  it('should have the correct length', () => {
    expect(listOfStudents.length).toBe(5);
  });

  it('should contain instances of StudentHolberton', () => {
    listOfStudents.forEach((student) => {
      expect(student).toBeInstanceOf(StudentHolberton);
    });
  });

  it('should have the correct fullStudentDescription for each student', () => {
    const expectedDescriptions = [
      'Guillaume Salva - 2020 - San Francisco',
      'John Doe - 2020 - San Francisco',
      'Albert Clinton - 2019 - San Francisco',
      'Donald Bush - 2019 - San Francisco',
      'Jason Sandler - 2019 - San Francisco',
    ];

    const actualDescriptions = listOfStudents.map(
      (student) => student.fullStudentDescription,
    );

    expect(actualDescriptions).toEqual(expectedDescriptions);
  });
});