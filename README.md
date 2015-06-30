WEBSITE

**How to Run:**

create Virtual environment using `virtualenv env` and activate by `source env/bin/activate`

Then download the source `git clone http://github.com/rajasimon/website`

```
/Users/simon/Freelancer/
---env
---website
  |__account ( user accounts )
  |__frontend ( Main page and css and js all...)
  |__website ( Actual Project root folder)
  manage.py
  ```

Do the migration `python manage.py migrate`

Run using `python manage.py runserver`

**Note for social login**

add  `/etc/hosts` `website.com:8000`  
  For the facebook
  ```
  export FACEBOOK_KEY=1234556
  export FACEBOOK_SECRET=12352454
  ```

  Same With Google Plus
  ```
  export GOOGLE_KEY=234234234
  export GOOGLE_SECRET=2342342352
  * enable Google plus api in google developer console
  * Redirect URIs	http://website.com:8000/complete/google-oauth2/
  *  JavaScript origins	http://website.com:8000
  ```
