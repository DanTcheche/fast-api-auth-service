#!/bin/bash

# Let the DB start
python api_pre_start.py

# Run migrations
alembic upgrade head

# Run application
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
