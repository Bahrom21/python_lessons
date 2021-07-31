# ILON OYIN
"""
import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.quit()
quit()
"""
import pygame
pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption("Mening birinchi o`yinim")
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()