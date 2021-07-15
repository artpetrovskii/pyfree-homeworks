HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []
today = []
tomorrow = []
other = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    task = input("Введите название задачи: ")
    time_of_task = input("Введите дату выполнения задачи: ")
    if time_of_task == "Сегодня":
      today.append(today)
    elif time_of_task == "Завтра":
      tomorrow.append(tomorrow)
    else:
      other.append(other)
    tasks.append(task) 
    print("Задача добавлена")
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    break
  else:
    print("Неизвестная команда")
    break
