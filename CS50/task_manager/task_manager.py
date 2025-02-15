def main():
    task = {}

    def menu():
        exit_program = False

        while not exit_program:
            # Pergunta se o usuário quer adicionar uma tarefa
            keep = input("Do you want to add any task?\nInsert 'No' or 'Yes': ").title()

            if keep == "No":
                # Pergunta se quer sair ou deletar
                if len(task) > 0:
                    del_or_leave = input(
                        "Do you want to exit the program or delete a task?\nInsert 'exit' or 'delete': "
                    )

                    if del_or_leave == "exit":
                        print_tasks(task)
                        exit_program = True

                    elif del_or_leave == "delete":
                        clear = input(
                            f"What task do you want to clear: {list(task.keys())} "
                        )
                        if clear in task:
                            task.pop(clear)
                            print(f"You just removed {clear}")
                        else:
                            print("Task not found.")
                else:
                    print("No tasks to manage.")
                    exit_program = True
            else:
                try:
                    t, d, s = input(
                        "Please add the task, date (YYYY-MM-DD), and status (e.g., Pending, Completed): "
                    ).split(",")
                    t = t.strip()  # Remove possíveis espaços extras
                    d = d.strip()
                    s = s.strip()

                    # Validação simples para data e status
                    if not t or not d or not s:
                        print("Invalid input. Please provide all fields.")
                        continue

                    task[t] = {"date": d, "status": s}
                    print(f"Task '{t}' added successfully.")

                except ValueError:
                    print(
                        "Invalid format. Please use the format: task, date, status (comma separated)."
                    )

        if len(task) > 0:
            print("\nAll tasks:")
            print_tasks(task)
        else:
            print("No tasks to show.")

    def print_tasks(task_dict):
        if task_dict:
            for task_name, details in task_dict.items():
                print(f"{task_name}, {details['date']}, {details['status']}")
        else:
            print("No tasks available.")

    menu()


main()
