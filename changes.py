import json

# Read the Terraform plan JSON file as UTF-16
with open('plan.json', 'r', encoding='utf-16') as file:
    plan = json.load(file)

# Extract only the changed resources (create, update, delete)
changes = []
for resource in plan.get('resource_changes', []):
    actions = resource.get('change', {}).get('actions', [])
    if any(action in ['create', 'update', 'delete'] for action in actions):
        resource_name = resource.get('address', 'unknown_resource')
        actions_str = ", ".join(actions)
        changes.append(f"{resource_name}: {actions_str}")

# Create a summary of changes
summary = "\n".join(changes)

# Write to a file (optional)
with open('changes_summary.txt', 'w') as file:
    file.write(summary)

print("Filtered changes summary prepared.")
