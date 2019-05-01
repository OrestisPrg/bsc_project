In order to run the web application, Python 3 and a specific set of dependencies is needed.  
The dependencies can be installed in a virtual environment or directly onto the user’s machine although it is recommended to use a virtual environment.  
After downloading the source code from the GitLab repository follow the specific instructions depending if you are using a virtual environment or not.  
This guide assumes the user is working on a Linux machine.  

To create a virtual environment and install the dependencies in the virtual environment, execute the following commands in a terminal where the “hackhub” directory downloaded is located:

*  `python -m venv env`    Creates a virtual environment named “env”
*  `source env/bin/activate`   Activates the virtual environment
*  `pip install django`   Installs Django
*  `pip install django-crispy-forms`  Installs crispy forms
*  `pip install image`  Installs image
  
if you do not wish to work in a virtual environment you can just install django, django-crispy-forms & image directly on your machine.  
  
  
Once you have completed the above steps navigate inside the directory “hack_app” located in “hackhub” from the terminal.  
You should see the “manage.py” file in the “hack_app” directory. In the terminal window type the following command:  

    
*  `python manage.py runserver` Activates the web server to host the web application on localhost

The above command will activate Django’s web server which will host the web application on localhost.
To access the web application, in a web browser type “localhost” in the navigation bar and press enter.

You can login as administrator using the following credentials:
*  Username: hackhub
*  Password: admin2019
      
  
The virtual machine image for Kali Linux is available at: https://www.dropbox.com/sh/pwh3qrqlke5gc6h/AACaYZW8jjmiLX1mG_ziGl-Wa?dl=0 