#!/bin/sh
python manage.py dumpdata --exclude admin --exclude contenttypes --exclude sessions > exampledata.json
