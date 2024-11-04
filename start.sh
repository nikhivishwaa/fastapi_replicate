#!bin/bash

echo "Running FastAPI App"
source ./env/Scripts/activate
pip install -r requirements.txt


# cd app/
uvicorn app.main:app --reload
