class Particula:

  def __init__(self,x,y,vx,vy,massa):

    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.massa = massa

  def newton(self,fx,fy,dt):

    ax = fx/self.massa
    ay = fy/self.massa

    self.vx += ax*dt
    self.vy += ay*dt

    self.x += self.vx*dt
    self.y += self.vy*dt

    return self.x, self.y, self.vx, self.vy

p = Particula(0,0,10,10,1)

p.x

p.vy

p.newton(5,9.8,2)
