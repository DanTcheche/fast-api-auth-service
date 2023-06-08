#!/bin/bash

# Let the db start
python prestart_scripts/backend_pre_start.py

# Run migrations
alembic upgrade head

# Run application
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload