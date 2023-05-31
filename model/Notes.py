class Notes:
    def __init__(self):
        self.id = 0
        self.list_notes = []

    def add_note(self,note):
        self.id += 1
        note.set_id(self.id)
        self.list_notes.append(note)

    def get_all_notes(self):
        return self.list_notes

    def save(self):
        pass