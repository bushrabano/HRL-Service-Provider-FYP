HRL Service Provider - Provider Verification FYP

This package contains the existing frontend plus a Django backend for real provider verification.

1) Install Python 3.10+.
2) Open terminal in the backend folder.
3) Run: python -m venv venv
4) Windows: venv\Scripts\activate
5) Run: pip install -r requirements.txt
6) Run: python manage.py makemigrations
7) Run: python manage.py migrate
8) Run: python manage.py createsuperuser
9) Run: python manage.py runserver
10) Open http://127.0.0.1:8000/provider/register/
11) Open http://127.0.0.1:8000/admin/ and log in with the superuser.

Admin opens a Provider record, checks submitted documents, and changes Status to Approved or Rejected. Approved providers appear at /provider/list/ with a Verified Provider badge.

Important: This is an FYP verification workflow. A real production identity verification service would require secure document handling, access controls, encryption, retention rules, and—if needed—an authorized identity-verification provider/API. Do not treat a simple admin approval as government identity verification.
