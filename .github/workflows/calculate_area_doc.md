### Explanation of the `calculate_area` Function

#### Purpose
The `calculate_area` function is designed to calculate the area of geometric shapes based on the provided shape type and parameters. It supports two shapes: a rectangle and a circle. If an unsupported shape is provided or the parameters are invalid, the function returns `None`.

#### Inputs
- `shape` (str): The type of shape to calculate the area for. Supported values are `'rectangle'` and `'circle'` (case-insensitive).
- `parameters` (dict): A dictionary containing the necessary dimensions for the shape:
  - For `'rectangle'`: Must include `'width'` and `'height'` keys with numeric values.
  - For `'circle'`: Must include a `'radius'` key with a numeric value.

#### Outputs
- Returns a `float` representing the calculated area if the shape and parameters are valid.
- Returns `None` if:
  - The shape is not supported.
  - Required parameters are missing.
  - Parameters are invalid (e.g., non-numeric values or negative dimensions).

#### Error Handling
- The function includes robust error handling:
  - Checks for missing parameters (e.g., `'width'` or `'height'` for a rectangle).
  - Validates that parameters are numeric (integers or floats).
  - Ensures dimensions are positive (e.g., no negative radius).
  - Prints error messages to help with debugging (e.g., "Error: 'circle' requires 'radius' in parameters").

#### Examples
1. **Rectangle Example**:
   ```python
   rectangle_params = {"width": 5, "height": 3}
   area = calculate_area("rectangle", rectangle_params)
   print(area)  # Output: 15.0
