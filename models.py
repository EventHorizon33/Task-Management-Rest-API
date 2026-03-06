task_counter = 1
tasks = []

class Task:
    def __init__(self, title, description=""):
        global task_counter
        self.id = task_counter
        self.title = title
        self.description = description
        self.done = False
        task_counter += 1

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done
        }
    
# tasks = []: in-memory database. all tasks done are stored into this
# task_counter: global counter that gives each task a unique ID. It never rests,
# never reuses IDs even after any deletes.
# __init__ : runs when a new task is created. Takes (required) title and (optional_ description.
# to+dict(): converts a Task object into a plain dictionary.
    # so Flask can turn it into a JSON request.

# Why task_counter instead of len(tasks)?
    # If you have 3 tasks and delete task 2, len(tasks) becomes 2 — so your next task gets ID 2 again, colliding with history. 
    # The counter only ever goes up.
