# Initial queue of pending tasks
tasks = ["Prepare Report", "Send Emails"]

print("Pending Tasks:", tasks)

# Assign the next task (remove and return the first task)
assigned_task = tasks.pop(0)
print("\nAssigned Task:", assigned_task)

print("Remaining Tasks:", tasks)

# Batch of new tasks received
new_tasks = ["Schedule Meeting", "Client Follow-up"]

# Add all new tasks to the queue
tasks.extend(new_tasks)

print("\nUpdated Task Queue:", tasks)