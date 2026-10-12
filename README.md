# HRL Local Human Services Provider — Complete FYP Project

This package contains **both frontend and Django backend** for the HRL Service Provider FYP.

## Project Structure

- `frontend/` — HTML/CSS/JavaScript website, service pages, provider pages, admin UI mockups.
- `backend/` — Django project with Provider model, document uploads, verification status, and Django Admin approval/rejection.

## Backend Setup (Windows)

Open Command Prompt/PowerShell inside the `backend` folder:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open:

- Main frontend: `http://127.0.0.1:8000/frontend/index.html`
- Provider registration backend page: `http://127.0.0.1:8000/provider/register/`
- Approved providers: `http://127.0.0.1:8000/provider/list/`
- Django admin: `http://127.0.0.1:8000/admin/`

## Verification Flow

1. Provider registers and uploads CNIC front/back, profile picture and optional certificate.
2. Provider starts with `Pending Verification` status.
3. Admin logs into `/admin/`.
4. Admin opens **Providers** and reviews documents.
5. Admin can approve or reject providers.
6. Only approved providers appear on the backend verified-provider list.

## Important

The frontend pages are designed as the user-facing UI. The Django backend contains the real database/model and document-upload verification workflow. For a fully connected production-style deployment, the frontend forms can be served through Django templates or connected to Django endpoints with CSRF protection and authentication.

This is an FYP/demo project. Do not use real CNIC documents in an unsecured development environment.


### Updated Frontend
All frontend pages now use the same HRL Services header, Services dropdown, Become a Provider link, and complete professional footer. Provider registration page was also unified with the same header/footer.
