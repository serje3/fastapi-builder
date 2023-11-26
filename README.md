# Build system microservice FastApi

### Description

FastApi microservice written on Python 3.10

### Installation

#### Docker-Compose
```shell
docker-compose up -d
```

#### Windows
```shell
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
#### Linux/Mac Os
```shell
pip install -r requirements.txt
uvicorn app.main:app --reload
```
### Documentation

There is only one API POST method ```/tasks/get_by_build```, 
that accepts JSON 
```json
{
  "build": "string"
}
```

### Testing
To test the application, the pytest module is used here.
Tests written in the "tests" folder

You can run tests by this command
#### Windows
```shell
python -m pytest
```

#### Linux/Mac Os
```shell
pytest
```

### File structure
```
.
├── app                    # Application folder
│   ├── main.py
│   ├── config.py          # Config file where the path to yaml files is configured
│   ├── dependencies.py
│   └── repositories   
│   │   ├── __init__.py
│   │   ├── builds.py
│   │   └── tasks.py     
│   └── routers          
│   │   └── tasks.py
│   └── schemas
│   │   ├── __init__.py
│   │   ├── builds.py
│   │   └── tasks.py
│   └── services          
│   │   ├── __init__.py
│   │   ├── builds.py
│   │   └── tasks.py
│   └── utils         
│       └── abc             # Abstract class and interfaces
│       │   ├── loader.py
│       │   ├── repository.py
│       │   └── service.py
│       ├── loaders.py      # yaml file loaders    
│       └── exceptions.py   # custom exceptions 
│
├── builds                  # Here yaml files by default
│   ├── builds.yaml 
│   └── tasks.yaml
│
├── tests                   # Tests for api and services
│   ├── builds              # folder with test data 
│   ├── conftest.py         # config for tests
│   ├── test_api.py
│   └── test_services.py    
│

```
