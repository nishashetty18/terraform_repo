import re

# Define a function to parse the plain text and extract resource name and action
def extract_changes_from_txt(file_path):
    changes = []

    # Define regular expressions to match resource actions (create, update, delete)
    create_pattern = re.compile(r'(\S+)\s+will be created')
    update_pattern = re.compile(r'(\S+)\s+will be updated')
    delete_pattern = re.compile(r'(\S+)\s+will be destroyed')

    # Open and read the file
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Match the "create", "update", and "delete" actions
                create_match = create_pattern.search(line)
                update_match = update_pattern.search(line)
                delete_match = delete_pattern.search(line)

                # Append resource and action to the changes list
                if create_match:
                    changes.append(f"{create_match.group(1)}: create")
                elif update_match:
                    changes.append(f"{update_match.group(1)}: update")
                elif delete_match:
                    changes.append(f"{delete_match.group(1)}: delete")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

    return changes

# Path to your plain text file (adjust this to your file path)
file_path = 'readable_plan.txt'

# Extract changes
changes = extract_changes_from_txt(file_path)

# If changes were found, create a summary
if changes:
    # Join the changes into a formatted string
    summary = "\n".join(changes)

    # Write the summary to a file (optional)
    with open('changes_summary.txt', 'w') as file:
        file.write(summary)

    print("Filtered changes summary written to changes_summary.txt.")
else:
    print("No changes found or error processing the file.")
