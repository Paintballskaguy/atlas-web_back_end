import { listOfStudents } from './9-hoisting.js';

test('listOfStudents has the correct length', () => {
  expect(listOfStudents.length).toBe(5);
});