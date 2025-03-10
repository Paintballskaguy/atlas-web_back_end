export default function updateUniqueItems(map) {
  // veriify input //
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  // go through the map and update quantities //
  for (const [key, value] of map) {
    if (value === 1) {
      map.set(key, 100);
    }
  }

  return map;
}
