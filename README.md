# News Board Backend


## Development environment
- Activate ```_development/docker-compose.yml``` file when you want to work on your local machine.
- Create new venv and install all the requirements from the requirements.txt file


## Project Structure
- Project have one main mini-app(django app). Core
- All API views, serializer and api related stuff live in the api mini-app.

### Usecases
- Every business logic lives under the usecases folders. Every mini-app has its own usecases folder.
- You can simply understand the purpose of the specific usecase by looking its name or description in the class.
- Usecases implemented using profit404/stories library.

### Repositories
- Every db related actions are stored in the repositories. 
- Do not use querysets and db related actions outside of the repositories.
# news-board-api
