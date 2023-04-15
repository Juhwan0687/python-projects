from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont

img=Image.open('lion.png')

circle_area=[(0,0),(367,249)]

draw_img=ImageDraw.Draw(img)
draw_img.ellipse(circle_area,outline='yellow')

#img.show()
#img.save('Lion2.png')

img2=Image.open('lion.png')

circle_area=[(240,20),(320,70)]

draw_img=ImageDraw.Draw(img2)
draw_img.ellipse(circle_area,outline='yellow')

circle_area=[(210,58),(238,74)]

draw_img.ellipse(circle_area,fill='yellow',outline='yellow')
circle_area=[(188,72),(203,83)]
draw_img.ellipse(circle_area,fill='yellow',outline='yellow')

c3=Image.open('c3.png')

stx,sty=(265,39)

c3x,c3y=c3.size
msg1='The               is'
msg2='the best!'

mfont=ImageFont.truetype('arial.ttf',10)
m2font=ImageFont.truetype('arial.ttf',12)

draw_img.text((245,36),msg1,(255,255,0),font=mfont,align='Left')
draw_img.text((260,52),msg2,(255,0,0),font=m2font,align='Left')

img2.paste(c3,(stx,sty,stx+c3x,c3y+sty))
#img2.show()
#img2.save('lion3.png')

frame=Image.open('frame.png')
c3.resize((68,41))
img3=Image.open('lion.png')
lix,liy=img3.size
frame.paste(img3,(50,38,lix+50,liy+38))
frame.paste(c3,(220,300,c3x+220,c3y+300))
f=open('description.txt','r')
mfont=ImageFont.truetype('arial.ttf',30)
ex,ey=(300,45)
for i in range(7):
    msg1=f.readline()
    draw_img.text((300,45),msg1,(255,255,0),font=mfont,align='left')
    msg2=f.readline()
    draw_img.text((300,45+10),msg2,(0,255,255),font=mfont,align='left')


frame.save('frame.png')
frame.show()