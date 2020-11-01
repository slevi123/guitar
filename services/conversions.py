from colorsys import hsv_to_rgb

# def darken(color):
#     kuszob = 50
#     if t:= color + kuszob < 230:
#         return t
#     return color
#

# def hex_and_invert_color(h, s, v):
#     r, g, b = map(lambda num: darken(int(255 - num * 255)), hsv_to_rgb(h / 360.0, s, v))
#
#     return '#%02x%02x%02x' % (r, g, b)

# def hex_and_invert_color(h, s, v):
#     fekete = "#242424"
#     feher = "#ECECEC"
#     if (1-s) + (1-v) <= 1:
#         return fekete
#     return feher


def hsv_to_hex(h, s, v):
    r, g, b = map(lambda num: int(num*255), hsv_to_rgb(h/360.0, s, v))

    return '#%02x%02x%02x' % (r, g, b)