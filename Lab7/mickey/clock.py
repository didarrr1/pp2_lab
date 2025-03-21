import pygame
import sys
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

body_image = pygame.image.load("mickey_body.png").convert_alpha()
right_hand_image = pygame.image.load("right_hand.png").convert_alpha()
left_hand_image = pygame.image.load("left_hand.png").convert_alpha()

body_rect = body_image.get_rect(center=CENTER)
right_hand_rect = right_hand_image.get_rect(center=CENTER)
left_hand_rect = left_hand_image.get_rect(center=CENTER)

clock = pygame.time.Clock()

def blit_rotate_center(surf, image, origin_pos, angle):
image_rect = image.get_rect(topleft=(origin_pos[0], origin_pos[1]))
offset_center_to_pivot = pygame.math.Vector2(origin_pos) - image_rect.center
rotated_offset = offset_center_to_pivot.rotate(-angle)
rotated_image_center = (origin_pos[0] - rotated_offset.x, origin_pos[1] - rotated_offset.y)
rotated_image = pygame.transform.rotate(image, angle)
rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
surf.blit(rotated_image, rotated_image_rect.topleft)

while True:
for event in pygame.event.get():
        if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

now = datetime.now()
minutes = now.minute
seconds = now.second

    minute_angle = -6 * minutes 
    second_angle = -6 * seconds  

screen.fill((255, 255, 255))

screen.blit(body_image, body_rect.topleft)

blit_rotate_center(screen, right_hand_image, CENTER, minute_angle)
blit_rotate_center(screen, left_hand_image, CENTER, second_angle)

pygame.display.flip()
clock.tick(60)
