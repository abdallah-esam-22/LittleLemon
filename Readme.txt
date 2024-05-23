to run the virtual environment:
    cd workspace
    Scripts\activate



Restaurant home page:
http://127.0.0.1:8000/restaurant/

Menu API:
http://127.0.0.1:8000/restaurant/menu/
http://127.0.0.1:8000/restaurant/menu/{id}

Table booking API:(for authenticated only)
http://127.0.0.1:8000/restaurant/booking/tables/
http://127.0.0.1:8000/restaurant/booking/tables/{id}

------------------------------------------------------------
Note:
to be authenticated on:
    1- browsable API:
        You should create a superuser and log in django admin.
    2- Insomnia:
        You should get a token and use it.
------------------------------------------------------------
-To register a new user:
    http://127.0.0.1:8000/auth/users/

-To get a Token for an existing user:
    http://127.0.0.1:8000/auth/token/login/
