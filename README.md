# Market Price Watch

Real prices from real markets. Market Price Watch is a Django web app where anyone can report what food staples cost at their local market, and everyone can compare prices across markets to find the cheapest deal.

Built by David Peluola during SIWES II at HiiT PLC, as the project for the Django Framework course.

## Features

- **Latest prices:** the home page shows the ten most recent price reports across all markets.
- **Item pages:** each item shows its lowest, average and highest reported price, the cheapest market, and every report with notes and dates.
- **Public price reporting:** anyone can submit a price through a validated form, with an optional photo of the price tag as proof.
- **Admin dashboard:** a customised Django admin for managing markets, items and reports, with search, filters and a date drill-down.

## Tech stack

- Python 3.12 or newer
- Django 6.1
- SQLite (development database)
- Pillow (image validation for uploads)
- python-dotenv (loads settings from a `.env` file)
- HTML and CSS with Django templates

## Data model

| Model | Fields | Notes |
|---|---|---|
| `Market` | name, city, state | One market has many price reports |
| `Item` | name, unit, category | Unit gives the price meaning (e.g. 50kg bag) |
| `PriceReport` | item, market, price, note, photo, reported_at | `on_delete=PROTECT` on both foreign keys, so price history is never deleted by accident |

## Getting started

These commands are for Git Bash on Windows. On macOS or Linux, activate the virtual environment with `source venv/bin/activate` instead.

```bash
git clone https://github.com/Adeolu05/market-price-watch.git
cd market-price-watch
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env
```

Generate a secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Open `.env` and replace `generate-your-own` with that key, keeping the single quotes. Then:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit http://127.0.0.1:8000 for the site and http://127.0.0.1:8000/admin to add markets and items.

## Security

- The secret key lives in `.env`, which is excluded from Git. Only `.env.example` is committed.
- `DEBUG` defaults to `False`, so the site fails safe if the setting is missing.
- `ALLOWED_HOSTS` is restricted and read from the environment.
- In production (`DEBUG=False`), HTTPS redirect, secure session and CSRF cookies, and HSTS are switched on.
- All forms use CSRF protection, and templates auto-escape user input to block XSS.
- Price validation runs on the server, and uploaded photos are checked by Pillow to be real images under 3MB.
- `python manage.py check --deploy` passes apart from two HSTS options (subdomains and preload) that are deliberately left off until the app has its own domain.
- `pip-audit` reports no known vulnerabilities in the dependencies.

## Project structure

```
market-price-watch/
  manage.py
  requirements.txt
  .env.example
  pricewatch/          project settings and root URLs
  prices/              the app
    models.py          Market, Item, PriceReport
    views.py           home, item_detail, report_price
    forms.py           PriceReportForm with custom validation
    admin.py           customised admin
    urls.py            app routes
    templates/prices/  base, home, item detail and report form templates
    static/prices/     stylesheet
```

## Planned improvements

- Rate limiting and moderation on the public form to stop spam and fake prices
- Price trend charts over time for each item
- Filtering by market, city and category on the public pages
- PostgreSQL and a live deployment

## Author

David Peluola ([@Adeolu05](https://github.com/Adeolu05))