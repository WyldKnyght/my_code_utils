## Coding Utilities

### Introduction
These coding utilities are designed to assist in the development process, providing tools that simplify tasks such as extracting project folder structures and creating databases from schemas. 

These utilities are not part of the project's source code but are essential for streamlining development workflows.

### Current Structure
Current structure includes a `.my_coding_utilities` folder containing specific utility directories, a `docs` folder for documentation, and a `src` folder for project-specific code. 

This separation distinguishes between development tools and project code.

### Separation from Source Code
- By keeping these utilities separate from the `src` folder, you maintain a clear distinction between project-specific code and development tools. 
- This is similar to how infrastructure-as-code (IaC) configurations are often kept separate from application source code.

### Current Utilities
#### Extract Folder Structure:
    - This utility generates a folder structure representation of a given root directory, excluding specified directories. 
    - It uses the treelib library to create a tree structure and writes the output to a file and prints it to the console. 
    - It also appends a timestamp to the output.

#### Create databse from schema: 
    - This utility creates a SQLite database from a SQL schema file. 
    - It handles file existence checks, creates necessary directories, and executes the SQL schema.

 
