import pygame

import comon
import GUI

app = comon.App()
app.set_window_mode((0, 0), pygame.FULLSCREEN)
t = comon.Scene()
t.add_node(GUI.Text("1", font_color=(255, 255, 255)))
app.add_scene(t)
app.set_scene(0)

app.run()
