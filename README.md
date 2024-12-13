# Unique Character Count

This project includes a Python function that counts the frequency of unique characters in a given string. The function is optimized for large inputs.

## Features

- **Accurate Character Counting**: Handles both lowercase and uppercase letters.
- **Optimized for Performance**: Processes large strings efficiently using a dictionary.
- **Simple Input/Output**: Easy-to-use function that accepts a string and returns a dictionary of character frequencies.

## Example

### Input
```python
"characteristics"
```

### Output
```python
 {'c': 3, 'h': 1, 'a': 2, 'r': 2, 't': 2, 'e': 1, 'i': 2, 's': 2}
```

## Big-O Analysis

- **Time Complexity**: `O(n)`, where `n` is the length of the input string. Each character is processed once.
- **Space Complexity**: `O(u)`, where `u` is the number of unique characters in the string.

## Usage Instructions

1. Clone the repository:
   ```bash
   https://github.com/sarah98-bit/attachment.git
   ```
2. Navigate to the project directory:
   ```bash
   cd unique-character-count
   ```
3. Run the Python script:
   ```bash
   python unique_character_count.py
   ```


# FAQ Accordion Component

## Project Description
The FAQ Accordion Component is a responsive and accessible accordion feature for displaying frequently asked questions (FAQs). It allows users to toggle the visibility of answers by clicking on the questions. This project is designed with user experience and accessibility in mind, ensuring smooth navigation across devices and compatibility with assistive technologies.

## Features
- **Accordion Behavior:** Only one FAQ answer is visible at a time.
- **Keyboard Navigation:** Users can navigate and toggle FAQs using the `Tab`, `Enter`, or `Space` keys.
- **Accessibility:** ARIA roles and attributes are implemented for screen-reader compatibility.
- **Responsive Design:** Adapts to different screen sizes for seamless display on mobile, tablet, and desktop devices.
- **Interactive States:** Visual feedback for hover and focus states with smooth transitions.

## Technologies Used
- **HTML5:** For the structure and semantic markup.
- **CSS3:** For styling and responsive design.
- **JavaScript:** For interactive functionality.

## Installation and Setup
1. Clone the repository:
   ```bash
    https://github.com/sarah98-bit/attachment.git
   ```
2. Navigate to the project directory:
   ```bash
   cd faq-accordion
   ```
3. Open the `FAQ Accordion.html` file in your preferred browser.

## Usage
1. Click on a question to view the corresponding answer.
2. Use `Tab` to navigate through the questions and `Enter` or `Space` to toggle visibility.

## File Structure
```
faq-accordion/
├── FAQ Acordion.html       # Main HTML file
├── styles.css       # CSS styles for layout and design
├── script.js        # JavaScript for functionality
```

## Accessibility Features
- ARIA roles and attributes (`aria-expanded`, `aria-hidden`) ensure compatibility with screen readers.
- Keyboard navigation allows toggling and focus management without using a mouse.
- Focus and hover states provide clear visual indicators.

## Responsive Behavior
- On mobile devices, FAQ items stack vertically for better readability.
- On larger screens, the component adjusts to utilize available space.
- Smooth transitions enhance user experience across all devices.
## Future Enhancements
- Adding animation customizations for more visually appealing transitions.
- Incorporating themes or dark mode for better user preferences.
- Extending functionality to allow multiple answers to be visible simultaneously if needed.

# Flask API for CHAMA Group Creation

This Flask API provides an endpoint for creating CHAMA groups. It accepts JSON data through a `POST` request, validates the input, and returns the created group details, including a unique group ID.

---

## Features
- **Endpoint**: `/groups` (POST)
- **Request Body**: JSON data containing group details and admin information.
- **Response**: JSON response with the created group details or error messages for invalid input.
- **Error Handling**: Handles invalid input and unexpected errors gracefully.
- **Simulated Database**: Simulates group creation by generating a mock group ID.
- **Logging**: Logs requests and errors for debugging purposes.

---

## Code Explanation

### File: `app.py`

### 1. **Dependencies**
```python
from flask import Flask, request, jsonify
import logging
```
- `Flask`: Micro web framework used for building the API.
- `request`: To parse incoming HTTP requests.
- `jsonify`: To create JSON responses.
- `logging`: For debugging and logging errors.

### 2. **Application Setup**
```python
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
```
- `app`: Initializes the Flask application.
- `logging.basicConfig`: Configures logging to the DEBUG level for detailed logs.

### 3. **Route Definition**
```python
@app.route('/groups', methods=['POST'])
def create_group():
```
- Defines a route `/groups` that only accepts `POST` requests.
- Calls the `create_group()` function to process the request.

### 4. **Request Handling**
```python
data = request.get_json()
logging.debug(f"Received data: {data}")
```
- Parses the incoming JSON request and logs the data for debugging.

### 5. **Data Extraction and Validation**
```python
group_name = data['groupName']
admin_name = data['admin']['name']
admin_email = data['admin']['email']

if not group_name or not admin_name or not admin_email:
    return jsonify({'error': 'Invalid input: groupName and admin fields are required'}), 400
```
- Extracts required fields (`groupName`, `admin.name`, `admin.email`) from the request.
- Returns a `400 Bad Request` error if any required fields are missing.

### 6. **Simulated Database Interaction**
```python
group_id = create_group_in_database(group_name, admin_name, admin_email)
```
- Calls the `create_group_in_database()` function to simulate database insertion.

#### Function: `create_group_in_database()`
```python
def create_group_in_database(group_name, admin_name, admin_email):
    logging.info("Simulating database insertion for the group")
    return "12345"  # Return a mock group ID
```
- Simulates storing the group in a database and returns a mock group ID (`12345`).

### 7. **Response Creation**
```python
response = {
    'groupId': group_id,
    'groupName': group_name,
    'admin': {
        'name': admin_name,
        'email': admin_email
    }
}
logging.debug(f"Response data: {response}")
return jsonify(response), 201
```
- Constructs a JSON response containing the group details and returns it with a `201 Created` status code.

### 8. **Error Handling**
#### Missing Fields
```python
except KeyError as e:
    logging.error(f"KeyError: {e}")
    return jsonify({'error': 'Invalid input: Missing required fields'}), 400
```
- Catches `KeyError` exceptions for missing fields in the input and returns a `400 Bad Request` error.

#### Unexpected Errors
```python
except Exception as e:
    logging.error(f"Unexpected error: {e}")
    return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500
```
- Catches all other exceptions and returns a `500 Internal Server Error` response.

### 9. **Application Entry Point**
```python
if __name__ == '__main__':
    app.run(debug=True)
```
- Starts the Flask development server with debugging enabled.

---

## Example Usage

### Request
**URL**: `http://127.0.0.1:5000/groups`
**Method**: `POST`
**Headers**:
```plaintext
Content-Type: application/json
```
**Body**:
```json
{
    "groupName": "Family Savings Group",
    "admin": {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
}
```

### Successful Response (201 Created)
```json
{
    "groupId": "12345",
    "groupName": "Family Savings Group",
    "admin": {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
}
```

### Error Responses
#### Missing Fields (400 Bad Request)
```json
{
    "error": "Invalid input: groupName and admin fields are required"
}
```
#### Unexpected Error (500 Internal Server Error)
```json
{
    "error": "An unexpected error occurred. Please try again later."
}
```

---

## Testing the API
1. **Run the Application**:
   ```bash
   python app.py
   ```
2. **Send Requests**:
   Use Postman, cURL, or any HTTP client to send requests to `http://127.0.0.1:5000/groups`.
3. **Debugging**:
   Check the console logs for debugging information and errors.

---

## Future Enhancements
- Integrate a real database for group creation.
- Add authentication and authorization for admin users.
- Improve error handling with detailed messages.
- Add unit tests to validate functionality.




