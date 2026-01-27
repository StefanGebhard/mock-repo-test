# Push: Update utils.js

## Overview

This update modifies the `utils.js` file to include a revised `add` function. The primary motivation for this change is to ensure that the function can gracefully handle string inputs by converting them to numbers before performing addition.

## Usage

The `add` function can be used to sum three numerical or string-representable numerical values.

```javascript
// Assuming utils.js is imported as 'utils'

let sum1 = utils.add(1, 2, 3);
console.log(sum1); // Output: 6

let sum2 = utils.add('5', 10, '15');
console.log(sum2); // Output: 30
```

## API Reference

### `add(a, b, c)`

*   **Description:** Adds three values together. It converts all input arguments to numbers before performing the addition.
*   **Parameters:**
    *   `a`: The first value (number or string).
    *   `b`: The second value (number or string).
    *   `c`: The third value (number or string).
*   **Returns:** The sum of `a`, `b`, and `c` as a number.