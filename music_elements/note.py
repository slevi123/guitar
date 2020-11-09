

class Note:
    all_notes = {}

    def __init__(self, name):
        self.name = name.strip()
        self.all_notes[name] = self

    def __str__(self):
        return self.name

    @classmethod
    def get_note(cls, key):
        key = key[0].upper() + key[1:]
        return cls.all_notes[key]

    @classmethod
    def init_notes(cls, list_of_notes_names="C,D,E,F,G,A,B"):
        """It takes the C-major notes and create all the natural and modified notes
        Use [] operator to access them"""
        for note_name in list_of_notes_names.split(','):
            cls(note_name + 'b')
            cls(note_name)
            cls(note_name+'#')

    def __repr__(self):
        return f'"{self.name}"'


Note.init_notes()


def main():
    print(len(Note.all_notes))
    print(list(map(str, Note.all_notes)))


if __name__=="__main__":
    main()
