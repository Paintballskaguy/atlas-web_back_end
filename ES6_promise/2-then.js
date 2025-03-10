export default function handleResponseFromAPI(promise) {
  return promise
  // this is for success //
    .then(() => ({ status: 200, body: 'success' }))
    // this is for a rejection //
    .catch(() => new Error())
    // this will should show if the API handled the call and not a 404 not found //
    .finally(() => {
      console.log('Got a response from the API');
    });
}
