### Project Strucure
```
fastapi_replicate/
├── app/
│   ├── main.py                 # Main FastAPI application file
│   ├── config.py               # Configuration for Replicate API
│   ├── models/
│   │   ├── __init__.py
│   │   └── image_model.py      # Fine-tuning and generation functions
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── image.py            # Request and response schemas
│   ├── routers/
│   │   ├── __init__.py
│   │   └── image_router.py     # Routers for API endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   └── replicate_service.py # Replicate API interaction
├── .env            # environment variable
├── requirements.txt            # Dependency requirements
└── start.sh            # shell script to start the app

```

#### Project Description

- It is a FastAPI application that uses the Replicate Image generation endpoint to fine-tune and generate images.

#### Project Setup

##### Step 1: clone the repository

##### Step 2: create virtual env
```
python -m venv env
```

##### Step 3: Create `.env` file with following variables
```
REPLICATE_API_TOKEN='your key'
```

##### Step 4: Get the App Running
```
./start.sh
```


#### Documentation : `http://127.0.0.1:8000/docs/`