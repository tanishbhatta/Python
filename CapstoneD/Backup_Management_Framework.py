"""
Capstone 8: BACKUP MANAGEMENT FRAMEWORK

A backup management system that can register, store, list,
remove, and execute backup tasks dynamically by treating
functions as data.
"""

from typing import Callable


def apply_operation(value: str, operation: Callable[[str], str]) -> str:
    """
    Higher-order function that accepts another function.

    Args:
        value: Input string.
        operation: Function to apply.

    Returns:
        Processed string.
    """
    return operation(value)


def register_backup_task(*backup_ids: str) -> list[Callable]:
    """
    Register backup tasks.

    Args:
        backup_ids: One or more backup identifiers.

    Returns:
        List of task function references.
    """
    tasks = []

    for backup_id in backup_ids:

        execution_count = 0

        def backup(
            server: str,
            mode: str,
            backup_id: str = backup_id
        ) -> str:
            """
            Executes a backup task.
            """

            nonlocal execution_count

            execution_count += 1

            return (
                f"Backup={backup_id} | "
                f"Server={server} | "
                f"Mode={mode} | "
                f"Run={execution_count}"
            )

        tasks.append(backup)

    return tasks


def remove_backup_task(
    tasks: list[Callable],
    backup_id: str
) -> list[Callable]:
    """
    Remove a backup task.

    Args:
        tasks: Registered tasks.
        backup_id: Backup identifier to remove.

    Returns:
        Updated task list.
    """

    filtered_tasks = []

    for task in tasks:

        task_name = task("TEMP", "TEST").split("|")[0]
        current_id = task_name.split("=")[1].strip()

        if current_id != backup_id:
            filtered_tasks.append(task)

    return filtered_tasks


def list_backup_tasks(tasks: list[Callable]) -> None:
    """
    Display registered backup tasks.

    Args:
        tasks: Registered task functions.
    """

    print("Registered Tasks:")

    for task in tasks:

        task_name = task("LIST", "SCAN").split("|")[0]
        current_id = task_name.split("=")[1].strip()

        print(current_id)


def execute_backup_tasks(
    tasks: list[Callable],
    *args,
    **kwargs
) -> None:
    """
    Execute all registered tasks.

    Args:
        tasks: Registered task functions.
        *args: Positional execution arguments.
        **kwargs: Keyword execution arguments.
    """

    print("\nExecuting Tasks:\n")

    for task in tasks:
        print(task(*args, **kwargs))


# ----------------------------
# LAMBDA CALLBACK
# ----------------------------

uppercase = lambda text: text.upper()


# ----------------------------
# DEMONSTRATION
# ----------------------------

registered_tasks = register_backup_task(
    "DB-INDIA",
    "DB-CHINA",
    "DB-SINGAPORE"
)

print(apply_operation("daily backup", uppercase))

list_backup_tasks(registered_tasks)

registered_tasks = remove_backup_task(
    registered_tasks,
    "DB-CHINA"
)

print("\nAfter Removal:\n")

list_backup_tasks(registered_tasks)

# * unpacking demonstration
execution_args = (
    "SERVER-X",
    "FULL"
)

execute_backup_tasks(
    registered_tasks,
    *execution_args
)

# ** unpacking demonstration
execution_config = {
    "server": "SERVER-Y",
    "mode": "INCREMENTAL"
}

print("\nKeyword Execution:\n")

for task in registered_tasks:
    print(task(**execution_config))