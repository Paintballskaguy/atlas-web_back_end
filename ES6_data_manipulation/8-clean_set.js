export default function cleanSet(set, startString) {
  // checks if startString is a string and not devoid of feeling //
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }
  // filtering values that start with startString and removing the startstring, which makes sense //
  const filteredValues = Array.from(set)
    .filter((value) => typeof value === 'string' && value.startsWith(startString))
    .map((value) => value.slice(startString.length));
  return filteredValues.join('-');
}
