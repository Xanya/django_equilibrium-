To run the project you just need to follow these steps:

Linux:
1. python3 -m venv venv
2. source venv/bin/activate
3. If you're using regular pip then: "pip install -r requirements"; but if you use poetry then: "poetry install"
4. python3 manage.py migrate
5. python3 manage.py runserver

Windows:
1. python -m venv venv
2. . venv/Scripts/activate
3. If you're using regular pip then: "pip install -r requirements"; but if you use poetry then: "poetry install"
4. python manage.py migrate
5. python manage.py runserver

Short description:
I've included the Equilibrium Index solution in equilibrium_index file in the root of the project. I used django-image-cropping and ease-thumbnails to allow the image cropping from the admin, used CKeditor to allow formatting of the text. The rest features is pretty simple