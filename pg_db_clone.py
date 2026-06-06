import subprocess
import sys
import os

SOURCE_DB_URL = os.getenv("SOURCE_DB_URL")
TARGET_DB_URL = os.getenv("TARGET_DB_URL")
DUMP_FILE = os.getenv("DUMP_FILE", "database.dump")


def run(cmd):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)

    if result.returncode != 0:
        raise RuntimeError(f"Command failed with exit code {result.returncode}")


def main():
    if not SOURCE_DB_URL:
        print("Error: SOURCE_DB_URL environment variable is not set")
        sys.exit(1)
    if not TARGET_DB_URL:
        print("Error: TARGET_DB_URL environment variable is not set")
        sys.exit(1)
    
    try:
        print("Creating dump from source database...")

        run([
            "pg_dump",
            "--format=custom",
            "--verbose",
            "--no-owner",
            "--no-privileges",
            "--dbname",
            SOURCE_DB_URL,
            "--file",
            DUMP_FILE,
        ])

        print("Restoring into target database...")

        run([
            "pg_restore",
            "--verbose",
            "--clean",
            "--if-exists",
            "--no-owner",
            "--no-privileges",
            "--dbname",
            TARGET_DB_URL,
            DUMP_FILE,
        ])

        print("Database clone completed successfully.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
