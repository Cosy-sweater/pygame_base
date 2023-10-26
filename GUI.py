import pygame
from pygame.locals import *
from typing import Union
from comon import Node, App

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

    def __init__(self, text: str = "", pos: (int, int) = (0, 0), font: Union[str] = None,
                 font_size: int = 16, font_color: (int, int, int) = (0, 0, 0),
                 anchor="topleft", **other):
        self.id = Text.id
        Text.id += 1
        Text.text_objects.append(self)

        self.text = text
        self.font = font if type(font) is pygame.font else pygame.font.SysFont(font, font_size)
        self.font_size = font_size
        self.font_color = font_color
        self.pos = pos
        self.anchor = anchor

        self.text_surface = None
        self.rect = None
        self.update_object()

    def update_object(self):
        self.text_surface = self.font.render(self.text, False, self.font_color)
        self.rect = self.text_surface.get_rect()
        exec(f"self.rect.{self.anchor} = self.pos")

    def draw(self) -> None:
        self.app.screen.blit(self.text_surface, self.rect)

    def __repr__(self):
        return f"Text({self.text}, {self.id})"


class FPSCounter(Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, *args):
        self.text = str(int(self.app.get_fps()))
        self.update_object()


class Button(Node):
    id = 0
    button_objects = []

    @classmethod
    def delete_by_id(cls, obj_id):
        for item in Button.button_objects:
            if item.id == obj_id:
                Text.text_objects.remove(item)
                del item
                break

    @classmethod
    def get_by_id(cls, obj_id):
        for item in Button.button_objects:
            if item.id == obj_id:
                return item
        sys.stderr.write(f"No Button object found with id({obj_id})\n")

    def __init__(self,text: Text = "", pos: (int, int) = (0, 0), surface: pygame.Surface = None,
                 anchor="topleft", text_anchor="center", command=lambda *_: None):
        self.id = Button.id
        Button.id += 1
        Button.button_objects.append(self)

        self.surface = surface
        self.pos = pos
        self.anchor = anchor
        self.text_anchor = text_anchor
        if type(text) is Text:
            self.text = text
        else:
            raise TypeError("Button only takes Text objects as text argument")
        self.command = command

        self.rect: pygame.Rect = None
        self.update_object()

    def update_object(self):
        self.rect = self.surface.get_rect()
        self.text.anchor = self.text_anchor
        self.text.pos = self.pos
        exec(f"self.rect.{self.anchor} = self.pos")
        exec(f"self.text.rect.{self.text_anchor} = self.rect.{self.text_anchor}")

    def update(self, dt) -> None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
                exec(self.command)

    def draw(self) -> None:
        self.app.screen.blit(self.surface, self.rect)
        self.text.draw()


class BGPlate(Node):
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], color: tuple[int, int, int], alpha: int=255):
        self.rect = pygame.Rect(pos, size)
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.surface.set_alpha(alpha)

    def draw(self):
        self.app.screen.blit(self.surface, self.rect)
