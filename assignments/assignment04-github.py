# assignment04-github.py
# This program will read a file from a repository and replace all of the text "Andrew" to "John"
# Author: John Crumlish

import os
import subprocess

REPO_URL = "https://github.com/johncrumlish25/WSAA-coursework"
LOCAL_REPO_FOLDER = "WSAA-coursework"
FILE_TO_EDIT = "text.txt"   
OLD_NAME = "Andrew"
NEW_NAME = "John"

def run_git_command(command):
    """Run a git command using subprocess."""
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
    return result

def main():

    # Step 1: Clone repo if not already cloned
    if not os.path.exists(LOCAL_REPO_FOLDER):
        print("Cloning repository...")
        run_git_command(["git", "clone", REPO_URL, LOCAL_REPO_FOLDER])
    else:
        print("Repository already exists. Pulling latest changes...")
        run_git_command(["git", "-C", LOCAL_REPO_FOLDER, "pull"])

    file_path = os.path.join(LOCAL_REPO_FOLDER, FILE_TO_EDIT)

    # Step 2: Read file contents
    print("Reading file...")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Step 3: Replace text
    updated_content = content.replace(OLD_NAME, NEW_NAME)

    # Step 4: Write updated content back to file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Replaced all instances of '{OLD_NAME}' with '{NEW_NAME}'.")

    # Step 5: Add changes
    run_git_command(["git", "-C", LOCAL_REPO_FOLDER, "add", FILE_TO_EDIT])

    # Step 6: Commit changes
    run_git_command([
        "git",
        "-C",
        LOCAL_REPO_FOLDER,
        "commit",
        "-m",
        f"Replaced {OLD_NAME} with {NEW_NAME}"
    ])

    # Step 7: Push changes
    print("Pushing changes to repository...")
    run_git_command(["git", "-C", LOCAL_REPO_FOLDER, "push"])

    print("Done!")


if __name__ == "__main__":
    main()