

## Requirements
- Python 3.12 or higher
- Docker (If installation is not possible, use GitHub Codespaces for development.)
- uv package management (Installation: [uv on PyPI](https://pypi.org/project/uv/))
- DuckDB
  - via CLI: [Installation Guide](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=package_manager)  
  - recommended via IDE: [DBeaver Guide](https://duckdb.org/docs/stable/guides/sql_editors/dbeaver.html)  
-unzip file on folder data

```

via Docker:
```bash
docker compose build
docker compose up --watch # Auto rebuild on changes
```
> **Note:** To reload code after making changes, go to the "Deployment" tab and click "Reload All."

There may be some error messages initially, but it should stabilize within a few seconds once all services are up and running.

You should be able to access the Dagster UI at http://localhost:3000.

> In case of using GitHub Codespaces, after starting your Dagster instance, open the "Ports" tab in the GitHub Codespaces interface. You should see a forwarded port 3000. Click on the link to access the Dagster UI directly.

## Adding New Packages

In case you want to add additional dependencies, run:
```bash
uv add <Package name>
```

Then run:
```bash
uv lock  # Updates dependencies without upgrading existing ones
# or
uv lock --upgrade  # To upgrade and update the lock file
uv sync  # To install from the lock file
```