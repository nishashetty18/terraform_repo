import json

# Define the file path
file_path = 'plan.json'

try:
    # Open the file with the correct encoding (assuming UTF-8 is the expected encoding)
    with open(file_path, 'r', encoding='utf-8') as file:
        plan = json.load(file)
except UnicodeError as e:
    print(f"Encoding error: {e}")
    print("Retrying with UTF-16 encoding...")
    try:
        # Retry with UTF-16 encoding
        with open(file_path, 'r', encoding='utf-16') as file:
            plan = json.load(file)
    except Exception as e:
        print(f"Failed to read the file with UTF-16 encoding: {e}")
        exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit(1)
except FileNotFoundError as e:
    print(f"Error: {file_path} not found: {e}")
    exit(1)

# Extract only the changed resources (create, update, delete)
changes = []
for resource in plan.get('resource_changes', []):
    # Extract actions for the resource
    actions = resource.get('change', {}).get('actions', [])
    # Include only resources with actual changes (not "no-op")
    if any(action in ['create', 'update', 'delete'] for action in actions):
        resource_name = resource.get('address', 'unknown_resource')
        actions_str = ", ".join(actions)
        changes.append(f"{resource_name}: {actions_str}")

# Create a summary of changes
summary = "\n".join(changes)

# Write to a file (optional)
output_file = 'changes_summary.txt'
try:
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(summary)
    print(f"Filtered changes summary written to {output_file}.")
except Exception as e:
    print(f"Error writing to {output_file}: {e}")
