import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


stop = str(input('Digite stop para parar!'))
if stop == stop:
    quit()