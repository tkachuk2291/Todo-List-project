# Todo-List-project


This project is a web application for managing to-do lists, developed using the Django framework.

The main goal of the application is to assist users in organizing and managing their tasks. Users can create new tasks, set deadlines for them, mark them as completed or incomplete, and assign tags to them for easier classification.




## Installing / Getting started

> 👉 Download the code  

```shell
git clone https://github.com/tkachuk2291/Todo-List-project.git
cd LiveBlog
```

<br />

> 👉 Install modules via `VENV`  

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```shell
python manage.py makemigrations
python manage.py migrate
```

<br />

> 👉 Create the Superuser

```shell
python manage.py createsuperuser 
```
```
Or login with default SuperUser:  
Login: Author
Password: Authortest2291
```
<br />

> 👉 Start the app

```shell
 python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 



## Features

**Home Page:**  
Implemented a home page accessible at 127.0.0.1:8000/.
Added a sidebar on all pages with links to the home page and the tags list page.
The home page displays a list of tasks (Todo list), sorted from incomplete to complete and from newest to oldest.
Each task displays its content, along with buttons for editing and deleting.
Added the ability to add a new task.
For each task, buttons "Complete" and "Undo" are added, which change the task status and redirect to the same page.  

**Tags:**  

Created a page with a list of tags, accessible via the sidebar on all pages.
The tags list page displays all available tags.
Each tag is represented by its name.
For each tag, tasks can be added or removed accordingly.
Implemented functionality for adding new tags to tasks and deleting them.

## Contributing

If you're interested in contributing, simply fork the repository and create a feature branch.  
We appreciate all contributions and warmly welcome pull requests.  

## Links

- Repository: https://github.com/tkachuk2291/Todo-List-project
- Issue tracker: https://github.com/tkachuk2291/Todo-List-project/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    tkacuk2291@gmail.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!

  