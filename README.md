# Photo_album

# Flask Project Template



## How to Run

### Step 1: Get the Python file

### Git

Clone this repository
```sh
git clone https://github.com/UddavMagar/photo_album.git
```

### Step 2: Navigate to the Project Folder
Go to the newly created project folder: 

```sh
cd photo_album
```

### Step 3: Create and Activate a Virtual Environment
Create a virtual environment in the project folder and activate it:

On Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```sh
python3 -m venv venv
source venv/bin/activate
```


### Step 4: Install Requirements
Install the required packages listed in requirements.txt:

```sh
pip install -r requirements.txt
```

### Step 5: To Initialize and Migrate the Database
To initialize your database, use the following command:

```sh
flask db init
```
To migrate your database, use the following commands:
```sh
flask db migrate
flask db upgrade
```
Whenever you make changes to your models, run these commands to apply the changes to your database smoothly.

### Step 6: Run the Flask Application
Run the application:

```sh
python run.py
```
You should see your Flask web application running, where you can start building and expanding your own photo album.

## Description

### Photo Album: A Flask Application for Uploading and Viewing Images

This project is a web application built using Flask, designed to allow users to upload and view their photos. The main features of this application include:

* **User-Friendly Interface:** Simple and intuitive interface for uploading and browsing images.
* **Photo Upload:** Users can easily upload photos to the application.
* **Image Gallery:** Displays uploaded images in a gallery format for easy viewing.
* **Database Integration:** Utilizes SQLAlchemy for managing image metadata and storage paths.
* **Secure Access:** Implements user authentication using Flask-Login and encryption with Flask-Bcrypt to ensure secure access to personal photo albums.
* 
The project is structured to provide a clean and organized codebase, facilitating easy maintenance and scalability. This application serves as a great starting point for anyone looking to build more complex image management systems or simply as a personal photo album.

### Key Technologies Used:
* **Flask:** Web framework for building the application.
* **SQLAlchemy:** ORM for database interactions.
* **Flask-Migrate:** For handling database migrations.
* **Flask-Login:** For managing user authentication.
* **Flask-Bcrypt:** For encrypting user passwords.
* **Flask-WTF:** For form handling and validation.

