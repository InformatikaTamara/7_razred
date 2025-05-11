import pygame as pg
pg.init()
pg.display.set_caption("Meda")
(sirina,visina)=(400,400)
prozor = pg.display.set_mode((sirina,visina))
prozor.fill(pg.Color("white"))

#Usi
pg.draw.circle(prozor,pg.Color("brown"),(175,50),30)
pg.draw.circle(prozor,pg.Color(240, 220, 130),(175,50),20)

pg.draw.circle(prozor,pg.Color("brown"),(225,50),30)
pg.draw.circle(prozor,pg.Color(240, 220, 130),(225,50),20)

#glava
pg.draw.circle(prozor,pg.Color("brown"),(200,100),50)
pg.draw.ellipse(prozor,pg.Color("white"),(175,70,20,35))
pg.draw.ellipse(prozor,pg.Color("white"),(205,70,20,35))
pg.draw.ellipse(prozor,pg.Color("black"),(178,78,15,25))
pg.draw.ellipse(prozor,pg.Color("black"),(208,78,15,25))

#usta
pg.draw.ellipse(prozor,pg.Color("black"),(175,115,50,20),2)
pg.draw.rect(prozor,pg.Color("brown"),(175,105,50,20))

#njuska
pg.draw.ellipse(prozor,pg.Color("black"),(180,102,40,20))
#ruke
pg.draw.ellipse(prozor,pg.Color("brown"),(110,180,178,40))
#telo
pg.draw.ellipse(prozor,pg.Color("brown"),(150,140,100,200))
pg.draw.ellipse(prozor,pg.Color(240, 220, 130),(170,170,60,160))
#noge
pg.draw.circle(prozor,pg.Color("brown"),(175,350),30)
pg.draw.circle(prozor,pg.Color(240, 220, 130),(175,350),20)

pg.draw.circle(prozor,pg.Color("brown"),(225,350),30)
pg.draw.circle(prozor,pg.Color(240, 220, 130),(225,350),20)



pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

