# Harvardx CS50 Web programming
## Project 4

Last project of the course. A project made out of deep learning passion. It is designed to be **continuously expanded** and **improved**.

It consists of two servers, one that hosts a deep learning model using tensorflow with gpu support and flask, which communicates with a  server that hosts the django web application.


The application itself is an automatic diagnoser, where a user signs-up/logs-in, then uploads an image of a part of his or her skin lloking for a diagnostic. Then the application returns the image and the corresponding prediction, being:

- Melanoma
- Common Nevu
- Atypical Nevu


The advantage of this method, is that each server handles a specific task. Then it is natural to think, that we could latter implement more models and servers to make the app be able to identify more diseases, and be overall more versatile.

Currently the model works with a test accuracy of 60%, because of the lack of trainning data. But it will suit the purposes of the course. As future work, the model's architecture is going to be improved, and a better dataset is going to be used.

The directory of the deep learning model, the "Tensorflow-server" is as follows:

- checkpoints: A folder that holds the weights file that are loaded onto the tensorflow-model when the server starts.
- application.py: Python script that contains the flask applciation. Here, the model is instantiated, the index route makes sure the model is correctly loaded, and the prediction route does exactly that. Recieves data via post request, makes predictions and then sends back the data.

The django application directory holds the following files and folders:

- detector: The folder that django creates when the __detector__ app is created.
  - migrations: Folder that contains all the changes to the models that django makes when __makemigrations__ is passed to __manage.py__.
  - static: Folder containing all Js, CSS and images used of the design of the front end of the web app.
    - img_post.js: javascript file that sends the form data to the django server, then captures the response data, which is the image and the prediction. Finally, returns false to prevent the page from reloading.
    - form_style.css: Enables flexbox for the container of the image form, ands styles how the other container for the image and prediction appears.
    - register_style.css: The style for the login/register form.
    - cover.css: Styles for the landing page.
    - images: Images for the backgounds of the application.
  - models.py: Contains the definitions for the models used for the application. One for the registration of users, one for the image records, and the other for the diagnostic.
  - forms.py: Contains the form specifications of the apps. It includes a form that overrides the built-in user registration form to include more fields. It also includes a form specification for image form.
  - views.py: Contains how the app is going to interact between views. One in particular is the __upload__ which recieves the image dat from the form, then sends to the tensorflow server the info. Finally it gets back the information and saves everything on the database.
  - The other scripts are created by django to manage the urls and other aspects.
- media: Folder that will contain all images uploaded by users.
- project4: The folder created by django when the project was created. Contains url, settings and other  scripts to manage the project.
- templates: HTML files corresponding to the web pages of the project.
- manage.py: Script that djnago uses to make migrations, migrate and start the server.

