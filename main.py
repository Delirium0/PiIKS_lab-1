import datetime
import os
import platform
import shutil
import subprocess


def backup_data(actions_enabled):
    source_folder = input("Введите путь к исходной папке: ")
    backup_folder = input("Введите путь к папке резервного копирования: ")

    try:
        shutil.copytree(source_folder, backup_folder)
        print("Резервное копирование выполнено успешно.")
        if actions_enabled:
            register_action(f"Резервное копирование: {source_folder} -> {backup_folder}")
    except Exception as e:
        print(f"Произошла ошибка при резервном копировании: {e}")


def create_or_edit_file(actions_enabled):
    file_name = input("Введите имя файла: ")
    file_content = input("Введите содержимое файла: ")

    try:
        with open(file_name, 'w') as file:
            file.write(file_content)
        print(f"Файл '{file_name}' успешно создан/изменен.")
        if actions_enabled:
            register_action(f"Файл '{file_name}' успешно создан/изменен.")
    except Exception as e:
        print(f"Произошла ошибка при создании/изменении файла: {e}")


def register_action(action_message):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    with open("actions.log", "a") as log_file:
        log_file.write(f"{formatted_time}: {action_message}\n")


def check_system_info(actions_enabled):
    system_info = platform.uname()
    print(f"Системная информация: {system_info}")
    if actions_enabled:
        register_action(f"Запрошена Системная информация: {system_info}")


def clear_screen(actions_enabled):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Экран очищен.")
    if actions_enabled:
        register_action(f"экран очищен")


def mark_files(actions_enabled):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Маркировка файлов
    file_name = input("Введите имя файла для маркировки: ")
    with open(file_name, 'a') as file:
        file.write(f"\nМаркировка: {formatted_time}\n")
    print(f"Файл '{file_name}' был маркирован.")
    if actions_enabled:
        register_action(f"Файл '{file_name}' был маркирован.")


def configure_os(actions_enabled):
    command = input("Введите команду для конфигурирования ОС: ")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Команда выполнена успешно: {command}")
        if actions_enabled:
            register_action(f"Команда выполнена успешно: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка при выполнении команды: {e}")


def input_large_text(actions_enabled):
    print("Введите текст. Для завершения ввода введите 'EOF' в новой строке.")
    text = ""
    while True:
        line = input()
        if line == 'EOF':
            break
        text += line + "\n"
    print("Введенный текст:")
    print(text)
    if actions_enabled:
        register_action(f'выведен текст {text}')


def register_actions():
    actions_enabled = True
    while True:

        choice = input(
            " 1 -резервное копирование \n 2 - включить отключить логирование "
            "\n 3 - выход из программы \n 4 - Системная информация \n 5 - очищение экрана "
            "\n 6 - Маркировка/датировка информации в файлах \n 7 - команда для конфигурирования "
            "\n 8 - Ввод/вывод на экран \n 9 - создание удаление файлов \n Выберите команду (1/2/3/4/5/6/7/8/9/0):")

        if choice == '1':
            backup_data(actions_enabled)
        elif choice == '2':

            actions_enabled = not actions_enabled  # Включение/отключение регистрации действий
            print(f'логирование теперь {actions_enabled}')
        elif choice == '3':
            print("Выход из программы.")
            break
        elif choice == '4':
            check_system_info(actions_enabled)
        elif choice == '5':
            clear_screen(actions_enabled)
        elif choice == '6':
            mark_files(actions_enabled)
        elif choice == '7':
            configure_os(actions_enabled)
        elif choice == '8':
            input_large_text(actions_enabled)
        elif choice == '9':
            create_or_edit_file(actions_enabled)
        else:
            print("Неверный выбор команды. Пожалуйста, выберите из списка (1/2/3/4/5/6/7/8/9/0).")


register_actions()
