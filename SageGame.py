#Author: FunnybunnyofDOOM
#Created: 9/24/2021
#Language: Python 3.0
#Contact: Funnybunnyofdoom@gmail.com

# Simple pygame program to display images upon keys being pressed


# Import and initialize the pygame library
import pygame, sys
from pygame.locals import *

bg = pygame.image.load("SageGameIMG\keyboard.png")
q = pygame.image.load("SageGameIMG\key_q.png")
w = pygame.image.load("SageGameIMG\key_w.png")
e = pygame.image.load("SageGameIMG\key_e.png")
r = pygame.image.load("SageGameIMG\key_r.png")
t = pygame.image.load("SageGameIMG\key_t.png")
y = pygame.image.load("SageGameIMG\key_y.png")
u = pygame.image.load("SageGameIMG\key_u.png")
i = pygame.image.load("SageGameIMG\key_i.png")
o = pygame.image.load("SageGameIMG\key_o.png")
p = pygame.image.load("SageGameIMG\key_p.png")
a = pygame.image.load("SageGameIMG\key_a.png")
s = pygame.image.load("SageGameIMG\key_s.png")
d = pygame.image.load("SageGameIMG\key_d.png")
f = pygame.image.load("SageGameIMG\key_f.png")
g = pygame.image.load("SageGameIMG\key_g.png")
h = pygame.image.load("SageGameIMG\key_h.png")
j = pygame.image.load("SageGameIMG\key_j.png")
k = pygame.image.load("SageGameIMG\key_k.png")
l = pygame.image.load("SageGameIMG\key_l.png")
z = pygame.image.load("SageGameIMG\key_z.png")
x = pygame.image.load("SageGameIMG\key_x.png")
c = pygame.image.load("SageGameIMG\key_c.png")
v = pygame.image.load("SageGameIMG\key_v.png")
b = pygame.image.load("SageGameIMG\key_b.png")
n = pygame.image.load("SageGameIMG\key_n.png")
m = pygame.image.load("SageGameIMG\key_m.png")
k0 = pygame.image.load("SageGameIMG\key_0.png")
k1 = pygame.image.load("SageGameIMG\key_1.png")
k2 = pygame.image.load("SageGameIMG\key_2.png")
k3 = pygame.image.load("SageGameIMG\key_3.png")
k4 = pygame.image.load("SageGameIMG\key_4.png")
k5 = pygame.image.load("SageGameIMG\key_5.png")
k6 = pygame.image.load("SageGameIMG\key_6.png")
k7 = pygame.image.load("SageGameIMG\key_7.png")
k8 = pygame.image.load("SageGameIMG\key_8.png")
k9 = pygame.image.load("SageGameIMG\key_9.png")
alt = pygame.image.load("SageGameIMG\key_alt.png")
backspace = pygame.image.load("SageGameIMG\key_backspace.png")
capslock = pygame.image.load("SageGameIMG\key_capslock.png")
ctrl = pygame.image.load("SageGameIMG\key_ctrl.png")
delete = pygame.image.load("SageGameIMG\key_delete.png")
down = pygame.image.load("SageGameIMG\key_down.png")
end = pygame.image.load("SageGameIMG\key_end.png")
enter = pygame.image.load("SageGameIMG\key_enter.png")
home = pygame.image.load("SageGameIMG\key_home.png")
insert = pygame.image.load("SageGameIMG\key_insert.png")
left = pygame.image.load("SageGameIMG\key_left.png")
printscreen = pygame.image.load("SageGameIMG\key_printscreen.png")
right = pygame.image.load("SageGameIMG\key_right.png")
shift = pygame.image.load("SageGameIMG\key_shift.png")
space = pygame.image.load("SageGameIMG\key_space.png")
tab = pygame.image.load("SageGameIMG\key_tab.png")
symbols = pygame.image.load("SageGameIMG\key_symbols.png")
up = pygame.image.load("SageGameIMG\key_up.png")


CLOCK = 7000
CLOCK2 = 1250

keypressed = False
display_q = False
display_w = False
display_e = False
display_r = False
display_t = False
display_y = False
display_u = False
display_i = False
display_o = False
display_p = False
display_a = False
display_s = False
display_d = False
display_f = False
display_g = False
display_h = False
display_j = False
display_k = False
display_l = False
display_z = False
display_x = False
display_c = False
display_v = False
display_b = False
display_n = False
display_m = False
display_0 = False
display_1 = False
display_2 = False
display_3 = False
display_4 = False
display_5 = False
display_6 = False
display_7 = False
display_8 = False
display_9 = False
display_0 = False
display_alt = False
display_backspace = False
display_capslock = False
display_ctrl = False
display_delete = False
display_down = False
display_end = False
display_enter = False
display_home = False
display_insert = False
display_left = False
display_printscreen = False
display_right = False
display_shift = False
display_space = False
display_tab = False
display_symbols = False
display_up = False


timer = 0

background_colour = (255,255,255)
(width, height) = (450, 450)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bunny Keyboard')
screen.fill(background_colour)

pygame.display.flip()






running = True
while running:
    #screen.blit(bg, (0, 0))
    pygame.display.update()
    



#Check for display status of images
    if display_q == True:
        screen.fill(background_colour)
        screen.blit(q, (0, 0))
        pygame.display.update()
    elif display_w == True:
        screen.fill(background_colour)
        screen.blit(w, (0, 0))
        pygame.display.update()
    elif display_e == True:
        screen.fill(background_colour)
        screen.blit(e, (0, 0))
        pygame.display.update()
    elif display_r == True:
        screen.fill(background_colour)
        screen.blit(r, (0, 0))
        pygame.display.update()
    elif display_t == True:
        screen.fill(background_colour)
        screen.blit(t, (0, 0))
        pygame.display.update()
    elif display_y == True:
        screen.fill(background_colour)
        screen.blit(y, (0, 0))
        pygame.display.update()
    elif display_u == True:
        screen.fill(background_colour)
        screen.blit(u, (0, 0))
        pygame.display.update()
    elif display_i == True:
        screen.fill(background_colour)
        screen.blit(i, (0, 0))
        pygame.display.update()
    elif display_o == True:
        screen.fill(background_colour)
        screen.blit(o, (0, 0))
        pygame.display.update()
    elif display_p == True:
        screen.fill(background_colour)
        screen.blit(p, (0, 0))
        pygame.display.update()        
    elif display_a == True:
        screen.fill(background_colour)
        screen.blit(a, (0, 0))
        pygame.display.update()        
    elif display_s == True:
        screen.fill(background_colour)
        screen.blit(s, (0, 0))
        pygame.display.update()        
    elif display_d == True:
        screen.fill(background_colour)
        screen.blit(d, (0, 0))
        pygame.display.update()        
    elif display_f == True:
        screen.fill(background_colour)
        screen.blit(f, (0, 0))
        pygame.display.update()        
    elif display_g == True:
        screen.fill(background_colour)
        screen.blit(g, (0, 0))
        pygame.display.update()        
    elif display_h == True:
        screen.fill(background_colour)
        screen.blit(h, (0, 0))
        pygame.display.update()        
    elif display_j == True:
        screen.fill(background_colour)
        screen.blit(j, (0, 0))
        pygame.display.update()        
    elif display_k == True:
        screen.fill(background_colour)
        screen.blit(k, (0, 0))
        pygame.display.update()        
    elif display_l == True:
        screen.fill(background_colour)
        screen.blit(l, (0, 0))
        pygame.display.update()        
    elif display_z == True:
        screen.fill(background_colour)
        screen.blit(z, (0, 0))
        pygame.display.update()        
    elif display_x == True:
        screen.fill(background_colour)
        screen.blit(x, (0, 0))
        pygame.display.update()        
    elif display_c == True:
        screen.fill(background_colour)
        screen.blit(c, (0, 0))
        pygame.display.update()        
    elif display_v == True:
        screen.fill(background_colour)
        screen.blit(v, (0, 0))
        pygame.display.update()        
    elif display_b == True:
        screen.fill(background_colour)
        screen.blit(b, (0, 0))
        pygame.display.update()        
    elif display_n == True:
        screen.fill(background_colour)
        screen.blit(n, (0, 0))
        pygame.display.update()        
    elif display_m == True:
        screen.fill(background_colour)
        screen.blit(m, (0, 0))
        pygame.display.update()
    elif display_0 == True:
        screen.fill(background_colour)
        screen.blit(k0, (0, 0))
        pygame.display.update()
    elif display_9 == True:
        screen.fill(background_colour)
        screen.blit(k9, (0, 0))
        pygame.display.update()
    elif display_8 == True:
        screen.fill(background_colour)
        screen.blit(k8, (0, 0))
        pygame.display.update()
    elif display_7 == True:
        screen.fill(background_colour)
        screen.blit(k7, (0, 0))
        pygame.display.update()
    elif display_6 == True:
        screen.fill(background_colour)
        screen.blit(k6, (0, 0))
        pygame.display.update()
    elif display_5 == True:
        screen.fill(background_colour)
        screen.blit(k5, (0, 0))
        pygame.display.update()
    elif display_4 == True:
        screen.fill(background_colour)
        screen.blit(k4, (0, 0))
        pygame.display.update()
    elif display_3 == True:
        screen.fill(background_colour)
        screen.blit(k3, (0, 0))
        pygame.display.update()
    elif display_2 == True:
        screen.fill(background_colour)
        screen.blit(k2, (0, 0))
        pygame.display.update()
    elif display_1 == True:
        screen.fill(background_colour)
        screen.blit(k1, (0, 0))
        pygame.display.update()
    elif display_alt == True:
        screen.fill(background_colour)
        screen.blit(alt, (0, 0))
        pygame.display.update()
    elif display_backspace == True:
        screen.fill(background_colour)
        screen.blit(backspace, (0, 0))
        pygame.display.update()
    elif display_capslock == True:
        screen.fill(background_colour)
        screen.blit(capslock, (0, 0))
        pygame.display.update()
    elif display_shift == True:
        screen.fill(background_colour)
        screen.blit(shift, (0, 0))
        pygame.display.update()
    elif display_ctrl == True:
        screen.fill(background_colour)
        screen.blit(ctrl, (0, 0))
        pygame.display.update()
    elif display_delete == True:
        screen.fill(background_colour)
        screen.blit(delete, (0, 0))
        pygame.display.update()
    elif display_down == True:
        screen.fill(background_colour)
        screen.blit(down, (0, 0))
        pygame.display.update()
    elif display_end == True:
        screen.fill(background_colour)
        screen.blit(end, (0, 0))
        pygame.display.update()
    elif display_enter == True:
        screen.fill(background_colour)
        screen.blit(enter, (0, 0))
        pygame.display.update()
    elif display_home == True:
        screen.fill(background_colour)
        screen.blit(home, (0, 0))
        pygame.display.update()
    elif display_insert == True:
        screen.fill(background_colour)
        screen.blit(insert, (0, 0))
        pygame.display.update()
    elif display_left == True:
        screen.fill(background_colour)
        screen.blit(left, (0, 0))
        pygame.display.update()
    elif display_printscreen == True:
        screen.fill(background_colour)
        screen.blit(printscreen, (0, 0))
        pygame.display.update()
    elif display_right == True:
        screen.fill(background_colour)
        screen.blit(right, (0, 0))
        pygame.display.update()
    elif display_space == True:
        screen.fill(background_colour)
        screen.blit(space, (0, 0))
        pygame.display.update()
    elif display_tab == True:
        screen.fill(background_colour)
        screen.blit(tab, (0, 0))
        pygame.display.update()
    elif display_symbols == True:
        screen.fill(background_colour)
        screen.blit(symbols, (0, 0))
        pygame.display.update()
    elif display_up == True:
        screen.fill(background_colour)
        screen.blit(up, (0, 0))
        pygame.display.update()
    else:
        screen.fill(background_colour)
        screen.blit(bg, (0, 0))
        pygame.display.update()

#Check for image timer
    if timer == 0:
        display_q = False
        display_w = False
        display_e = False
        display_r = False
        display_t = False
        display_y = False
        display_u = False
        display_i = False
        display_o = False
        display_p = False
        display_a = False
        display_s = False
        display_d = False
        display_f = False
        display_g = False
        display_h = False
        display_j = False
        display_k = False
        display_l = False
        display_z = False
        display_x = False
        display_c = False
        display_v = False
        display_b = False
        display_n = False
        display_m = False
        display_0 = False
        display_9 = False
        display_8 = False
        display_7 = False
        display_6 = False
        display_5 = False
        display_4 = False
        display_3 = False
        display_2 = False
        display_1 = False
        display_alt = False
        display_backspace = False
        display_capslock = False
        display_ctrl = False
        display_delete = False
        display_down = False
        display_end = False
        display_enter = False
        display_home = False
        display_insert = False
        display_left = False
        display_printscreen = False
        display_right = False
        display_shift = False
        display_space = False
        display_tab = False
        display_symbols = False
        display_up = False
        keypressed = False
        
        
    #Check for timer nnumber
    if timer >= 1:
        timer = timer - 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and keypressed == False:

            if event.key == pygame.K_q:
                display_q = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_w:
                display_w = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_e:
                display_e = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_r:
                display_r = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_t:
                display_t = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_y:
                display_y = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_u:
                display_u = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_i:
                display_i = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_o:
                display_o = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_p:
                display_p = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_a:
                display_a = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_s:
                display_s = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_d:
                display_d = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_f:
                display_f = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_g:
                display_g = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_h:
                display_h = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_j:
                display_j = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_k:
                display_k = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_l:
                display_l = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_z:
                display_z = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_x:
                display_x = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_c:
                display_c = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_v:
                display_v = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_b:
                display_b = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_n:
                display_n = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_m:
                display_m = True
                timer = CLOCK
                keypressed = True
            elif event.key == pygame.K_0:
                display_0 = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_1:
                display_1 = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_2:
                display_2 = True
                timer = CLOCK2
            elif event.key == pygame.K_3:
                display_3 = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_4:
                display_4 = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_5:
                display_5 = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_6:
                display_6 = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_7:
                display_7 = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_8:
                display_8 = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_9:
                display_9 = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_LALT:
                display_alt = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_RALT:
                display_alt = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_BACKSPACE:
                display_backspace = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_CAPSLOCK:
                display_capslock = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_RCTRL:
                display_ctrl = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_LCTRL:
                display_ctrl = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_DELETE:
                display_delete = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_DOWN:
                display_down = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_END:
                display_end = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_RETURN:
                display_return = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_KP_ENTER:
                display_enter = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_HOME:
                display_home = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_INSERT:
                display_insert = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_LEFT:
                display_left = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_PRINT:
                display_printscreen = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_RIGHT:
                display_right = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_LSHIFT:
                display_shift = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_RSHIFT:
                display_shift = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_SPACE:
                display_space = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_TAB:
                display_tab = True
                timer = CLOCK2
                keypressed = True
            elif event.key == pygame.K_UP:
                display_up = True
                timer = CLOCK2
                keypressed = True
                
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

