from music_elements.note import Note
from collections import defaultdict


class Scale:
    all_scales = {
        # 'chromatic': CromaticScale,
        'minor': {},
        'major': {},
        'pentatonic': {}
    }
    all_scales = defaultdict(dict, all_scales)
    registered_scale_types = {}  # chromatic excluded

    @classmethod
    def get_scale(cls, scale_type, key: Note = None, *args):
        if scale_type == 'chromatic':
            if key:
                # this part is only for internal use, it's different
                if args[0] == 'sharp':  # check, which modified values we wanna use
                    chromatic_scale = cls.all_scales[scale_type].notes_sharp
                else:
                    chromatic_scale = cls.all_scales[scale_type].notes_flat
                key_index = chromatic_scale.index(key)
                return chromatic_scale[key_index:] + chromatic_scale[:key_index]  # this return value differs from other
            else:
                return cls.all_scales[scale_type]
        else:
            try:
                return cls.all_scales[scale_type][key]
            except KeyError:
                return cls.registered_scale_types[scale_type](key)

    @property
    def root(self):
        return self.notes[0]

    @property
    def name(self):
        if self.scale_type == 'chromatic':
            return self.scale_type
        return f"{self.root}-{self.scale_type}"

    def __init__(self, key, scale_type=None, *args, **kwargs):
        self.scale_type = scale_type
        self.notes = []  # list of notes: [ ]
        self.scale_factory(key, *args, **kwargs)
        self.all_scales[scale_type][key] = self

    def scale_factory(self, *args, **kwargs):
        """Everything that builds up(initialize) the scale"""
        note_names = kwargs.get('note_names')
        if not note_names:
            note_names = args[0]

        self.notes = self.scale_names_to_scale(note_names)

    @staticmethod
    def scale_names_to_scale(note_names):
        notes = []
        for note_name in note_names.split(','):
            notes.append(Note.get_note(note_name.strip()))
        return notes

    def __repr__(self):
        return f"{self.name}: {self.notes}"

    @classmethod
    def register_scale_type(cls, scale_type, derived_class):
        cls.registered_scale_types[scale_type] = derived_class


class ChromaticScale(Scale):

    def __init__(self):
        self.notes_sharp = self.scale_names_to_scale('C, C#, D, D#, E, F, F#, G, G#, A, A#, B')
        self.notes_flat = self.scale_names_to_scale('C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B')
        super().__init__(None, 'chromatic')
        self.all_scales['chromatic'] = self

    def scale_factory(self, *args, **kwargs):
        self.notes = self.notes_sharp


def create_scales():
    ChromaticScale()


create_scales()

if __name__ == '__main__':
    print()
