WEBSITE
How to Run:

create Virtual environment using `virtualenv env` and activate by

`source env/bin/activate`

Then download the source `git clone http://github.com/rajasimon/website`

/Users/simon/Freelancer/
---env
---website
  |__account ( user accounts )
  |__frontend ( Main page and css and js all...)
  |__website ( Actual Project root folder)
  manage.py

Do the migration `python manage.py migrate`

Run using `python manage.py runserver`
