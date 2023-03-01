import pygame
from constants import *
from helpers import screen
from classes.Comment import Comment


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, image_src, location, description):
        self.image_src = image_src
        self.location = location
        self.description = description
        image = pygame.image.load(image_src)
        image = pygame.transform.scale(image,(POST_WIDTH,POST_HEIGHT))
        self.image = image
        self.likes_counter = 0
        self.comments = []           #סוגרים מרובעות הופכת את המשתנה לרשימה
        self.comments_display_index = 0       #זה מספר



        #TODO: write me!
        pass

    def display(self):

        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        screen.blit(self.image, (POST_X_POS,POST_Y_POS))
        pass

    def display_header(self):
        font_location = pygame.font.SysFont("ariel",15)
        display_to_location = font_location.render(self.location, True,  (134 ,134 ,134))
        screen.blit(display_to_location,[LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS])

        front_image = pygame.font.SysFont("ariel",15)
        text_image = front_image.render(self.description, True, (50,50,50))
        screen.blit(text_image, [DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS])

        pass
    def display_likes(self):
        massage = "Liked by {} users".format(self.likes_counter)
        font = pygame.font.SysFont("ariel", 15)
        text = font.render(massage, True,(0,0,0))
        screen.blit(text, [LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS])

    def add_like(self):

        self.likes_counter += 1

    def add_comment(self, comment_text):
        comment1 = Comment(comment_text )
        self.comments.append(comment1)












    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



