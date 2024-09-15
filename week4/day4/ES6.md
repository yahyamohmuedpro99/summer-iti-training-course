# Day 4: Form Validation and ES6 Features in JavaScript

## Objectives:
* Validate form inputs using JavaScript.
* Learn modern JavaScript features introduced in ES6.
* Write cleaner and more efficient code using new syntax.

## 1. Form Validation

Form validation is crucial for ensuring that user input meets the required criteria before being submitted to the server.

### Accessing form elements:

```javascript
let form = document.getElementById('myForm');
let username = document.getElementById('username');
let email = document.getElementById('email');
```

### Validating text fields, email, phone numbers, and passwords:

```javascript
function validateForm() {
  // Username validation
  if (username.value.trim() === '') {
    showError(username, 'Username cannot be blank');
  } else if (username.value.length < 3) {
    showError(username, 'Username must be at least 3 characters');
  } else {
    showSuccess(username);
  }

  // Email validation
  if (email.value.trim() === '') {
    showError(email, 'Email cannot be blank');
  } else if (!isValidEmail(email.value)) {
    showError(email, 'Email is not valid');
  } else {
    showSuccess(email);
  }

  // Phone number validation
  if (phone.value.trim() === '') {
    showError(phone, 'Phone number cannot be blank');
  } else if (!isValidPhone(phone.value)) {
    showError(phone, 'Phone number is not valid');
  } else {
    showSuccess(phone);
  }

  // Password validation
  if (password.value.trim() === '') {
    showError(password, 'Password cannot be blank');
  } else if (password.value.length < 6) {
    showError(password, 'Password must be at least 6 characters');
  } else {
    showSuccess(password);
  }
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function isValidPhone(phone) {
  return /^\d{10}$/.test(phone);
}
```

### Providing user feedback:

```javascript
function showError(input, message) {
  const formControl = input.parentElement;
  formControl.className = 'form-control error';
  const small = formControl.querySelector('small');
  small.innerText = message;
}

function showSuccess(input) {
  const formControl = input.parentElement;
  formControl.className = 'form-control success';
}
```

### Preventing form submission on validation failure:

```javascript
form.addEventListener('submit', function(e) {
  e.preventDefault();
  validateForm();
});
```

## 2. Introduction to ES6

ES6 (ECMAScript 2015) introduced many new features to JavaScript that make the language more powerful and expressive.

### Let and Const:

`let` and `const` provide block-scoping, unlike `var` which is function-scoped.

```javascript
// let allows reassignment
let count = 1;
count = 2; // This is fine

// const prevents reassignment
const PI = 3.14159;
// PI = 3.14; // This would throw an error

// Block scoping
if (true) {
  let blockScoped = 'I am block-scoped';
  var functionScoped = 'I am function-scoped';
}
// console.log(blockScoped); // This would throw an error
console.log(functionScoped); // This works
```

### Arrow Functions:

Arrow functions provide a more concise syntax for writing function expressions.

```javascript
// Traditional function
function add(a, b) {
  return a + b;
}

// Arrow function
const addArrow = (a, b) => a + b;

// Arrow function with single parameter
const square = x => x * x;

// Arrow function with no parameters
const sayHello = () => console.log('Hello!');

// Arrow functions and 'this'
const person = {
  name: 'John',
  greet: function() {
    setTimeout(() => {
      console.log(`Hello, my name is ${this.name}`);
    }, 1000);
  }
};
```

### Template Literals:

Template literals allow for easier string interpolation and multi-line strings.

```javascript
const name = 'John';
const age = 30;

// String interpolation
console.log(`My name is ${name} and I am ${age} years old.`);

// Multi-line strings
const multiLine = `
  This is a
  multi-line
  string.
`;
```

### Destructuring Assignment:

Destructuring allows you to extract values from arrays or properties from objects into distinct variables.

```javascript
// Array destructuring
const numbers = [1, 2, 3];
const [first, second, third] = numbers;

// Object destructuring
const person = { name: 'John', age: 30 };
const { name, age } = person;

// Destructuring with different variable names
const { name: personName, age: personAge } = person;
```

### Spread and Rest Operators:

The spread operator (...) allows an iterable to be expanded in places where zero or more arguments or elements are expected.

```javascript
// Spread operator with arrays
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]

// Spread operator with objects
const obj1 = { x: 1, y: 2 };
const obj2 = { ...obj1, z: 3 }; // { x: 1, y: 2, z: 3 }

// Rest parameter in functions
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}
console.log(sum(1, 2, 3, 4)); // 10
```

### Default Parameters:

Default parameters allow you to specify default values for function parameters.

```javascript
function greet(name = 'Guest') {
  console.log(`Hello, ${name}!`);
}

greet(); // "Hello, Guest!"
greet('John'); // "Hello, John!"
```

## Practical Example: Form Validation with ES6 Features

Let's combine form validation with some ES6 features:

```javascript
const form = document.getElementById('myForm');
const inputs = [...document.querySelectorAll('input')];

const validateInput = ({ id, value }) => {
  switch (id) {
    case 'username':
      return value.length >= 3 ? null : 'Username must be at least 3 characters';
    case 'email':
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) ? null : 'Invalid email format';
    case 'password':
      return value.length >= 6 ? null : 'Password must be at least 6 characters';
    default:
      return null;
  }
};

const showFeedback = (input, error) => {
  const formControl = input.parentElement;
  formControl.className = `form-control ${error ? 'error' : 'success'}`;
  const small = formControl.querySelector('small');
  small.innerText = error || '';
};

form.addEventListener('submit', (e) => {
  e.preventDefault();
  
  const errors = inputs.map(input => ({
    input,
    error: validateInput(input)
  }));

  errors.forEach(({ input, error }) => showFeedback(input, error));

  const isValid = errors.every(({ error }) => !error);
  if (isValid) {
    console.log('Form submitted successfully!');
    // Here you would typically send the form data to a server
  }
});
```

This example demonstrates how ES6 features like arrow functions, destructuring, spread operator, and template literals can be used to create more concise and readable code for form validation.

Remember to practice these concepts by modifying the examples and creating your own scripts. This will help reinforce your understanding of both form validation techniques and ES6 features.

# Task
Task 1: Create a registration form with validation for each input field.
Task 2: Refactor previous functions using arrow function syntax.
Task 3: Use template literals to create a dynamic HTML snippet.


## Submit here => https://drive.google.com/drive/folders/1XsdS_BmakQCFncz2M60vxCt2VQArouXS?usp=sharing
