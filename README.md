# file-process-service

FastAPI service that accepts CSV uploads, stores the file in **Google Cloud Storage (GCS)**, records upload metadata in **PostgreSQL**, and optionally **validates** the CSV and persists parsed rows into a `content` table.

## Features

- **Upload** (`POST /upload_csv`): multipart CSV + JSON `metadata` with `email`. File is written to GCS; a row is created in `csv_uploads` with user, blob name, status `uploaded`, and server timestamp.
- **Validate** (`POST /validate`): body with GCS blob name (`file_address`). Downloads the object, validates each row with Pydantic, bulk-inserts into `content`, returns a simple success message.

## Stack

- Python 3.11+
- FastAPI, Uvicorn
- SQLAlchemy (async) + asyncpg, Alembic migrations
- Pydantic v2 (e.g. `EmailStr`, CSV row model)
- Google Cloud Storage (service account from base64 env)

## Configuration

| Variable | Purpose |
|----------|---------|
| `DATABASE_URL` | Async SQLAlchemy URL (e.g. `postgresql+asyncpg://...`) |
| `GCS_BUCKET_NAME` | Target bucket name |
| `GCP_SA_JSON_BASE64` | Base64-encoded service account JSON for GCS |

## Local setup

1. Install dependencies (e.g. `uv sync` or `pip install -e .` from `pyproject.toml`).
2. Set the environment variables above.
3. Apply migrations: `alembic upgrade head` (or use your existing DB workflow).
4. Run the API: `uvicorn main:app --reload`.

## API

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/upload_csv` | `file`: CSV (`text/csv`). `metadata`: JSON string, e.g. `{"email": "user@example.com"}`. Returns `201` with JSON `{"email": ...}`. |
| `POST` | `/validate` | JSON body `{"file_address": "<blob name in bucket>"}`. Validates rows and saves to `content`. |

OpenAPI docs: `/docs` when the app is running.

## Database

- **`csv_uploads`**: `id` (UUID), `user` (email string), `blob_address`, `status`, `created_at`.
- **`content`**: `id` (UUID), `serial_number` (unique), `sku_id`, `variant_type`, `sku_name`, `price`, `qty`, `store_location`.

## Deployment

GitHub Actions workflow `.github/workflows/deployment-railway.yaml` supports manual deploy to Railway (`workflow_dispatch`).

---

## Planning board (rough work)

Informal scratch notes and backlog — not a formal spec. Kept here for context while evolving the service.

### Todos

- pydantic
- sqlAlchemy
- GCS bucket
- cloud task
- async await
- decorator

### Problem statement

- when i upload the file, i want who(email) uploaded the file and save it and when it was uploaded.
- add preprocessing stage, after file is uploaded --> validation
- save this data into the database
- given file upload id and email id --> give me the status of the file

### Table (CSV row shape)

- serial number
- sku id
- variant type
- sku name
- price
- qty
- store location
