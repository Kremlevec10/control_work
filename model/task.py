import datetime


class Task:
    def __init__(self):
        self.id = int()
        self.title = str()
        self.text = str()
        self.date = datetime.datetime.now()


    def create(self,title,text):
        self.title = title
        self.text = text

    def create_task(self,title,text,date):
        self.title = title
        self.text = text
        self.date = date


    def edit(self,title=None,text=None):
        if title:
            self.title = title
        if text:
            self.text = text
        self.date = 'Дата изменения'

    def set_id(self,id):
        self.id = id

    def get_row(self):
        return [self.id,self.text,self.title,self.date]

    def info(self):
        return f'{self.id} {self.title} {self.text} {self.date}'