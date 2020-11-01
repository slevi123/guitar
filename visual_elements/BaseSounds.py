from tkinter import Canvas
from services.conversions import hsv_to_hex


class BaseSounds(Canvas):
    def __init__(self, parent, config_parser):
        self.m_width = 600
        self.m_height = 50

        super().__init__(parent, width=self.m_width, height=self.m_height, borderwidth=0, highlightthickness=0)

        self.base_sounds = self.get_basesounds(config_parser)
        self.draw()

    @staticmethod
    def get_basesounds(config):
        return dict(config['SOUNDCOLOR'])

    def draw(self):
        sound_count = len(self.base_sounds)
        part_size = self.m_width / sound_count

        self.draw_color_boxes(sound_count, part_size)
        self.draw_grid(sound_count, part_size)

    def draw_color_boxes(self, sound_count, part_size):
        for i, (key, color) in enumerate(self.base_sounds.items()):
            x_coord = i*part_size
            x_plus_coord = (i+1)*part_size
            color = int(color)
            bg_color = hsv_to_hex(color, 0.5, 0.99)
            fg_color = "#242424"
            self.create_rectangle(x_coord, 0, x_plus_coord, self.m_height, fill=bg_color, outline="")
            self.create_text(x_coord + part_size//2, self.m_height//2, text=key, fill=fg_color,
                             font=('Arial', 30))

    def draw_grid(self, sound_count, part_size):
        for i in range(1, sound_count):
            x_coord = i*part_size
            self.create_line(x_coord, 0, x_coord, self.m_height, fill="#8c887e")




