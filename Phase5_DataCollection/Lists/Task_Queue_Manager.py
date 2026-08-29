"""
Requirements:

Create a list containing at least 8 tasks.
Remove one task by value.
Remove one task by position and store the removed task.
Delete a range of tasks.
Display the removed task.
Display the remaining tasks.
Empty the entire queue.
Verify the queue still exists afterward.
"""
tasks = ['Broom', 'Wash Dishes', 'Wash Clothes', 'Watch TV', 'Scroll', 'Visit Temple', 'Play Game', "Coding"]
tasks.remove('Broom')

important = tasks.pop(-1)

del tasks[2:7]

print(important)
print(tasks)

tasks.clear()
print(tasks)