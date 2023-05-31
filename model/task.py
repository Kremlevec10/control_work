class Task:
    def __init__(self):
        self.id = int()
        self.title = str()
        self.text = str()
        self.date = 'Дата создания'


    def create(self,title,text):
        self.title = title
        self.text = text


    def edit(self,title=None,text=None):
        if title:
            self.title = title
        if text:
            self.text = text
        self.date = 'Дата изменения'

    def set_id(self,id):
        self.id = id

