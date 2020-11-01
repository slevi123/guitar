from tkinter import Canvas
import configparser
from colorsys import hsv_to_rgb

from services.conversions import hsv_to_hex


class SoundBoard(Canvas):
    def __init__(self, parent, config_parser):
        self.marked_steps = list(map(int, config_parser['SOUNDBOARD']['marked_steps'].split(',')))
        self.guitar_tuning = list(config_parser['SOUNDBOARD']['guitar_tuning'].split(','))
        self.color_lookup = self.get_color_lookup(config_parser)
        self. chromatic_scale = list(self.color_lookup.keys())

        self.box_size = 80
        self.step_count = 22
        self.m_width = self.box_size * self.step_count
        self.m_height = self.box_size*(len(self.guitar_tuning)+1)

        super().__init__(parent, width=self.m_width, height=self.m_height, borderwidth=0, highlightthickness=0)

        self.draw()

    def create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    def draw(self):
        half = self.box_size//2
        self.draw_sounds(half)
        self.draw_string_separators()
        self.draw_step_separators()
        self.draw_marked_steps(half)

    def draw_string_separators(self):
        for i in range(1, 7):
            y_coord = i * self.box_size
            self.create_line(0, y_coord, self.m_width, y_coord)

    def draw_step_separators(self):
        for i in range(1, self.step_count):
            x_coord = i*self.box_size
            self.create_line(x_coord, 0, x_coord, self.m_height, fill="#8c887e")

    def draw_marked_steps(self, half):
        self.create_circle(half, half, half // 2, outline='black', width=2)
        for i in range(self.step_count):
            if i in self.marked_steps:
                self.create_circle(i*self.box_size + half, half, half//3, fill='black')

    def draw_sounds(self, half):
        current_sounds = list(map(lambda x: x.split('/'), self.guitar_tuning))
        for step_counter in range(self.step_count):
            for i, sound in enumerate(current_sounds):
                name = ''.join(sound)
                fg_color = "#242424"
                bg_color = hsv_to_hex(self.color_lookup[sound[0]], 0.08*int(sound[1]), 1)

                self.create_rectangle(step_counter*self.box_size, (i+1)*self.box_size,
                                      (step_counter+1)*self.box_size, (i+2)*self.box_size,
                                      fill=bg_color, outline="")
                self.create_text(step_counter*self.box_size+half, (i+1)*self.box_size+half,
                                 text=name, fill=fg_color, font=('Arial', self.box_size//3))

            for index in range(len(current_sounds)):
                current_sounds[index] = self.count_next_sound(current_sounds[index])

    @staticmethod
    def get_color_lookup(config_parser):
        return dict(map(lambda item: (item[0], int(item[1])), config_parser['SOUNDCOLOR'].items()))

    def count_next_sound(self, sound):
        if sound[0] == 'b':
            return 'c', str(int(sound[1])+1)
        return self.chromatic_scale[self.chromatic_scale.index(sound[0]) + 1], sound[1]
