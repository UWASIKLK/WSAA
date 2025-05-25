# WSAA - Web Services and Applications
***
This repository contains assignment, labs, my work and final project. 

The purpose of this module was to introduce the different ways of obtaining data from external sources (CSO, weather servers, event information) and in what format the data can arrive (XML, JSON, CSV) and how the data can be retrieved (via API - Application Programmer's Interface) and processed using JavaScript and Python.

Learn how to create own API using the python module Flask to make data available to the outside world.

### Get Started

To get started with this project, you will need to download the necessary software/application in 
case you don't have it:

- **[Python](https://www.python.org/downloads/)** - it is a computer programming language which can be used for various of tasks, like to build website, data analysis and software testing. 

- **[Visual Studio Code](https://visualstudio.microsoft.com/downloads/)** - it is integrated 
development environment (IDE) designed by Microsoft which can be used for writing, editing, 
debugging and building the code.

- **[GitHub](https://github.com/)** - is cloud base platform which allows developers to store, 
manage and share their code. Git is open source and free to use control system which GitHub uses 
for small and large project to track any change you make in GitHub.

- **[WampServer](https://www.wampserver.com/en/)** - WampServer is a Windows web development environment, primary used for building, testing and debugging web applications. It combines Apache(web server), MySQL(database) and PHP(programming language) in a single, easily manageable package.

- **[GitHub Account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)** - to get started with GitHub, you'll need to create a free personal account and verify your email address.

If you want to explore my repositories, you can `clone` the selected repository to your device 
from my link: `git clone https://github.com/UWASIKLK/WSAA.git`. Alternatively, you can create 
`GitHub Codespases` in your existing GitHub account. Here's how: [GitHub Codespaces overview - 
GitHub Docs](https://docs.github.com/en/codespaces/overview)

### Repository

* **mywork** - this directory contains my work during the course following the lectures videos
and lab work.
* **assignments** - this directory contains the practical assignments.
* **project** - this directory contains the final project for this module.

#### Assignments

- **Deal Cards:** Write a program that "deals" (prints) 5 cards and call it "assignment02-carddraw.py". Using the [Deck of Cards API](https://deckofcardsapi.com/) page, this is an API that simulates dealing a deck of cards.

- **CSO Data:** Write a program that retrieves the dataset for the "exchequerAccount (historical series)" from CSO and stores it into a file called "cso.json". Program name: "assignment03-cso.py".

- **Github authorisation:** Write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with your name. The program should then commit those changes and push the file back to the repository. Program name: "assignment04-github.py".

#### Project

Create a Web application in Flask that has a RESTful API, the application should link to one or more database tables. You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data. The full project description is **[here](https://github.com/andrewbeattycourseware/WSAA-Courseware/blob/main/labs/WSAA%20Project%20Description.pdf)**.

I created a "clinic" database with two tables, "doctor" and "patients", inspired by my work in the health insurance industry. The goal of this project was to design a MySQL database capable of storing and managing information about doctors and patients. The backend is developed using Python Flask, which exposes a RESTful API for database interactions. Additionally, a web interface enables users to search, add, and delete records in both the doctors and patients tables.

**Project Structure**

![project structure](/project/static/structure.png)

