# Information on the blog app

Contains the views file where we create different views for various functions of the app.
Then a view is created in the views file and an associated url in the app urls file

To view the shell we just use python manage.py shell
I am using an sqlite db for development
In class meta in the forms file, we create a model that interacts with the user and then we specify the fields which as of this case is from the registration form
Class Meta provides a nested namespace for configurartions and keeps them in place

To use cripsy for styling of the forms, we install it in our environment then add it under installed apps in our settings file then also show its styling still in the same file.

Class based views don't need us to create a forms model to handle the the view other than specifying the fields needed
