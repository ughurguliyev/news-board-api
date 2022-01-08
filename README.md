# News Board Backend


## Set up development environment
- Activate ```_development/docker-compose.yml``` file when you want to work on your local machine:
```bash
$ docker-compose up -d --build 
 
```
- Create new venv and install all the requirements from the requirements.txt file:
```bash
$ python3 -m venv venv 
$ source venv/bin/activate 
$ pip3 install -r requirements.txt

```
- Enter app folder and apply migrations:
```bash
$ python3 manage.py makemigrations 
$ python3 manage.py migrate 

```
- Finally start up the server:
```bash
$ python3 manage.py runserver 

```

## Project Structure
- Project have one main mini-app(django app) - core
- All API views, serializer and api related stuff live in the api mini-app.

### Usecases
- Every business logic lives under the usecases folders.
- You can simply understand the purpose of the specific usecase by looking its name or description in the class.
- Usecases implemented using profit404/stories ("https://github.com/proofit404/stories") library.
- Celery & Redis used to reset upvote count daily at 00:00 asynchronously.

### Repositories
- Every db related actions are stored in the repository. 
- Do not use querysets and db related actions outside of the repository.

## Postman Documentation and Collection
- https://documenter.getpostman.com/view/17377284/UVXerdT7 (Documentation)
- https://www.postman.com/grey-crescent-804077/workspace/news-board-api/collection/17377284-1ce2152c-e57a-4ec8-b38d-e9ce6d0ef5b5?ctx=documentation (Collection)

## Extra infos
- Deployed project url: http://161.35.198.20/
- Superuser login and password: admin && admin1234


