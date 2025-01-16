# utils.py
import pygame

def load_image(file_path):
    return pygame.image.load(file_path).convert_alpha()
