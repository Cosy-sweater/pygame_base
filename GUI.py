import pygame
from pygame.locals import *
from typing import Union
from comon import Node

import sys

pygame.font.init()


class Text(Node):
    id = 0
    text_objects = []

    @classmethod
    def delete_by_id(cls, obj_id):
        for item in Text.text_objects:
            if item.id == obj_id:
                Text.text_objects.remove(item)
                del item
                break

    @classmethod
    def get_by_id(cls, obj_id):
        for item in Text.text_objects:
            if item.id == obj_id:
                return item
        sys.stderr.write(f"No Text object found with id({obj_id})\n")

    def __init__(self, text: str, pos: (int, int) = (0, 0), font: Union[str] = None,
                 font_size: int = 16, font_color: (int, int, int) = (0, 0, 0),
                 anchor="topleft", **other):
        self.app = None
        self.id = Text.id
        Text.id += 1
        Text.text_objects.append(self)

        self.text = text
        self.font = font if type(font) is pygame.font else pygame.font.SysFont(font, font_size)
        self.font_size = font_size
        self.font_color = font_color
        self.pos = pos

        self.text_surface = self.font.render(self.text, False, self.font_color)
        self.rect = self.text_surface.get_rect()
        self.rect = self.rect.move(*self.pos)

    def update_object(self):
        self.text_surface = self.font.render(self.text, False, self.font_color)
        self.rect = self.text_surface.get_rect()
        self.rect.move_ip(*self.pos)

    def draw(self) -> None:
        self.app.screen.blit(self.text_surface, self.rect)

    def __repr__(self):
        return f"Text({self.text}, {self.id})"


if __name__ == "__main__":
    Text("1")
    Text("2")
    Text("text")
    print(Text.get_by_id(2))
    Text.delete_by_id(2)
    print(Text.get_by_id(2))
