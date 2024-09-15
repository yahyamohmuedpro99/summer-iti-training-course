# Day 3: Arrays, Objects, and Advanced DOM Manipulation in JavaScript

## Objectives:
* Use arrays and objects to store and manage data.
* Perform advanced DOM manipulation tasks.
* Understand how to create and remove HTML elements dynamically.

## 1. Arrays

Arrays are used to store multiple values in a single variable.

### Creating arrays:

```javascript
let fruits = ['apple', 'banana', 'orange'];
let numbers = new Array(1, 2, 3, 4, 5);
```

### Accessing and modifying elements:

```javascript
console.log(fruits[0]); // Output: 'apple'
fruits[1] = 'grape';
console.log(fruits); // Output: ['apple', 'grape', 'orange']
```

### Array methods:

1. `push()` and `pop()`:
   ```javascript
   fruits.push('mango'); // Adds to the end
   console.log(fruits); // ['apple', 'grape', 'orange', 'mango']
   
   let lastFruit = fruits.pop(); // Removes from the end
   console.log(lastFruit); // 'mango'
   console.log(fruits); // ['apple', 'grape', 'orange']
   ```

2. `shift()` and `unshift()`:
   ```javascript
   fruits.unshift('kiwi'); // Adds to the beginning
   console.log(fruits); // ['kiwi', 'apple', 'grape', 'orange']
   
   let firstFruit = fruits.shift(); // Removes from the beginning
   console.log(firstFruit); // 'kiwi'
   console.log(fruits); // ['apple', 'grape', 'orange']
   ```

3. `splice()`:
   ```javascript
   fruits.splice(1, 1, 'pear', 'melon');
   console.log(fruits); // ['apple', 'pear', 'melon', 'orange']
   ```

4. `slice()`:
   ```javascript
   let citrus = fruits.slice(2);
   console.log(citrus); // ['melon', 'orange']
   ```

5. `forEach()`:
   ```javascript
   fruits.forEach(function(fruit) {
     console.log(fruit);
   });
   ```

6. `map()`:
   ```javascript
   let upperFruits = fruits.map(function(fruit) {
     return fruit.toUpperCase();
   });
   console.log(upperFruits); // ['APPLE', 'PEAR', 'MELON', 'ORANGE']
   ```

7. `filter()`:
   ```javascript
   let longFruits = fruits.filter(function(fruit) {
     return fruit.length > 4;
   });
   console.log(longFruits); // ['apple', 'melon', 'orange']
   ```

## 2. Objects

Objects are used to store collections of data and more complex entities.

### Defining objects with properties and methods:

```javascript
let person = {
  firstName: "John",
  lastName: "Doe",
  age: 30,
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};
```

### Accessing object properties:

```javascript
// Dot notation
console.log(person.firstName); // 'John'

// Bracket notation
console.log(person['lastName']); // 'Doe'

// Calling a method
console.log(person.fullName()); // 'John Doe'
```

### Object constructors and prototypes:

```javascript
function Car(make, model, year) {
  this.make = make;
  this.model = model;
  this.year = year;
}

Car.prototype.getInfo = function() {
  return this.year + " " + this.make + " " + this.model;
};

let myCar = new Car("Toyota", "Corolla", 2020);
console.log(myCar.getInfo()); // '2020 Toyota Corolla'
```

## 3. Advanced DOM Manipulation

### Creating new elements:

```javascript
let newDiv = document.createElement('div');
newDiv.textContent = 'This is a new div';
```

### Appending elements:

```javascript
// Append to the end of an element
document.body.appendChild(newDiv);

// Insert before a specific element
let existingElement = document.getElementById('existingElement');
document.body.insertBefore(newDiv, existingElement);
```

### Removing elements:

```javascript
let parentElement = document.getElementById('parent');
let childElement = document.getElementById('child');
parentElement.removeChild(childElement);
```

### Cloning nodes:

```javascript
let original = document.getElementById('original');
let clone = original.cloneNode(true); // true for deep clone (includes children)
document.body.appendChild(clone);
```

## 4. Traversing the DOM

### Parent, child, and sibling relationships:

```javascript
let element = document.getElementById('myElement');

// Parent
let parent = element.parentNode;

// Children
let children = element.childNodes;
let firstChild = element.firstChild;
let lastChild = element.lastChild;

// Siblings
let nextSibling = element.nextSibling;
let previousSibling = element.previousSibling;
```

### Navigating the DOM tree:

```javascript
// Get all paragraphs in the document
let paragraphs = document.getElementsByTagName('p');

// Get all elements with a specific class
let highlights = document.getElementsByClassName('highlight');

// Get the first element that matches a CSS selector
let firstButton = document.querySelector('button');

// Get all elements that match a CSS selector
let allButtons = document.querySelectorAll('button');
```

### Practical Example: Creating a Dynamic List

Let's put it all together with a practical example that uses arrays, objects, and DOM manipulation:

```javascript
// Array of objects
let books = [
  { title: "The Great Gatsby", author: "F. Scott Fitzgerald" },
  { title: "To Kill a Mockingbird", author: "Harper Lee" },
  { title: "1984", author: "George Orwell" }
];

// Function to create and append list items
function createBookList() {
  let ul = document.createElement('ul');
  
  books.forEach(function(book) {
    let li = document.createElement('li');
    li.textContent = `${book.title} by ${book.author}`;
    ul.appendChild(li);
  });
  
  document.body.appendChild(ul);
}

// Call the function to create the list
createBookList();
```

This example demonstrates how to use an array of objects, iterate over it, create new DOM elements, and append them to the document.

Remember, practice is key to mastering these concepts. Try modifying the examples and creating your own scripts to reinforce your learning.


# Task 
Task 1: Create an array of student names and display them in a list on a webpage.
Task 2: Build a to-do list application where users can add and remove tasks.
Task 3: Create an object representing a person and display their details on the page.


## Submit here => https://drive.google.com/drive/folders/13X1NqqIlr_5BgRd_sP3zQheEnVWqwVEl?usp=sharing