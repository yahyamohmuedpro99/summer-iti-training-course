# Day 1: Introduction to JavaScript

## Objectives:
* Understand what JavaScript is and how it integrates with HTML.
* Learn basic JavaScript syntax and data types.
* Write simple scripts that manipulate data and interact with the user.

## 1. What is JavaScript?

JavaScript is a versatile programming language primarily used for creating interactive and dynamic content on websites. It's an essential tool for modern web development.

### Role of JavaScript in web development:
- Client-side scripting: Runs in the user's browser
- Enhances user interaction and experience
- Manipulates HTML content dynamically
- Communicates with servers (AJAX)
- Enables single-page applications (SPAs)

### Differences between JavaScript, HTML, and CSS:
- HTML: Structure of the web page
- CSS: Styling and layout of the web page
- JavaScript: Behavior and interactivity of the web page

Example:
```html
<!-- HTML provides structure -->
<button id="myButton">Click me!</button>

<!-- CSS provides styling -->
<style>
  #myButton {
    background-color: blue;
    color: white;
  }
</style>

<!-- JavaScript provides interactivity -->
<script>
  document.getElementById("myButton").addEventListener("click", function() {
    alert("Button clicked!");
  });
</script>
```

### Examples of dynamic web content powered by JavaScript:
- Form validation
- Interactive maps (e.g., Google Maps)
- Real-time updates (e.g., social media feeds)
- Animations and transitions
- Dynamic data visualization

## 2. Including JavaScript in HTML Pages

### `<script>` tag placement:
JavaScript can be included in the `<head>` or `<body>` of an HTML document.

In the `<head>`:
```html
<!DOCTYPE html>
<html>
<head>
  <script>
    // JavaScript code here
  </script>
</head>
<body>
  <!-- HTML content -->
</body>
</html>
```

In the `<body>` (often preferred for performance):
```html
<!DOCTYPE html>
<html>
<head>
  <!-- Other head elements -->
</head>
<body>
  <!-- HTML content -->
  <script>
    // JavaScript code here
  </script>
</body>
</html>
```

### External JavaScript files:
For better organization and caching, JavaScript is often placed in external files:

```html
<!DOCTYPE html>
<html>
<head>
  <script src="myscript.js"></script>
</head>
<body>
  <!-- HTML content -->
</body>
</html>
```

## 3. Basic Syntax and Variables

### Statements and semicolons:
JavaScript statements are separated by semicolons (;). While they're often optional, it's good practice to include them.

```javascript
let x = 5;
console.log(x);
```

### Comments:
```javascript
// This is a single-line comment

/*
This is a
multi-line comment
*/
```

### Variables: var, let, and const:
- `var`: Function-scoped or globally-scoped (older, less used now)
- `let`: Block-scoped, can be reassigned
- `const`: Block-scoped, cannot be reassigned

```javascript
var oldWay = "I'm function-scoped";
let canChange = "I can be reassigned";
const cantChange = "I cannot be reassigned";

canChange = "See? I changed";
// cantChange = "This would cause an error";
```

### Data types:
- Numbers: `let age = 25;`
- Strings: `let name = "John";`
- Booleans: `let isStudent = true;`
- Null: `let empty = null;`
- Undefined: `let notDefined;`

### Variable naming conventions:
- Use camelCase for variable names
- Start with a letter, underscore, or dollar sign
- Can contain letters, numbers, underscores, or dollar signs
- Case-sensitive
- Avoid reserved keywords

Good examples:
```javascript
let firstName = "John";
let userAge = 25;
let is_student = true; // valid but not conventional in JavaScript
```

## 4. Operators and Expressions

### Arithmetic operators:
```javascript
let a = 10;
let b = 3;

console.log(a + b);  // Addition: 13
console.log(a - b);  // Subtraction: 7
console.log(a * b);  // Multiplication: 30
console.log(a / b);  // Division: 3.3333...
console.log(a % b);  // Modulus (remainder): 1
```

### Assignment operators:
```javascript
let x = 5;
x += 3;  // Equivalent to: x = x + 3
console.log(x);  // 8

x *= 2;  // Equivalent to: x = x * 2
console.log(x);  // 16
```

### Comparison operators:
```javascript
let a = 5;
let b = "5";

console.log(a == b);   // true (loose equality)
console.log(a === b);  // false (strict equality)
console.log(a != b);   // false (loose inequality)
console.log(a !== b);  // true (strict inequality)
console.log(a > 3);    // true
console.log(a <= 5);   // true
```

### Logical operators:
```javascript
let isAdult = true;
let hasLicense = false;

console.log(isAdult && hasLicense);  // false (AND)
console.log(isAdult || hasLicense);  // true (OR)
console.log(!isAdult);               // false (NOT)
```

## 5. Basic Input and Output

### alert():
Displays a popup message to the user.
```javascript
alert("Hello, World!");
```

### prompt():
Asks the user for input.
```javascript
let name = prompt("What's your name?");
console.log("Hello, " + name);
```

### console.log():
Outputs a message to the browser's console.
```javascript
console.log("This is a log message");
console.log("Number:", 42);
```

## 6. Control Structures

### Conditional statements:
```javascript
let age = 20;

if (age < 18) {
  console.log("You're a minor");
} else if (age >= 18 && age < 65) {
  console.log("You're an adult");
} else {
  console.log("You're a senior");
}
```

### Loops:

For loop:
```javascript
for (let i = 0; i < 5; i++) {
  console.log("Iteration " + i);
}
```

While loop:
```javascript
let count = 0;
while (count < 3) {
  console.log("Count is " + count);
  count++;
}
```

Do...while loop:
```javascript
let i = 0;
do {
  console.log("I will run at least once");
  i++;
} while (i < 3);
```

This expanded content provides a more comprehensive introduction to JavaScript, including examples and explanations for each concept. It should serve as a good study guide for beginners starting with JavaScript.

=> JavaScript: Dynamically typed, weakly typed with implicit type coercion. This can lead to unexpected behavior if types are not handled carefully.

=> Python: Dynamically typed, strongly typed, with no implicit type coercion.

# Task
  ### - Task 1: Create a script that asks the user's name using prompt() and greets them with an alert().
  ### - Task 2: Write a program that calculates the sum of two numbers input prompt()  by the user alert().
  ### - Task 3: Use a for loop to display numbers from range of values user put using prompt and print in the console.

## Submit here => https://drive.google.com/drive/folders/13g5kOL_2bq-a4srB4tV2DXy0ihfrh_C9?usp=sharing