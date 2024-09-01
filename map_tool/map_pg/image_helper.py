import pygame as p

def scale_on_h(p_surface, h_scale):
    x_size, y_size = p_surface.get_size()
    rezise = x_size / y_size
    return p.transform.scale(p_surface,(rezise * h_scale, h_scale))