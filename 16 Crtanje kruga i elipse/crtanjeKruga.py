import pygame as pg
pg.init()
(sirina,visina)=(200,200)
prozor = pg.display.set_mode((sirina,visina))
pg.display.set_caption("Crveni krug")
prozor.fill(pg.Color("white"))

#crtanje crvenog kruga
pg.draw.circle(prozor,pg.Color("red"),(100,100),50)

pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()
