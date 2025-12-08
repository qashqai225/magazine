**Repository Overview**

- **Type:** Django web app (single project `magazine`, single app `main`). Entrypoint: `manage.py`.
- **DB:** SQLite at `db.sqlite3` (local development only).
- **Static & Templates:** app-local templates under `main/templates/`; static assets under `main/static/deps/`.

**Quick Start (Developer commands)**

- **Run dev server:** `python manage.py runserver`
- **Apply DB migrations:** `python manage.py migrate`
- **Create migrations for `main`:** `python manage.py makemigrations main`
- **Create superuser:** `python manage.py createsuperuser`
- **Run tests:** `python manage.py test`

**Big Picture & Architecture**

- Single Django project with one application called `main`. URL routing and app registration are standard (see `magazine/urls.py` and `magazine/settings.py`).
- Views are implemented as function-based views (see `main/views.py` — `index()` and `about()` examples).
- Templates live in `main/templates/main/` and predominantly reference static assets under the `deps/` folder.

**Project-specific patterns & conventions**

- **Templates:** use `{% load static %}` and mostly use `{% static 'deps/...' %}` for CSS. Note: some script tags at the bottom of `main/templates/main/index.html` use relative paths like `deps/js/...` rather than `{% static %}` — preserve the existing pattern when making minimal changes.
- **Static layout:** CSS, JS, images and icons are grouped under `main/static/deps/` (examples: `deps/css/*`, `deps/js/*`, `deps/images/*`).
- **Views → Templates:** view `index` renders `main/index.html` with context keys `title`, `content`, `list`, `dict`, and `bool` — follow similar context naming for simple pages.
- **Settings quirks:** `magazine/settings.py` sets `DEBUG = True`, `ALLOWED_HOSTS = ['*']`, and a non-standard `STATIC_URL = "/../static/"` with `STATICFILES_DIRS` pointing at `BASE_DIR / '..' / 'main' / 'static'`. When changing static handling, check this configuration first.

**Integration points & external dependencies**

- No external services configured: everything is local (SQLite + static files). Ensure `django` is installed. There is no `requirements.txt` in the repo — use `pip install django` (version compatible with settings; tested with Django 4/5 series).

**Editing guidance for AI agents**

- Focus edits on the `main` app unless instructed otherwise. Keep changes minimal and consistent with current patterns (function-based views, templates under `main/templates/main`, static under `main/static/deps`).
- When modifying templates, prefer existing static referencing style in that file — e.g., maintain `{% static 'deps/css/...' %}` for CSS and preserve relative script references unless refactoring all templates.
- If adding new static assets, place them under `main/static/deps/` and reference via `{% static 'deps/...path...' %}`.
- For DB schema changes: add migrations via `makemigrations` and include new migration files in commits.

**Where to look for examples**

- `manage.py` — project entrypoint and the standard Django command surface.
- `magazine/settings.py` — static handling, installed apps, DEBUG/ALLOWED_HOSTS.
- `main/views.py` — examples of function-based views and context shaping.
- `main/templates/main/index.html` — canonical template showing static usage, layout, and mixed-language content.
- `main/static/deps/` — canonical location for CSS, JS, icons, and images.

**Merge notes**

- No existing agent instruction files (e.g., `copilot-instructions.md`, `AGENT.md`) were found. If you add or merge later, preserve these repo-specific bullets: static layout, `STATIC_URL` quirk, and template static patterns.

If anything here is unclear or you'd like more examples (e.g., test structure or a suggested `requirements.txt`), tell me which area to expand and I'll iterate.
