export default function createInt8TypedArray(length, position, value) {
  // Check if the position is within  range //
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);

  const dataView = new DataView(buffer);

  dataView.setInt8(position, value);

  return dataView;
}
