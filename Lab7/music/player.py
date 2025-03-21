import pygame
import sys
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

music_folder = "music"
music_files = [f for f in os.listdir(music_folder) if f.endswith(('.mp3', '.ogg'))]
current_track = 0

def load_music(index):
    if 0 <= index < len(music_files):
        pygame.mixer.music.load(os.path.join(music_folder, music_files[index]))
        pygame.mixer.music.play()

if music_files:
    load_music(current_track)

font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  
                current_track = (current_track + 1) % len(music_files)
                load_music(current_track)
            elif event.key == pygame.K_b:  
                current_track = (current_track - 1) % len(music_files)
                load_music(current_track)

    screen.fill(WHITE)
    if music_files:
        track_name = os.path.basename(music_files[current_track])
        text = font.render(f"Playing: {track_name}", True, BLACK)
        screen.blit(text, (20, 20))
    else:
        text = font.render("No music files found.", True, BLACK)
        screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(30)
