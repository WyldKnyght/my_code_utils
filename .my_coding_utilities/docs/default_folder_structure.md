### Default Folder Structure
These utility codes, work on the following folder structure, if you use a different structure the codes will need to be refactrored to match.

Project Root
├── data               # SQLite database, schema files, and external data sources
├── docs               # Documentation
├── src
│   ├── main.py        # Entry point
│   ├── configs        # Configuration files
│   ├── controllers    # Business logic
│   ├── user_interface # UI code (no logic)
│   └── utils          # Utility functions
└── tests              # Unit and integration tests