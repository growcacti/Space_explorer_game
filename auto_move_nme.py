            pops = player.position
            fpos = nme.position
            nme2.FollowMe(pops, fpos)
            offset = (nme.x - player.x), (nme.y - player.y)
            
            if moving_object_mask.overlap(obstacle_mask, offset):
                projectiles.append(Projectile(nme.position
                - (nme.rect.width / 2, nme.rect.height / 2), nme.direction))
                for projectile in projectiles:
                    projectile.draw(screen) 

                for projectile in projectiles[:]:
                    projectile.update()
                    if not bg.get_rect().collidepoint(projectile.pos):
                        projectiles.remove(projectile)
        
            nme.offset = pg.Vector2((nme.position[0] - 600), (nme.position[1] - 400))
            nme.angle = player.angle
          
            if nme.offset[0] > player.position[0]:
                nme.velocity.x += nme.thrust
               

            if nme.offset[0] < player.position[0]:
               
                nme.velocity.x -= nme.thrust    

            if nme.offset[1] > player.position[1]:
                
                nme.velocity.y += nme.thrust
                


            if nme.offset[1] < player.position[1]:
           
                nme.velocity.y -= nme.thrust    

            if nme.position[0] >  2 * player.position[0]:
                nme.angle = player.angle + 180
                nme.velocity.x -= nme.thrust
            if nme.position[1] < player.position[1]:
                nme.angle = player.angle + 180
                nme.velocity.y += nme.thrust

          
            if nme2.position[0] < player.position[0]:
                nme2.velocity.x += nme2.thrust


            if nme2.position[0] > player.position[0]:
                nme2.angle = player.angle
                nme2.velocity.x += nme2.thrust    

            if nme2.position[1] < player.position[1]:
                nme2.angle = nme.angle
                nme2.velocity.y -= nme2.thrust
                


            if nme2.position[1] > player.position[1]:
                nme2.angle = player.angle - 90
                nme2.velocity.y += nme2.thrust    

            if nme2.position[0] >  2 * player.position[0]:
                nme2.angle = nme2.angle + 180
                nme2.velocity.x -= nme2.thrust
            if nme2.position[1] < player.position[1]:
                nme2.angle = player.angle + 180
                nme2.velocity.y += nme2.thrust


