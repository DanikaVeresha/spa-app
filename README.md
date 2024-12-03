# SPA-WebApp
Test Task for dZENcode Company 

## This project was developed on the following versions:
#### Operating system: Windows 11 - version: 23H2
#### Framework: Django - version: 3.2.25
#### Database: PostgreSQL
#### Frontend: HTML, CSS
#### Backend: Python - version: 3.11

## 
## How to run the project:
1. Clone the repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. Create a database in PostgreSQL. In terminal of IDE PyCharm enter next commands:
```bash
docker build --tag <name container> .
docker-compose up -d
```
4. Change the database settings in the settings.py file
5. Run the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
6. Open the browser and go to the following link:
```bash
http://127.0.0.1:8000
```
7. Enjoy the project!

## Project structure:
- **webapp** - the main application of the project
- **templates** - the folder with the HTML files
- **manage.py** - the main file for running the project
- **requirements.txt** - the file with the required packages
- **README.md** - the file with the project description
- **.gitignore** - the file with the ignored files
- **.Dockerfile** - the file with the Docker settings
- **.docker-compose.yml** - the file with the Docker Compose settings
- **.env** - the file with the environment variables
- **.env.example** - the example of the .env file
- **.git** - the folder with the git settings
- **.SPAappSettings** - the folder with the settings of the project

## The project was developed by:
- **Name**: Daria Veresha
- **IT_Name**: desh#dD&esh
- **Email**: deshdesh288@gmail.com
- **Phone**: +380 66 605 79 46
- **LinkedIn**: [Daria Veresha](https://www.linkedin.com/in/daria-veresha-a1912b2ba/)
- **GitHub**: [Daria Veresha](https://github.com/DanikaVeresha?tab=repositories)
- **Telegram**: @deshdDiesh992

