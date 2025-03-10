export default function hasValuesFromArray(set, array) {
  // checks to see if all elements in the array exist //
  return array.every((element) => set.has(element));
}
