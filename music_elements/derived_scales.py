from itertools import cycle

from music_elements.note import Note
from music_elements.scales import Scale


class DerivedScale(Scale):
    formula = []

    @staticmethod
    def determine_flat_or_sharp(key):
        return 'sharp'

    def get_base_scale(self, key, mod_type):
        pass

    def scale_factory(self, key=None):
        modification_type = self.determine_flat_or_sharp(key)
        base_scale = self.get_base_scale(key, modification_type)
        base_scale_cycle = cycle(base_scale)
        self.notes = [next(base_scale_cycle)]
        for interval in self.formula:
            for _ in range(interval-1):
                next(base_scale_cycle)
            self.notes.append(next(base_scale_cycle))


class MajorScale(DerivedScale):
    formula_wholes_as_measure = [1, 1, 0.5, 1, 1, 1]  # intervals using whole steps as measure, first note does'nt count
    formula = tuple(map(lambda interval: int(interval / 0.5), formula_wholes_as_measure))

    def __init__(self, key, *args, **kwargs):
        super().__init__(key, 'major', *args, **kwargs)

    @staticmethod
    def determine_flat_or_sharp(key):  # todo: resolve three pair of harmonically equal scales (double b or #)
        if len(key) == 1:
            if key == 'F':
                return 'flat'
            else:
                return 'sharp'
        else:
            if key[1] == 'b':
                return 'flat'
        return 'sharp'

    def get_base_scale(self, key_name, mod_type):
        key = Note.get_note(key_name)
        return Scale.get_scale('chromatic', key, mod_type)


if __name__ == "__main__":
    print(MajorScale('F').notes)
    print(MajorScale('F').notes)
    print(MajorScale('F').notes)
    print(MajorScale('F').notes)
