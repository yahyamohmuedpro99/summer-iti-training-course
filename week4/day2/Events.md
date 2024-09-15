# Day 2: Functions and Event Handling in JavaScript

## Objectives:
* Understand and create functions.
* Learn how to handle events to make web pages interactive.
* Manipulate the Document Object Model (DOM) to change HTML content dynamically.

## 1. Functions

Functions are reusable blocks of code that perform specific tasks. They are fundamental to JavaScript programming.

### Defining functions using `function` keyword:

```javascript
function greet(name) {
    console.log("Hello, " + name + "!");
}

greet("Alice"); // Output: Hello, Alice!
```

### Function expressions:

Functions can also be assigned to variables:

```javascript
const square = function(x) {
    return x * x;
};

console.log(square(4)); // Output: 16
```

### Arrow functions (ES6+):

A more concise way to write function expressions:

```javascript
const cube = (x) => x * x * x;

console.log(cube(3)); // Output: 27
```

### Parameters and return values:

Functions can accept parameters and return values:

```javascript
function add(a, b) {
    return a + b;
}

let result = add(5, 3);
console.log(result); // Output: 8
```

### Scope of variables:

Variables declared inside a function are only accessible within that function (local scope):

```javascript
function exampleScope() {
    let localVar = "I'm local";
    console.log(localVar); // Accessible
}

exampleScope();
// console.log(localVar); // This would cause an error
```

Variables declared outside functions have global scope:

```javascript
let globalVar = "I'm global";

function accessGlobal() {
    console.log(globalVar); // Accessible
}

accessGlobal();
```

## 2. Event Handling

Events are actions or occurrences that happen in the system you are programming, which the system tells you about so you can respond to them.

### What are events?

Events can be user actions (clicks, key presses) or system occurrences (page loaded, error occurred).

### Common events:

- `click`: When an element is clicked
- `mouseover`: When the mouse moves over an element
- `mouseout`: When the mouse moves out of an element
- `change`: When the value of an input element changes
- `submit`: When a form is submitted

### Inline event handling:

You can add event handlers directly in HTML:

```html
<button onclick="alert('Button clicked!')">Click me</button>
```

### Adding event listeners:

A more flexible way to handle events in JavaScript:

```javascript
let button = document.getElementById('myButton');
button.addEventListener('click', function() {
    alert('Button clicked!');
});
```

This method allows multiple event handlers for the same event and easier removal of event listeners.

## 3. DOM Manipulation Basics

The Document Object Model (DOM) is a programming interface for HTML and XML documents. It represents the structure of a document as a tree-like hierarchy.

### The DOM tree structure:

```
document
└── html
    ├── head
    │   ├── title
    │   └── meta
    └── body
        ├── h1
        ├── p
        └── div
            └── span
```

### Selecting elements:

```javascript
// By ID
let header = document.getElementById('main-header');

// By class name
let paragraphs = document.getElementsByClassName('content');

// By CSS selector
let firstParagraph = document.querySelector('p');
let allLinks = document.querySelectorAll('a');
```

### Changing content:

```javascript
// Using innerHTML (can include HTML tags)
document.getElementById('myDiv').innerHTML = '<strong>New content!</strong>';

// Using textContent (plain text only)
document.getElementById('myParagraph').textContent = 'Updated text';
```

### Modifying styles:

```javascript
let element = document.getElementById('myElement');
element.style.color = 'blue';
element.style.fontSize = '20px';
```

## 4. Timing Events

JavaScript can execute code at specified time intervals.

### setTimeout():

Executes a function once after a specified delay:

```javascript
setTimeout(function() {
    console.log("This message appears after 3 seconds");
}, 3000); // 3000 milliseconds = 3 seconds
```

### setInterval():

Repeatedly executes a function with a fixed time delay between each call:

```javascript
let counter = 0;
let intervalId = setInterval(function() {
    console.log("Counter: " + counter);
    counter++;
    if (counter > 5) {
        clearInterval(intervalId); // Stop the interval after 5 iterations
    }
}, 1000); // Runs every 1000 milliseconds (1 second)
```

Remember to use `clearInterval()` to stop the interval when it's no longer needed.

# Task
Task 1: Write a function that takes a number as an argument and returns its square.
Task 2: Create a simple webpage with a button that changes the background color of the page when clicked.
Task 3: Build an image gallery where hovering over thumbnails displays a larger version.


## Submit here => https://drive.google.com/drive/folders/1tfNrmVIiiFWKf5KksQ3sbcNk6DyzB-3C?usp=sharing