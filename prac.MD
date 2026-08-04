## What is DOM Manipulation?

**DOM Manipulation** means **using JavaScript to access and modify the HTML elements of a webpage**.

DOM stands for **Document Object Model**.

When a web page loads, the browser converts the HTML into a tree-like structure called the **DOM**. JavaScript uses this structure to read, update, add, or remove elements dynamically.

### Example HTML

```html
<!DOCTYPE html>
<html>
<body>

<h1 id="heading">Hello World</h1>

<button onclick="changeText()">Click Me</button>

<script src="script.js"></script>

</body>
</html>
```

### JavaScript

```javascript
function changeText() {
    document.getElementById("heading").innerHTML = "Welcome to JavaScript!";
}
```

### Before Clicking

```
Hello World

[ Click Me ]
```

### After Clicking

```
Welcome to JavaScript!

[ Click Me ]
```

Here, JavaScript **changed the content** of the `<h1>` element. This is **DOM Manipulation**.

---

# How DOM Looks Internally

For this HTML:

```html
<html>
  <body>
    <h1>Hello</h1>
    <p>Welcome</p>
  </body>
</html>
```

The DOM tree is:

```
Document
   |
 html
   |
 body
  /   \
 h1    p
 |      |
Hello  Welcome
```

JavaScript can access any node in this tree.

---

# Common DOM Manipulation Methods

## 1. Select an Element

```javascript
document.getElementById("heading");
```

or

```javascript
document.querySelector("#heading");
```

---

## 2. Change Text

```javascript
document.getElementById("heading").innerHTML = "New Text";
```

---

## 3. Change CSS

```javascript
document.getElementById("heading").style.color = "red";
```

---

## 4. Change Background

```javascript
document.body.style.backgroundColor = "lightblue";
```

---

## 5. Change Image

```html
<img id="photo" src="cat.jpg">
```

```javascript
document.getElementById("photo").src = "dog.jpg";
```

---

## 6. Read User Input

HTML

```html
<input type="text" id="name">
```

JavaScript

```javascript
let username = document.getElementById("name").value;

console.log(username);
```

---

## 7. Create a New Element

```javascript
let p = document.createElement("p");

p.innerHTML = "This is a new paragraph.";

document.body.appendChild(p);
```

Before

```
Hello
```

After

```
Hello

This is a new paragraph.
```

---

## 8. Remove an Element

```javascript
document.getElementById("heading").remove();
```

---

## 9. Change HTML Content

```javascript
document.getElementById("demo").innerHTML =
"<h2>Welcome</h2>";
```

---

## 10. Event Handling (DOM + Events)

HTML

```html
<button id="btn">Click</button>
```

JavaScript

```javascript
document.getElementById("btn").addEventListener("click", function () {
    alert("Button Clicked!");
});
```

---

# Real-Life Example: Student Registration Form

Suppose you have this form:

```html
<input type="text" id="name">

<button id="submitBtn">Submit</button>

<p id="result"></p>
```

JavaScript:

```javascript
document.getElementById("submitBtn").addEventListener("click", function () {

    let name = document.getElementById("name").value;

    document.getElementById("result").innerHTML =
        "Welcome " + name;

});
```

### User enters:

```
Rohan
```

After clicking **Submit**, the webpage changes to:

```
Welcome Rohan
```

JavaScript read the input and updated the page **without reloading it**. That's DOM manipulation.

---

# Why is DOM Manipulation Important?

It allows you to build interactive websites by:

* ✅ Reading user input
* ✅ Changing text dynamically
* ✅ Changing colors and styles
* ✅ Creating or deleting elements
* ✅ Showing validation messages
* ✅ Updating tables
* ✅ Building dashboards
* ✅ Creating forms
* ✅ Displaying API data

---

# Summary

**DOM Manipulation = Using JavaScript to access and modify HTML elements dynamically.**

It involves:

* Selecting elements (`getElementById`, `querySelector`)
* Changing content (`innerHTML`, `textContent`)
* Changing styles (`style`)
* Handling user events (`addEventListener`)
* Creating, appending, or removing elements

Since you're learning JavaScript, **DOM Manipulation is the bridge between HTML and JavaScript**. Once you understand it, you'll be able to build interactive web applications like student registration forms, calculators, to-do lists, and dashboards.
