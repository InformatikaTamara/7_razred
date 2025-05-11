import pygame as pg
pg.init()
pg.display.set_caption("Koncetrični krugovi")
(sirina,visina)=(250,250)
prozor = pg.display.set_mode((sirina,visina))
prozor.fill(pg.Color("white"))

#crtanje crnog kruga
(cx,cy)=(sirina//2,visina//2)
pg.draw.circle(prozor,pg.Color("black"),(cx,cy),125)
#crtanje žutog kruga
pg.draw.circle(prozor,pg.Color("yellow"),(cx,cy),100)
#crtanje crvenog kruga
pg.draw.circle(prozor,pg.Color("red"),(cx,cy),75)
#crtanje zelenog kruga
pg.draw.circle(prozor,pg.Color("green"),(cx,cy),50)


pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()
