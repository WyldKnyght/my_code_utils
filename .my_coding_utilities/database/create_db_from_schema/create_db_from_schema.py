# create_db_from_schema.py
import logging
import sqlite3
from pathlib import Path
from sqlite3 import Error as SQLiteError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Paths (update these as needed)
PROJECT_ROOT = Path("M:\dev_env\my_code_utils")
DATA_PATH = PROJECT_ROOT / "data"
DB_NAME = "sample.db"
DB_PATH = DATA_PATH / DB_NAME
SCHEMA_PATH = DATA_PATH / "schema.sql"

def create_database(db_path: Path, schema_path: Path, overwrite: bool = False):
    """Create or recreate a SQLite database from a SQL schema file."""
    logger.info(f"Starting database creation at {db_path}")

    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    if db_path.exists() and not overwrite:
        logger.warning(f"Database already exists at {db_path}. Set overwrite=True to recreate.")
        return

    db_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute("PRAGMA foreign_keys = ON;")
            conn.execute("PRAGMA journal_mode = WAL;")

            with open(schema_path, 'r') as schema_file:
                schema_content = schema_file.read()
                conn.executescript(schema_content)

        logger.info(f"Database {'recreated' if overwrite else 'created'} successfully at {db_path}")
    except SQLiteError as e:
        logger.error(f"SQLite error during database creation: {e}")
        raise

def main():
    """Main function to create the database."""
    try:
        create_database(DB_PATH, SCHEMA_PATH, overwrite=False)
    except Exception as e:
        logger.error(f"Failed to create the database: {e}")

if __name__ == "__main__":
    main()
