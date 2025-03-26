# extract_folder_structure.py
import datetime
import os

from treelib import Tree


def generate_folder_structure(root_dir, output_file=None, excluded_directories=None):
    tree = Tree()
    tree.create_node(os.path.basename(root_dir), root_dir)  # Create the root node

    # Convert excluded_dirs to a set (if it's not already)
    excluded_dir_set = set(excluded_directories) if excluded_directories else set()

    def add_to_tree(directory, parent):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                if item in excluded_dir_set:
                    continue
                node = tree.create_node(item, item_path, parent=parent)
                add_to_tree(item_path, node)
            else:
                # Add files to the tree
                file_name = os.path.basename(item_path)
                tree.create_node(file_name, item_path, parent=parent)

    # Call the add_to_tree function here
    add_to_tree(root_dir, root_dir)  # Build the tree structure

    if output_file:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(str(tree))

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nScript last modified: {timestamp}")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"\nScript last modified: {timestamp}")
if __name__ == "__main__":
    project_root = "m:\\dev_env\\my_code_utils"
    admin_dir = os.path.join(project_root, ".my_coding_utilities")
    output_filename = os.path.join(admin_dir, "project_setup", "folder_structure.txt")
    excluded_dirs = {
        ".git",
        ".venv",
        ".vs",
        ".my_files",
        "__pycache__",
        ".github",
        ".admin",
        ".vscode",
        ".myfiles",
        ".mypy_cache",
        "test",
        "data",
        "tests"
    }

    print(f"Project Folder Structure for: {project_root}")
    generate_folder_structure(project_root, output_file=output_filename, excluded_directories=excluded_dirs)