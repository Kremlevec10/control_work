import csv

from model.task import Task


class Notes:
    def __init__(self):
        self.__is_open_file = False
        self.__is_saving_file = False
        self.id = 0
        self.list_notes = dict()

    def open_file(self):
        self.__is_open_file = True
        with open('../db.csv','r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    if self.__is_parse_value_to_int(row[0]):
                        id,title,text,date = row
                        self.id = int(id)
                        task = Task()
                        task.set_id(int(id))
                        task.create_task(title,text,date)
                        self.list_notes[int(row[0])] = task

    def add_note(self,note):
        self.id += 1
        note.set_id(self.id)
        self.list_notes[self.id] = note

    def get_all_notes(self):
        return self.list_notes

    def get_note(self,id):
        return self.list_notes.get(id)

    def save(self):
        self.__is_saving_file = True
        fildes = ['id','Title','Description','Date']
        with open('../db.csv','w') as file:
            writer = csv.writer(file)
            writer.writerow(fildes)
            rows = list()
            for key,item in self.list_notes.items():
                rows.append(item.get_row())
            writer.writerows(rows)

    def __is_parse_value_to_int(self,value):
        try:
            int(value)
            return True
        except:
            return False

    def is_saving(self):
        return self.__is_saving_file

    def is_open(self):
        return self.__is_open_file
