# => CSS Basics: A Comprehensive Guide

## 1. What is CSS? (10  )

CSS (Cascading Style Sheets) is a style sheet language used for describing the presentation of a document written in HTML. 

### Difference between CSS and HTML:
- HTML provides the structure and content of a web page
- CSS controls the layout, styling, and appearance of that content

### CSS role in web development:
- Styling: Controls colors, fonts, spacing, etc.
- Layout: Determines how elements are positioned on the page
- Responsiveness: Allows design adaptation for different screen sizes

## 2. Basic Syntax and Selectors (40  )

### CSS Syntax:
```css
selector {
  property: value;
}
```

### Types of Selectors:

1. Element Selector:
   ```css
   p {
     color: blue;
   }
   ```

2. Class Selector:
   ```css
   .highlight {
     background-color: yellow;
   }
   ```

3. ID Selector:
   ```css
   #header {
     font-size: 24px;
   }
   ```

### Pseudo-classes and Pseudo-elements:

Pseudo-classes:
```css
a:hover {
  color: red;
}

input:focus {
  border-color: blue;
}
```

Pseudo-elements:
```css
p::first-line {
  font-weight: bold;
}

h1::before {
  content: "➤ ";
}
```

## 3. Text Styling and Colors (40  )

### Font Properties:
```css
body {
  font-family: Arial, sans-serif;
  font-size: 16px;
  font-weight: normal;
  text-align: left;
  line-height: 1.5;
}
```

### Color Properties:
```css
.example {
  color: #ff0000;  /* Hex */
  background-color: rgb(68, 87, 3);  /* RGB */
  border-color: hsl(240, 100%, 50%);  /* HSL */
}
```

### Linking CSS:

Internal CSS (within HTML file):
```html
<head>
  <style>
    body {
      background-color: lightgray;
    }
  </style>
</head>
```

External CSS (separate .css file):
```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```
Inline CSS 
```
<p style="color:red; border: 2px solid black;">this is some text</p>
```

## 4. Box Model (40  )

The CSS box model is fundamental to understanding layout in CSS. Every element in web design is a rectangular box.

```css
.box {
  width: 300px;
  padding: 20px;
  border: 2px solid black;
  margin: 10px;
}
```

### Box-sizing Property:
```css
* {
  box-sizing: border-box;
}
```
This ensures padding and border are included in the element's total width and height.

## 5. CSS Layout (40  )

### Display Types:
```css
.block {
  display: block;
}

.inline {
  display: inline;
}

.inline-block {
  display: inline-block;
}
```

### CSS Positioning:
```css
.static {
  position: static;
}

.relative {
  position: relative;
  top: 10px;
  left: 20px;
}

.absolute {
  position: absolute;
  top: 0;
  right: 0;
}

.fixed {
  position: fixed;
  bottom: 0;
  left: 0;
}
```

### Introduction to Flexbox:
```css
.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
```

## 6. Hands-on Activity (50  )

Apply the concepts learned to style the HTML page built on Day 1. Here's a starting point:

```css
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 20px;
  background-color: #f4f4f4;
}

header {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem;
}

nav ul {
  padding: 0;
  list-style-type: none;
}

nav ul li {
  display: inline;
  margin-right: 10px;
}

nav ul li a {
  color: #fff;
  text-decoration: none;
}

main {
  padding: 20px;
  background-color: #fff;
  margin-top: 20px;
}

section {
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
  max-width: 300px;
}

input, button {
  margin-bottom: 10px;
  padding: 5px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid #ddd;
  padding: 10px;
}

img, video, audio {
  max-width: 100%;
}

footer {
  text-align: center;
  padding: 10px;
  background-color: #333;
  color: #fff;
  margin-top: 20px;
}
```

This CSS will provide a basic styled layout for the HTML structure created in Day 1. Encourage students to modify colors, spacing, and layout to understand how changes in CSS affect the appearance of the HTML elements.

## Conclusion

This guide covers the basics of CSS, including its role in web development, syntax, selectors, text styling, the box model, and basic layout techniques. The hands-on activity allows students to apply these concepts practically. Remember, CSS is vast and powerful - this is just the beginning!