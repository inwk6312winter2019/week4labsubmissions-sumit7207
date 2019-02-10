class point():
	p1=(10,10)

p=point()

#part 1

class rectangle():
	width=200
	height=100
	corner=p.p1

rec=rectangle()

def find_centre(box):
	x=(rec.corner[0]+rec.width)/2
	y=(rec.corner[1]+rec.height)/2
	print('the centre is at: ',(x,y))

find_centre(rec)

#part 2

def move_rectangle(box,dx,dy):
        x=(rec.corner[0]+rec.width)/2+dx
        y=(rec.corner[1]+rec.height)/2+dy
        print('the new centre is at: ',(x,y))

xx=int(input('enter dx '))
yy=int(input('enter dy '))
move_rectangle(rec,xx,yy)


#part 3

rec2=rectangle()
rec2.width=100
rec2.height=50

def new_rectangle(b,dx,dy):
        x=(rec.corner[0]+rec.width)/2+dx
        y=(rec.corner[1]+rec.height)/2+dy
        return (x,y)

print (new_rectangle(rec2,xx,yy))
