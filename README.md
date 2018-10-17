# Book Share
Book share is `Peer to Peer` lending application that help book lovers to add and borrow books from other peers

## Requirements
    - python3
    - postgresSQL Databse Engine
    - Pipenv

# Installation  ##

1. Clone the Github repo to your machine 
    ``` git clone https://github.com/frankip/book-share.git ```

2. change the directory to the project by 

    ``` cd book_share ```

3. change to the active branch

    ``` git checkout development ```

4. Setup a virtual enviroment

    - Install pipenv

        ```brew install pipenv ```

    - Install dependencies:
        ``` pipenv install ```

    - Install dev dependencies to setup development environment
        ``` pipenv install --dev ```

    - Activate a virtual environment:
        ``` pipenv shell ```
    
5. Update .env file
    ```
    export FLASK_ENV="dev" 
    export DATABASE_URI="postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_DATABASE_NAME"
    export TEST_DATABASE_URI="postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_TEST_DATABASE_NAME" 
    export API_BASE_URL_V1="/api/v1"
    export SECRET_KEY="Some good random string"
    export FLASK_DEBUG=1
    export FLASK_APP=main

    ```

6. Apply migrations:
    ```flask db upgrade```

7. Start the application
    ``` flask run```