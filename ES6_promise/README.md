# Summary README
## Overview
This project contains a collection of JavaScript files that demonstrate various concepts related to Promises, error handling, and asynchronous operations. Each file focuses on a specific functionality, such as handling API responses, managing multiple promises, and performing safe operations with error handling.

## Files and Their Concepts
1. 0-promise.js
Concept: Introduces a basic Promise that does nothing (pending state).

Purpose: Demonstrates the creation of a simple Promise.

2. 1-promise.js
Concept: Simulates an API response using a Promise that resolves or rejects based on a condition.

Purpose: Shows how to handle success and failure in a Promise.

3. 2-then.js
Concept: Handles a Promise response, attaching .then, .catch, and .finally handlers.

Purpose: Demonstrates chaining and handling resolved/rejected Promises.

4. 3-all.js
Concept: Uses Promise.all to handle multiple promises concurrently.

Purpose: Shows how to execute and combine results from multiple asynchronous operations.

5. 4-user-promise.js
Concept: Resolves a Promise with user data (first name and last name).

Purpose: Demonstrates resolving a Promise with a fixed value.

6. 5-photo-reject.js
Concept: Rejects a Promise with an error message related to photo processing.

Purpose: Demonstrates rejecting a Promise with a custom error.

7. 6-final-user.js
Concept: Uses Promise.allSettled to handle multiple promises and capture their results, regardless of success or failure.

Purpose: Shows how to handle multiple asynchronous operations and process their outcomes.

8. 7-load_balancer.js
Concept: Uses Promise.race to return the result of the first resolving Promise.

Purpose: Demonstrates balancing between two competing asynchronous operations.

9. 8-try.js
Concept: Performs division and throws an error if the denominator is 0.

Purpose: Demonstrates error handling for invalid operations.

10. 9-try.js
Concept: Executes a function, captures its result or error, and appends a final message to a queue.

Purpose: Demonstrates handling function execution with try-catch-finally and managing results in a structured way.

Key Concepts Covered
Promises: Creation, resolution, rejection, and chaining.

Error Handling: Using try-catch, .catch, and Promise.allSettled to manage errors.

Asynchronous Operations: Handling multiple promises concurrently with Promise.all and Promise.race.

Safe Operations: Preventing invalid operations (e.g., division by zero) with error checks.

Usage
Each file is self-contained and can be imported and used in other JavaScript projects.

The functions are designed to demonstrate specific asynchronous and error-handling patterns.

