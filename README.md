This is a basic sqlalchemy + mysql + pymysql + alembic setup project with minimal boiler plate code.

How to start
-------------
1. Make sure your system has docker desktop installed.
2. Clone and open this project in any code editor.
3. Run command **docker-compose up --build** from root directory of the project.
4. There you have your setup running !


Alembic Usage Guide
-----------------
1. Go inside docker container using **docker exec -it python_app bash**
2. Run **alembic upgrade head** command to upgrade your DB to latest migration revision.
3. Run command **alembic current** to get current revision ID of the DB.
4. Remove/Unapply changes in DB using command **alembic downgrade -\<no of migration revision to downgrade>** example: **alembic downgrade -1** will remove the changes from the latest migration revision from the Database.

    Detect Changes and upgrade DB
    -----------------------------
    1. Make any model class that inherits **Base** from **main.py** module inside **models/** directory (example of user model is kept for reference).
    2. Import newly created model Class into **\__init__.py** file inside **models/** directory.
    3. Go inside docker container from terminal then,
    run command **alembic revision --autogenerate -m \<file name>** this will create a new migration file detecting the new model that was made / changes to existing model.
    4. Verify the migration file generated inside **alembic/versions** directory and to apply the migration changes into the DB run command **alembic upgrade head**  

