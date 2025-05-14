# Facial Recognition

A facial recognition app with capabilities of identifying people and sending alerts 

## Description

* Show readme.md information
* Register and login of users
* Very simple and easy to use interface

## Characteristics

* **Auth**: Register and login with `django.contrib.auth`.
* **Markdown**: Loading and rendering of `README.md` on HTML.
* **Responsive**: Adaptive to mobile displays with CSS simple.

## Install instructions

1. Clone the repository

   ```bash
   git clone https://github.com/bbBerny/facial-recognition.git
   cd facial-recognition
   ```
2. Create and activate a virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:

   ```bash
   python manage.py migrate
   ```
5. Run the server:

   ```bash
   python manage.py runserver
   ```

## Use

* Open on your browser `http://localhost:8000/`.
* If you do not have an account click on **Register**.
* Once authenticated you will be able to use the app.


## 🛠 Technologies

* Python 3.13.3
* Django 5.2.1
* markdown2
* HTML5 & CSS3
* OpenCV
* Numpy
