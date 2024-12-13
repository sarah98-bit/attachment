# Capitalize Words Program

## Description
This is a simple Java program that accepts a string as input, capitalizes the first letter of each word in the string, and returns the modified string. It works by splitting the string into individual words, capitalizing the first letter of each word, and then reassembling the words into a single string.

## Features
- Capitalizes the first letter of each word.
- Converts the rest of the letters in each word to lowercase.
- Handles multiple words separated by spaces.

## Example
### Input:
```
"i love programming"
```

### Output:
```
"I Love Programming"
```

### How it works:
1. The input string is split into words using space as the delimiter.
2. The first letter of each word is capitalized, while the rest of the letters are converted to lowercase.
3. The words are then joined back together with spaces, forming the final result.

## Usage
1. Clone the repository.
```
https://github.com/sarah98-bit/attachment
```
3. Open the project in your preferred Java IDE or text editor.
```
CapitalizeWords.java
```
5. Run the `CapitalizeWords` class.
6. Modify the `input` variable with any string of your choice.

### Example Run:
```
Input: "hello world from java" Output: "Hello World From Java"
```

## Code Explanation
- The program uses a `StringBuilder` to build the result efficiently.
- The string is split into an array of words using the `split(" ")` method.
- Each word is processed: the first character is converted to uppercase, and the rest of the characters are converted to lowercase.
- The `trim()` method is used to remove any extra spaces from the result.

## Requirements
- Java 8 or higher.

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
├── FAQ Accordion.html       # Main HTML file
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
