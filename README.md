1. Clone git repo and cd to edgetest/
2. Install Pip and virtualenvwrapper
3. Create new virtualenv in python3

    mkvirtualenv --python=/usr/bin/python3 edge

4. Run requirements.txt

   	pip install -r requirements.txt

5. Run collectstatic 

   ./manage.py collectstatic

7. Finally, run

   ./manage.py runserver

and go to http://127.0.0.1:8000/ in a browser
