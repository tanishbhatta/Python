def build_job_scheduler(space):
    sample = []
    for id in range(len(space)):

        def caller(callback_id:int = id) -> str:
            return f"{space[callback_id]}"
        sample.append(caller)
    
    return sample

jobs = build_job_scheduler(
    ["Backup", "Sync", "Cleanup"]
)

print(jobs[0]())
print(jobs[1]())
print(jobs[2]())