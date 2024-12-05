import json

# Read the Terraform plan JSON file
with open('plan.json', 'r') as file:
    plan = json.load(file)

# Extract only the changed resources (create, update, delete)
changes = []
for resource in plan.get('resource_changes', []):
    # Extract actions for the resource
    actions = resource.get('change', {}).get('actions', [])
    
    # Include only resources with actual changes (not "no-op")
    if any(action in ['create', 'update', 'delete'] for action in actions):
        resource_name = resource.get('address', 'unknown_resource')
        actions_str = ", ".join(actions)
        
        # Append the resource change details line by line
        changes.append(f"{resource_name}: {actions_str}")

# Create a summary of changes, each on a new line
summary = "\n".join(changes)

# Write to a file (optional)
with open('changes_summary.txt', 'w') as file:
    file.write(summary)

print("Filtered changes summary prepared.")
