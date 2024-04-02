import pygame 
import pywin as pw

test = pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN | pygame.OPENGL | pygame.HWSURFACE)
print(pygame.display.Info())
pw.draw_font(test, 20,3,3, "", (0,0,0))
pygame.display.flip()
pygame.quit()