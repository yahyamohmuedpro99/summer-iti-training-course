# Day 5: Asynchronous JavaScript and Final Project

## Objectives:
* Understand the concept of asynchronous programming in JavaScript.
* Learn how to fetch data from external APIs.
* Apply all learned concepts in a mini-project.

## 1. Asynchronous JavaScript

Asynchronous programming allows JavaScript to perform long-running tasks without blocking the main thread, ensuring that the application remains responsive.

### Callbacks:

Callbacks are functions passed as arguments to other functions, to be executed once an asynchronous operation has completed.

```javascript
function fetchData(callback) {
  setTimeout(() => {
    const data = { id: 1, name: 'John Doe' };
    callback(data);
  }, 2000);
}

fetchData((result) => {
  console.log(result);
});
```

However, nested callbacks can lead to "callback hell":

```javascript
fetchUserData((user) => {
  fetchUserPosts(user.id, (posts) => {
    fetchPostComments(posts[0].id, (comments) => {
      // Deeply nested and hard to read
    });
  });
});
```

### Promises:

Promises provide a cleaner way to handle asynchronous operations.

```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = true;
      if (success) {
        resolve({ id: 1, name: 'John Doe' });
      } else {
        reject('Error fetching data');
      }
    }, 2000);
  });
}

fetchData()
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

Chaining promises helps avoid callback hell:

```javascript
fetchUserData()
  .then(user => fetchUserPosts(user.id))
  .then(posts => fetchPostComments(posts[0].id))
  .then(comments => console.log(comments))
  .catch(error => console.error(error));
```

### Async/Await:

Async/await provides a more synchronous-looking way to write asynchronous code.

```javascript
async function fetchUserDataAndPosts() {
  try {
    const user = await fetchUserData();
    const posts = await fetchUserPosts(user.id);
    const comments = await fetchPostComments(posts[0].id);
    console.log(comments);
  } catch (error) {
    console.error(error);
  }
}

fetchUserDataAndPosts();
```

## 2. Fetching Data from APIs

The Fetch API provides a powerful and flexible way to make HTTP requests.

### Using the Fetch API:

```javascript
// GET request
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

// POST request
fetch('https://api.example.com/post', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ key: 'value' }),
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### Using Async/Await with Fetch:

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
```

## 3. Mini-Project: Building a Weather App

Let's apply what we've learned by building a simple weather app that fetches data from a public API.

### Project Structure:

```
weather-app/
│
├── index.html
├── style.css
└── script.js
```

### HTML (index.html):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Weather App</h1>
        <input type="text" id="cityInput" placeholder="Enter city name">
        <button id="searchBtn">Search</button>
        <div id="weatherInfo"></div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

### CSS (style.css):

```css
body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background-color: #f0f0f0;
}

.container {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

input, button {
    margin: 10px 0;
    padding: 5px;
}

#weatherInfo {
    margin-top: 20px;
}
```

### JavaScript (script.js):

```javascript
const API_KEY = 'your_api_key_here';
const API_URL = 'https://api.openweathermap.org/data/2.5/weather';

const cityInput = document.getElementById('cityInput');
const searchBtn = document.getElementById('searchBtn');
const weatherInfo = document.getElementById('weatherInfo');

async function getWeather(city) {
    try {
        const response = await fetch(`${API_URL}?q=${city}&appid=${API_KEY}&units=metric`);
        if (!response.ok) {
            throw new Error('City not found');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        throw error;
    }
}

function displayWeather(data) {
    const { name, main, weather } = data;
    weatherInfo.innerHTML = `
        <h2>${name}</h2>
        <p>Temperature: ${main.temp}°C</p>
        <p>Feels like: ${main.feels_like}°C</p>
        <p>Humidity: ${main.humidity}%</p>
        <p>Weather: ${weather[0].description}</p>
    `;
}

searchBtn.addEventListener('click', async () => {
    const city = cityInput.value.trim();
    if (city) {
        try {
            weatherInfo.innerHTML = 'Loading...';
            const data = await getWeather(city);
            displayWeather(data);
        } catch (error) {
            weatherInfo.innerHTML = `Error: ${error.message}`;
        }
    } else {
        weatherInfo.innerHTML = 'Please enter a city name';
    }
});
```

This mini-project demonstrates:
1. Asynchronous programming with async/await
2. Fetching data from an external API (OpenWeatherMap in this case)
3. DOM manipulation to update the UI
4. Error handling for network requests and user input
5. Event handling for user interactions

To use this app, you'll need to sign up for a free API key at OpenWeatherMap and replace `'your_api_key_here'` in the script with your actual API key.

This weather app serves as a practical application of the concepts learned throughout the course, including:
- ES6 features (arrow functions, template literals, destructuring)
- Asynchronous JavaScript (Fetch API, async/await)
- DOM manipulation
- Event handling
- Error handling

By building and extending this project, you can reinforce your understanding of JavaScript and explore more advanced features and APIs.

# Task
Task 1: Write a function that fetches data from an API and logs it to the console.
Task 2: Modify the function to display data on the webpage.
Task 3: Complete the mini-project by adding styling and additional features


## Submit here => 
https://drive.google.com/drive/folders/1DvGqail4Jft9r9X1C7KAnXy2dqEkcUwk?usp=sharing