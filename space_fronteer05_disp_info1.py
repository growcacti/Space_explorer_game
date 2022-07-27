import pygame as pg
import random
import sys
import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2
import bgp
import get_info
pg.init()
WIDTH = 1200
HEIGHT = 800

bg = bgp.background()
WHITE = (255, 255, 255)
screen = pg.display.set_mode((WIDTH, HEIGHT))


class Player:
    def __init__(
        self, image, x, y, angle=0.0, length=4, max_rotation=10, max_acceleration=5.0):
        self.orig_image = image
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = 450
        self.max_rotation = max_rotation
        self.max_velocity = 220
        self.thrust = 150
        self.sim_inertia = 10  # iner
        self.font = pg.font.Font(None, 18)
        self.acceleration = 0.0
        self.rotation = 0.0
        self.camera = Vector2(0, 0)  # Assigned the camera as an attribute.
        self.direction = Vector2(0, 0)
        
    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(
            -self.max_velocity, min(self.velocity.x, self.max_velocity)
        )

        if self.rotation:
            turning_radius = self.length / tan(radians(self.rotation))
            angular_velocity = self.velocity.x / turning_radius / 2
        else:
            angular_velocity = 0

        vel = self.velocity.rotate(-self.angle) * dt
        self.position += vel
        self.camera += vel  # Update the camera position as well.
        # If you use the rect as the blit position, you should update it, too.
        self.rect.center = self.position
        self.angle += degrees(angular_velocity) * dt
       
        self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        #self.direction = self.angle
        self.direction = pg.Vector2(1, 0).rotate(-self.angle)
        pg.display.set_caption("Space Fronteerer")
 
        text1 = self.font.render("X Y position: " + str(self.rect.center), True, WHITE)
       
        screen.blit(text1, (WIDTH - 200, HEIGHT - 750))
    
        origin = (600, 400)
        destination = self.rect.center
        sp = abs(vel[0] + vel[1]) * 24545 // 1
        distance, angle, x_ref, y_ref, op_ang, project =  get_info.info(origin, destination)
        dist = distance // 1
        text2 = self.font.render("Distance from Start: " + str(dist), True, WHITE)
        screen.blit(text2, (WIDTH - 200, HEIGHT - 780))
        text3 = self.font.render("Angle " + str(angle), True, WHITE)
        screen.blit(text3, (WIDTH - 200, HEIGHT - 770))
        text4 = self.font.render("Projection" + str(project), True, WHITE)
        screen.blit(text4, (WIDTH - 300, HEIGHT - 790))
        text5 = self.font.render("MPH " + str(sp), True, WHITE)
        screen.blit(text5, (WIDTH - 200, HEIGHT - 760))
class Bullet:
    def __init__(self, pos, direction):
        self.x, self.y = pos
        self.pos = self.x, self.y
##        mx1, my1 = pg.mouse.get_pos()
##        mx2, my2 = pg.mouse.get_rel()
##        mx = mx1 * mx2
##        my = my1 * my2
##        self.dir = (mx - self.x, my - self.y)
        self.dir = direction
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
            angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pg.Surface((7, 2)).convert_alpha()
        self.bullet_rect = self.bullet.get_rect(center = self.pos)
        self.bullet.fill((255, 255, 255))
        self.bullet = pg.transform.rotate(self.bullet, angle)
        self.speed = 20
        self.update()
    def update(self):  
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        screen.blit(self.bullet, bullet_rect)
        
class Projectile(pg.sprite.Sprite):
    def __init__(self, pos, direction, dt):
        super().__init__()
        self.image = pg.Surface((8, 8))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.image, pg.Color('red'), (6, 6), 6)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.pos = pg.Vector2(self.rect.center)
        self.update(dt)
    def update(self, dt):
        self.pos += self.direction
        
        
        self.rect.center = self.pos
        if not pg.display.get_surface().get_rect().contains(self.rect):
            self.kill()

    def draw(self):
       
        screen.blit(self.image, self.rect)
        
def main():

        pg.init()
        
        clock = pg.time.Clock()
        ticks = 60
        fps= ticks
        exit = False
        ship = pg.image.load("ship8.png").convert_alpha()
        player = Player(ship, *screen.get_rect().center)
        run = True
    
       

        lasers = []
        bullets = [] 
        pos = player.position
        bullet = Bullet(player.position, player.direction)
        while not exit:
            screen.fill(0)

            dt = clock.tick(fps) / 1000
          
                  # Event queue
            for event in pg.event.get():
                if event.type == pg.QUIT:
                   sys.exit()
                   return
                elif event.type == pg.MOUSEWHEEL:
                    if event.y == 1:
                        player.rotation -= 120 * dt
                    elif event.y == -1:
                        player.rotation += 120 * dt
                
                      # User input & Controls
            pressed = pg.key.get_pressed()
            pressed2 = pg.mouse.get_pressed(num_buttons=5)
            if pressed[pg.K_UP] or pg.mouse.get_pressed()[0]:
                if player.velocity.x < 0:
                    player.acceleration = player.thrust
                else:
                    player.acceleration += 890 * dt
            elif pressed[pg.K_DOWN] or pg.mouse.get_pressed()[1]:
                if player.velocity.x > 0:
                    player.acceleration = -player.thrust
                else:
                    player.acceleration -= 1 * dt

            
               
            elif pressed[pg.K_h]:
                if abs(player.velocity.x) > dt * player.thrust:
                    player.acceleration = -copysign(
                        player.thrust, player.velocity.x
                    )
                else:
                    player.acceleration = -player.velocity.x / dt
            else:
                if abs(player.velocity.x) > dt * player.sim_inertia:
                    player.acceleration = -copysign(
                        player.sim_inertia, player.velocity.x
                    )
                else:
                    if dt != 0:
                        player.acceleration = -player.velocity.x / dt
            player.acceleration = max(
                -player.max_acceleration,
                min(player.acceleration, player.max_acceleration),
            )

            if pressed[pg.K_RIGHT] or event.type == pg.MOUSEWHEEL:
                player.rotation -= 20 * dt
                
            elif pressed[pg.K_LEFT] or pg.mouse.get_pressed(num_buttons=5)[4]:
                player.rotation += 20 * dt
               
            else:
                player.rotation = 0
            player.rotation = max(
                -player.max_rotation,
                min(player.rotation, player.max_rotation),
            )

        

 
            if pressed[pg.K_SPACE]:
                real_pos = pg.Vector2(1,0)
                real_pos = (player.position - (player.rect.width / 8, player.rect.height / 8) - player.camera), 
                laser = Projectile(real_pos, player.direction.normalize(), dt)
                lasers.append(laser)
                laser.draw()
                laser.update(dt)
            player.update(dt)
          
            screen.blit(bg, -player.camera)
            screen.blit(
                player.image,
                player.position
                - (player.rect.width / 2, player.rect.height / 2)
                - player.camera,
            )
            
           
                              
                          # Drawing
                           # Drawing
            
            if pg.mouse.get_pressed()[2]:
                bullets.append(Bullet(player.position
                - (player.rect.width / 8, player.rect.height / 8) - player.camera, player.direction))
                for bullet in bullets:
                    bullet.draw(screen) 

            for bullet in bullets[:]:
                bullet.update()
                if not bg.get_rect().collidepoint(bullet.pos):
                    bullets.remove(bullet)

           
           
            for bullet in bullets:
                bullet.draw(screen) 

        
         

         
           
            pg.display.flip()

        pg.quit()


if __name__ == "__main__":
    main()
    

