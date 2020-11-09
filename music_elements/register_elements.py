from music_elements.derived_scales import MajorScale
from music_elements.note import Note
from music_elements.scales import Scale

Scale.register_scale_type('major', MajorScale)


if __name__ == "__main__":
    # MajorScale('F')
    # MajorScale('C')
    # MajorScale('E')
    # MajorScale('Bb')
    # MajorScale('Db')
    # MajorScale('B')
    MajorScale('F#')
    MajorScale('Gb')
    MajorScale("C#")
    # MajorScale('Cb')
    for key, value in Scale.all_scales['major'].items():
        print(key, value)
