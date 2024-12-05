import json
with open('plan.json', 'r') as file:
    plan = json.load(file)
changes = []
for resource in plan.get('resource_changes', []):
    actions = resource.get('change', {}).get('actions', [])
    if any(action in ['create', 'update', 'delete'] for action in actions):
        resource_name = resource.get('address', 'unknown_resource')
        actions_str = ", ".join(actions)
        changes.append(f"{resource_name}: {actions_str}")

summary = "\n".join(changes)
with open('changes_summary.txt', 'w') as file:
    file.write(summary)

print("Filtered changes summary prepared.")
