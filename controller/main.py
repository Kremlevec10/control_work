# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.

# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать
# идентификатор,
# заголовок,
# тело заметки и
# дату/время создания
# или
# последнего изменения заметки.
# Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента
import sys

from model.notes import Notes
from model.task import Task
from view.view import View

def start():
    view = View()
    notes = Notes()
    while(True):
        view.menu()
        choice = int(view.select('Выберите пункт меню'))
        match choice:
            case 1:
                notes.open_file()
                view.show_massage('Файл открыт')
            case 2:
                if notes.is_open():
                    task = Task()
                    task.create(view.select('Введите название заголовка'),view.select('Введите описание заметки'))
                    notes.add_note(task)
                else:
                    view.show_massage('Сначало откройте файл')
            case 3:
                if notes.is_open():
                    view.show_notes(notes.get_all_notes())
                    id = int(view.select('Выберите id изменяемой заметки'))
                    note = notes.get_note(id)
                    task.edit(view.select('Введите название заголовка'),view.select('Введите описание заметки'))
                else:
                    view.show_massage('Сначало откройте файл')
            case 4:
                if notes.is_open():
                    notes.save()
                    view.show_massage('Файл сохранен')
                else:
                    view.show_massage('Сначало откройте файл')
            case 5:
                if notes.is_open():
                    view.show_notes(notes.get_all_notes())
                else:
                    view.show_massage('Сначало откройте файл')
            case 6:
                if notes.is_saving():
                    sys.exit()
                else:
                    view.show_massage('Сначло сохраните файл')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
