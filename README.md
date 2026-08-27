# catalogo

Django app that implements a product catalog, part of the `django_mastery` project.

## App contents

- **Model** (`models.py`): `Producto` with the fields `nombre` (CharField), `descripcion`
  (TextField), `precio` (DecimalField, max 10 digits / 2 decimal places), `categoria`
  (CharField with choices: Electrónica, Ropa, Hogar) and `fecha_ingreso` (DateField, set
  automatically on creation).
- **Views** (`views.py`): `lista_productos` — lists products with optional filtering and
  pagination:
  - `q`: free-text search matching `nombre` or `descripcion` (case-insensitive, partial match).
  - `categoria`: exact-match filter by category.
  - Results are paginated at 2 products per page via Django's `Paginator`.
- **Templates** (`templates/catalogo/`):
  - `lista_productos.html` — extends `blog_estatico/base.html`; renders a search/filter form
    and a table of products (name, description, price, category), plus Previous/Next
    pagination controls that preserve the active search and filter.
- **Routes** (`urls.py`):

  | Route | View | Description |
  |-------|------|-------------|
  | `''` | `lista_productos` | Product list, with search (`q`), category filter (`categoria`) and pagination (`page`) |

- **Admin** (`admin.py`): `Producto` registered with `list_display` showing `nombre`,
  `categoria`, `precio` and `fecha_ingreso`.

## Usage

This app is part of the `django_mastery` Django project and does not run standalone.
It must be registered in `INSTALLED_APPS` and its routes included in the project's root
`urls.py` (already configured under the `catalogo/` prefix). To start the server, run from
the repository root:

```bash
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/catalogo/`.

Example queries:

```
http://127.0.0.1:8000/catalogo/?q=phone
http://127.0.0.1:8000/catalogo/?categoria=ropa
http://127.0.0.1:8000/catalogo/?q=phone&categoria=electronica&page=2
```
