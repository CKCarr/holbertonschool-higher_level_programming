# JavaScript - Web scraping
## Learning Objectives
***
### General
Explain Why JavaScript Programming is Amazing: JavaScript is a versatile and powerful programming language used to create interactive and dynamic websites. You will understand its key features and advantages, such as its ability to run on both client and server-side, its large community support, and its ease of integration with other technologies.
<details>
<summary>Explain Why JavaScript Programming is Amazing:</summary>
<br>
JavaScript is an amazing programming language for several reasons:

- Versatile: JavaScript can be used for both front-end and back-end development, making it a versatile language suitable for creating complete web applications.
- Widely Used: It is one of the most widely used programming languages, and its ecosystem is vast, with a large number of libraries, frameworks, and tools available.
- Easy to Learn: JavaScript has a relatively simple and straightforward syntax, making it accessible to beginners.
- Asynchronous Programming: JavaScript supports asynchronous programming, which allows for non-blocking operations, making it ideal for building responsive web applications.
- Community and Support: The language has a large and active community, making it easy to find resources, tutorials, and help online.
- Cross-Platform: JavaScript can run on various platforms, including web browsers, servers, mobile devices, and even IoT devices.
</details>
<br>

Manipulate JSON Data: JSON (JavaScript Object Notation) is a widely used data format for exchanging and storing data. You will learn how to read, parse, and manipulate JSON data in JavaScript, allowing you to work with APIs and process data effectively.
<details>
<summary>How to Manipulate JSON Data</summary>
<br>
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. To manipulate JSON data, you'll need to understand its basic structure:

- JSON Syntax: JSON consists of key-value pairs and data types, such as strings, numbers, booleans, arrays, and other JSON objects.
- Parsing JSON: To manipulate JSON data in JavaScript, you use JSON.parse() to convert a JSON string into a JavaScript object, allowing you to access and modify the data.
- Modifying JSON: After parsing JSON into a JavaScript object, you can use standard JavaScript operations to modify the object's properties and values.
- Stringifying JSON: To convert a JavaScript object back to a JSON string, use JSON.stringify()
</details>
<br>

Use Request and Fetch API: You will gain the knowledge to work with Request and Fetch APIs in JavaScript, which are used to make HTTP requests and interact with external resources like APIs and servers. This will enable you to retrieve data from remote servers and integrate it into your applications.
<details>
<summary>How to Use Request and Fetch API</summary>
<br>
The Request and Fetch APIs are used for making HTTP requests in JavaScript:

- Request API (Node.js): The Request API is used in Node.js to send HTTP requests to remote servers. It is part of the http or https module and provides a way to interact with servers programmatically.
- Fetch API (Browser): The Fetch API is used in web browsers to make HTTP requests from client-side JavaScript. It is a modern replacement for older methods like XMLHttpRequest and offers a more flexible and promise-based approach to handling requests and responses.
</details>
<br>


Read and Write a File using fs Module: The fs (File System) module in Node.js allows you to work with files on your computer. You will learn how to read data from files, write data to files, and manipulate file content using this module, providing you with the capability to create, modify, and handle files in your projects.
<details>
<summary>How to Read and Write a File Using fs Module</summary>
<br>
The fs module in Node.js allows you to work with the file system and perform file-related operations:

- Reading a File: You can use fs.readFile() to read the contents of a file. It takes the file path and an optional encoding parameter (e.g., 'utf8') to specify the character encoding.
- Writing to a File: To write data to a file, use fs.writeFile(). It takes the file path, the data to be written, and an optional encoding parameter.
- Asynchronous vs. Synchronous: The fs module provides both asynchronous (e.g., fs.readFile(), fs.writeFile()) and synchronous (e.g., fs.readFileSync(), fs.writeFileSync()) versions of these methods. It's generally recommended to use asynchronous methods in Node.js to avoid blocking the event loop.
</details>
<br>

---
#### Getting Started:

Install Node 10

    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs

Install semi-standard

[Documentation](https://github.com/standard/semistandard)

    $ sudo npm install semistandard --global

Install request module and use it

[Documentation](https://github.com/request/request)

    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules

Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

Learning Objectives
In this project, you will learn:

Why JavaScript programming is amazing
How to manipulate JSON data
How to use request and fetch API
How to read and write a file using fs module
Usage
Explain how to use the project, including any specific commands or inputs required to execute different functionalities.

Technologies Used
List the technologies, libraries, and frameworks used in the project. Include versions if applicable.
___
#### File Structure
Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: javascript-web_scraping

###### 0. Readme 
File: 0-readme.js: 
Write a script that reads and prints the content of a file.

The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object

###### 1. Write me 
File: 1-writeme.js
Write a script that writes a string to a file.

The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object

###### 2. Status code 
File: 2-statuscode.js
Write a script that display the status code of a GET request.

The first argument is the URL to request (GET)
The status code must be printed like this: code: \<status code>
You must use the module request

###### 3. Star wars movie title
File: 3-starwars_title.js
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

The first argument is the movie ID
You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
You must use the module request

###### 4. Star wars Wedge Antilles 
File: 4-starwars_count.js
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request

###### 5. Loripsum 
File: 5-request_store.js
Write a script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module request

###### 6. How many completed? 
File: 6-completed_tasks.js
Write a script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module request





