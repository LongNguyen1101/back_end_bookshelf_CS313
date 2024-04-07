# Bookshelf Backend

This is the backend of the bookshelf project, which provides APIs and database management for a web app that allows users to browse and buy books online. We made this project as a way to learn more about e-commerce and to share our love for reading. 📚

🛠 *This repo is still in the development stage. Some features may not work well or may change in the future.*

## Contributors

1. [Bùi Lê Khánh Linh](https://github.com/blkhanhlinh) - Leader / Front-end / Design / Document

## Installation

1. Create a virtual environment
```sh
py -m venv env
```

2. Activate the virtual env
(windows)
```sh
.\env\Scripts\activate
```
(macos & linux)
```sh
source env/bin/activate
```

3. Install dependencies
```sh
pip install -r library.txt

```

4. Run migrations 

If you make changes in the models.py file, then run the following commands:

```sh
py manage.py makemigrations
py manage.py migrate
```

5. If you want to delete the data in the database while keeping the structure of the database intact, use this command:
```sh
py manage.py flush
```

6. If you want to insert data to database, use this commands:
```sh
py manage.py import_data
```

If you want to edit the data added to the database, go to the file: playground/data
If you want to edit how the data is added, go to the file: playground/management/commands/import_data.py
Then run: py manage.py flush && py manage.py import_data

7. Run the server
```sh
py manage.py runserver
```