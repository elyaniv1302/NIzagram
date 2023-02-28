import pygame
from constants import *
from helpers import screen

class Comment :
    def __init__(self,text):
        self.text = text

    def display(self,comment_num):
        front_comment = pygame.font.SysFont("ariel", 15)
        text_comment = front_comment.render(self.text, True, (0, 0, 0))
        screen.blit(text_comment, [FIRST_COMMENT_X_POS,FIRST_COMMENT_Y_POS+COMMENT_LINE_HEIGHT*comment_num])
