# Django basic project
## Required modules:
**django**
*from django.http import HttpResponse*
*from django.urls import path, include*
*from django.shortcuts import render*
*from django.views import View*
*from django.views.generic import TemplateView*
*from django.test import SimpleTestCase*

### Install command:
pip install django

### Create project command:
django-admin startproject config .

### Create app command:
python manage.py startapp message

## Run project command:
python manage.py runserver

## Test apps command: (like message app)
python manage.py test
