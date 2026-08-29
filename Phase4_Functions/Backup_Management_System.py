def register_backup_tasks(server_id:str , backup_region:str, / , * , maintainance_window:int, force_mode:bool):
    callback_list = []

    for callback_id in range(4):
        def task(capturedid:int = callback_id) -> str:
            return f"Task {capturedid} scheduled on {server_id}"
        callback_list.append(task)
    
    return callback_list

tasks = register_backup_tasks(
    "SERVER-X",
    "EU-WEST",
    maintainance_window=12,
    force_mode=True
)

print(tasks[0]())
print(tasks[1]())
print(tasks[2]())
print(tasks[3]())
    
