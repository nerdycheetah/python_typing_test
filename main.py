import pygame
from pygame.locals import *
import sys
import time
import random

class Type_test:

    def __init__(self):
        self.width = 750
        self.height = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % WPM:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load('type-speed-open.png')
        self.open_img = pygame.transform.scale(self.open_img), (self.w, self.h)

        self.background = pygame.image.load('background.jpg')
        self.background = pygame.transform.scale(self.background, (500, 750))
        
        self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption('Type Speed Test')
        

    def draw_text(self, screen, msg, y, fsize, color):
        # making the font
        font = pygame.font.Font(None, fsize)
        # rendering the text
        text = font.render(msg, 1, color)
        # creating the borders for the typing test
        text_rect = text.get_rect(center=(self.width/2, y))
        # drawing the text and borders to game
        screen.blit(text, text_rect)
        # updating the screen
        pygame.display.update()


    def get_sentence(self):
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence


    def show_results(self, screen):
        if(not self.end):
            self.total_time = time.time() - self.time_start
            
            count = 0
            for i, x in enumerate(self.word):
                try:
                    if self.input_text[i] == x:
                        count += 1
                
                except:
                    pass
            self.accuracy = count/len(self.word) * 100

        self.wpm = len(self.input_text) * 60/(5 * self.total_time)
        self.end = True
        print(self.total_time)

        self.results = 'Time:' + str(round(self.total_time)) + " secs Accuracy:" + str(round(self.accuracy)) + "%" + " WPM: " + str(round(self.wpm))

        self.time_img = pygame.image.load('icon.png')
        self.time_img = pygame.transform.scale(self.time_img, (150, 150))
        screen.blit(self.time_img, (self.width/2-75, self.height-140))
        self.draw_text(screen,"Reset", self.h - 70, 26, (100,100,100))

        print(self.results)
        pygame.display.update()