import pygame as pg

pg.mixer.init()
pg.mixer.music.load('som-de-tropeco-ou-tombo.mp3')
pg.mixer.music.play()

while pg.mixer.music.get_busy():
    pg.time.Clock().tick(10)