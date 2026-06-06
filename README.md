# Scripts Collection

A collection of utility scripts for various development and maintenance tasks.

## Overview

This repository contains standalone Python scripts designed to automate common operations like database management, data processing, and deployment tasks. Each script is self-contained and can be run independently.

## Scripts

### `pg_db_clone.py`

Clones a PostgreSQL database from a source to a target environment using `pg_dump` and `pg_restore`.

**What it does:**
1. Creates a custom binary dump from the source database
2. Restores the dump into the target database with clean/fresh install semantics

**Use cases:**
- Syncing production data to staging/development environments
- Creating backups in different database services
- Migrating databases between cloud providers

**Features:**
- Uses custom binary format for optimal performance
- Cleans existing objects in target database before restore
- Removes owner/privilege information to simplify restoration
- Verbose output for debugging

**Prerequisites:**
- PostgreSQL client tools (`pg_dump`, `pg_restore`) must be installed
- Network access to both source and target databases
- Appropriate database credentials

**Usage:**

Set the required environment variables and run:

```bash
export SOURCE_DB_URL="postgresql://user:password@host:port/source_db"
export TARGET_DB_URL="postgresql://user:password@host:port/target_db"
python pg_db_clone.py
```

Or pass them inline:

```bash
SOURCE_DB_URL="..." TARGET_DB_URL="..." python pg_db_clone.py
```

**Environment Variables:**
- `SOURCE_DB_URL` (required) - PostgreSQL connection string for the source database
- `TARGET_DB_URL` (required) - PostgreSQL connection string for the target database
- `DUMP_FILE` (optional) - Path for the dump file (defaults to `database.dump`)

The generated dump file is saved in the current directory (or path specified by `DUMP_FILE`).

## Requirements

- Python 3.14+
- PostgreSQL client tools (for `pg_db_clone.py`)

## Setup

### Using Pipenv

```bash
pipenv install
pipenv run python pg_db_clone.py
```

### Using pip

```bash
pip install -r requirements.txt
python pg_db_clone.py
```

## Directory Structure

```
.
├── README.md              # This file
├── Pipfile                # Pipenv dependencies
├── pg_db_clone.py         # PostgreSQL database cloning script
└── database.dump          # Generated database dump file (ignored in git)
```

## Contributing

To add a new script:
1. Create a new Python file with a clear, descriptive name
2. Include a docstring explaining its purpose
3. Update this README with the script's description and usage instructions

## License

These scripts are provided as-is for personal use.
