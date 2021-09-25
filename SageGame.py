#Author: FunnybunnyofDOOM
#Created: 9/24/2021
#Language: Python 3.0
#Contact: Funnybunnyofdoom@gmail.com

# Simple pygame program to display images upon keys being pressed


# Import and initialize the pygame library
import pygame, sys, os
from pygame.locals import *
pygame.init()

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'SageGameIMG') # The resource folder path

infoObject = pygame.display.Info() #Get the display info object
width = infoObject.current_w #Get the width and height from the info object
height = infoObject.current_h
fullscreen_image_size = (width, height)

bg = pygame.image.load(os.path.join(resource_path, "keyboard.png"))
bg = pygame.transform.scale(bg, fullscreen_image_size)
q = pygame.image.load(os.path.join(resource_path, "key_q.png"))
q = pygame.transform.scale(q, fullscreen_image_size)
w = pygame.image.load(os.path.join(resource_path, "key_w.png"))
w = pygame.transform.scale(w, fullscreen_image_size)
e = pygame.image.load(os.path.join(resource_path, "key_e.png"))
e = pygame.transform.scale(e, fullscreen_image_size)
r = pygame.image.load(os.path.join(resource_path, "key_r.png"))
r = pygame.transform.scale(r, fullscreen_image_size)
t = pygame.image.load(os.path.join(resource_path, "key_t.png"))
t  = pygame.transform.scale(t, fullscreen_image_size)
y = pygame.image.load(os.path.join(resource_path, "key_y.png"))
y  = pygame.transform.scale(y, fullscreen_image_size)
u = pygame.image.load(os.path.join(resource_path, "key_u.png"))
u  = pygame.transform.scale(u, fullscreen_image_size)
i = pygame.image.load(os.path.join(resource_path, "key_i.png"))
i = pygame.transform.scale(i, fullscreen_image_size)
o = pygame.image.load(os.path.join(resource_path, "key_o.png"))
o = pygame.transform.scale(o, fullscreen_image_size)
p = pygame.image.load(os.path.join(resource_path, "key_p.png"))
p = pygame.transform.scale(p, fullscreen_image_size)
a = pygame.image.load(os.path.join(resource_path, "key_a.png"))
a = pygame.transform.scale(a, fullscreen_image_size)
s = pygame.image.load(os.path.join(resource_path, "key_s.png"))
s = pygame.transform.scale(s, fullscreen_image_size)
d = pygame.image.load(os.path.join(resource_path, "key_d.png"))
d = pygame.transform.scale(d, fullscreen_image_size)
f = pygame.image.load(os.path.join(resource_path, "key_f.png"))
f = pygame.transform.scale(f, fullscreen_image_size)
g = pygame.image.load(os.path.join(resource_path, "key_g.png"))
g = pygame.transform.scale(g, fullscreen_image_size)
h = pygame.image.load(os.path.join(resource_path, "key_h.png"))
h = pygame.transform.scale(h, fullscreen_image_size)
j = pygame.image.load(os.path.join(resource_path, "key_j.png"))
j = pygame.transform.scale(j, fullscreen_image_size)
k = pygame.image.load(os.path.join(resource_path, "key_k.png"))
k = pygame.transform.scale(k, fullscreen_image_size)
l = pygame.image.load(os.path.join(resource_path, "key_l.png"))
l = pygame.transform.scale(l, fullscreen_image_size)
z = pygame.image.load(os.path.join(resource_path, "key_z.png"))
z = pygame.transform.scale(z, fullscreen_image_size)
x = pygame.image.load(os.path.join(resource_path, "key_x.png"))
x = pygame.transform.scale(x, fullscreen_image_size)
c = pygame.image.load(os.path.join(resource_path, "key_c.png"))
c = pygame.transform.scale(c, fullscreen_image_size)
v = pygame.image.load(os.path.join(resource_path, "key_v.png"))
v = pygame.transform.scale(v, fullscreen_image_size)
b = pygame.image.load(os.path.join(resource_path, "key_b.png"))
b = pygame.transform.scale(b, fullscreen_image_size)
n = pygame.image.load(os.path.join(resource_path, "key_n.png"))
n = pygame.transform.scale(n, fullscreen_image_size)
m = pygame.image.load(os.path.join(resource_path, "key_m.png"))
m = pygame.transform.scale(m, fullscreen_image_size)
k0 = pygame.image.load(os.path.join(resource_path, "key_0.png"))
k0 = pygame.transform.scale(k0, fullscreen_image_size)
k1 = pygame.image.load(os.path.join(resource_path, "key_1.png"))
k1 = pygame.transform.scale(k1, fullscreen_image_size)
k2 = pygame.image.load(os.path.join(resource_path, "key_2.png"))
k2 = pygame.transform.scale(k2, fullscreen_image_size)
k3 = pygame.image.load(os.path.join(resource_path, "key_3.png"))
k3 = pygame.transform.scale(k3, fullscreen_image_size)
k4 = pygame.image.load(os.path.join(resource_path, "key_4.png"))
k4 = pygame.transform.scale(k4, fullscreen_image_size)
k5 = pygame.image.load(os.path.join(resource_path, "key_5.png"))
k5 = pygame.transform.scale(k5, fullscreen_image_size)
k6 = pygame.image.load(os.path.join(resource_path, "key_6.png"))
k6 = pygame.transform.scale(k6, fullscreen_image_size)
k7 = pygame.image.load(os.path.join(resource_path, "key_7.png"))
k7 = pygame.transform.scale(k7, fullscreen_image_size)
k8 = pygame.image.load(os.path.join(resource_path, "key_8.png"))
k8 = pygame.transform.scale(k8, fullscreen_image_size)
k9 = pygame.image.load(os.path.join(resource_path, "key_9.png"))
k9 = pygame.transform.scale(k9, fullscreen_image_size)
alt = pygame.image.load(os.path.join(resource_path, "key_alt.png"))
alt = pygame.transform.scale(alt, fullscreen_image_size)
backspace = pygame.image.load(os.path.join(resource_path, "key_backspace.png"))
backspace = pygame.transform.scale(backspace, fullscreen_image_size)
capslock = pygame.image.load(os.path.join(resource_path, "key_capslock.png"))
capslock = pygame.transform.scale(capslock, fullscreen_image_size)
ctrl = pygame.image.load(os.path.join(resource_path, "key_ctrl.png"))
ctrl = pygame.transform.scale(ctrl, fullscreen_image_size)
delete = pygame.image.load(os.path.join(resource_path, "key_delete.png"))
delete = pygame.transform.scale(delete, fullscreen_image_size)
down = pygame.image.load(os.path.join(resource_path, "key_down.png"))
down = pygame.transform.scale(down, fullscreen_image_size)
end = pygame.image.load(os.path.join(resource_path, "key_end.png"))
end = pygame.transform.scale(end, fullscreen_image_size)
enter = pygame.image.load(os.path.join(resource_path, "key_enter.png"))
enter = pygame.transform.scale(enter, fullscreen_image_size)
home = pygame.image.load(os.path.join(resource_path, "key_home.png"))
home = pygame.transform.scale(home, fullscreen_image_size)
insert = pygame.image.load(os.path.join(resource_path, "key_insert.png"))
insert = pygame.transform.scale(insert, fullscreen_image_size)
left = pygame.image.load(os.path.join(resource_path, "key_left.png"))
left = pygame.transform.scale(left, fullscreen_image_size)
printscreen = pygame.image.load(os.path.join(resource_path, "key_printscreen.png"))
printscreen = pygame.transform.scale(printscreen, fullscreen_image_size)
right = pygame.image.load(os.path.join(resource_path, "key_right.png"))
right = pygame.transform.scale(right, fullscreen_image_size)
shift = pygame.image.load(os.path.join(resource_path, "key_shift.png"))
shift = pygame.transform.scale(shift, fullscreen_image_size)
space = pygame.image.load(os.path.join(resource_path, "key_space.png"))
space = pygame.transform.scale(space, fullscreen_image_size)
tab = pygame.image.load(os.path.join(resource_path, "key_tab.png"))
tab = pygame.transform.scale(tab, fullscreen_image_size)
symbols = pygame.image.load(os.path.join(resource_path, "key_symbols.png"))
symbols = pygame.transform.scale(symbols, fullscreen_image_size)
up = pygame.image.load(os.path.join(resource_path, "key_up.png"))
up = pygame.transform.scale(up, fullscreen_image_size)


CLOCK = 70
CLOCK2 = 12

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
#(width, height) = (450, 450)

screen = pygame.display.set_mode((0, 0), FULLSCREEN)
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

