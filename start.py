import pygame as p
from time import sleep

def intro(*param):
    win = param[0]
    ww = param[1]
    rot1 = 0
    rot2 = 0
    c2 = p.transform.scale(p.image.load(param[3] + "intro_c.png"),(param[1] / 20 * 12,param[2] / 20 * 12))
    c1 = p.transform.scale(p.image.load(param[3] + "intro_c.png"),(param[1] / 20 * 14,param[2] / 20 * 14))
    c2_size = c2.get_size()
    c1_size = c1.get_size()
    win.blit(c1,(0,0))
    synth = p.image.load(param[3] + "intro_synth.png")
    proto = p.image.load(param[3] + "intro_proto.png")
    logo = p.image.load(param[3] + "intro_logo.png")
    s_sca = 0
    factor = param[1] / 8
    x_s_p = param[1] / 2
    y_s_p = param[2] / 2
    x_l_p = param[1] / 2
    y_l_p = param[2] / 2
    steps = int(x_s_p - factor) / 30
    c1x= param[1] / 20 * 3
    c1y= param[2] / 20 * 3
    c2x= param[1] / 20 * 4
    c2y= param[2] / 20 * 4
    for n in range(0,20):
        win.fill((0,0,0))
        #c1 rotation
        rc1 = p.transform.rotate(c1, rot1)
        c1bx = c1x - int(((rc1.get_size()[0] - c1_size[0]) / 2))
        c1by = c1y - int(((rc1.get_size()[1] - c1_size[1]) / 2))
        win.blit(rc1,(c1bx,c1by))
        rot1 += 3
        #c2 rotation
        rc2 = p.transform.rotate(c2, rot2)
        c2bx = c2x - int(((rc2.get_size()[0] - c2_size[0]) / 2))
        c2by = c2y - int(((rc2.get_size()[1] - c2_size[1]) / 2))
        win.blit(rc2,(c2bx,c2by))
        rot2 -= 3
        p.display.update()
        sleep(1/160)
        
    for n in range(0,30):
        win.fill((0,0,0))
        s_sca += steps
        x_s_p -= steps / 2
        y_s_p -= steps / 2
        win.blit(p.transform.scale(synth,(s_sca,s_sca)),(x_s_p,y_s_p))
        #c1 rotation
        rc1 = p.transform.rotate(c1, rot1)
        c1bx = c1x - int(((rc1.get_size()[0] - c1_size[0]) / 2))
        c1by = c1y - int(((rc1.get_size()[1] - c1_size[1]) / 2))
        win.blit(rc1,(c1bx,c1by))
        rot1 += 7
        #c2 rotation
        rc2 = p.transform.rotate(c2, rot2)
        c2bx = c2x - int(((rc2.get_size()[0] - c2_size[0]) / 2))
        c2by = c2y - int(((rc2.get_size()[1] - c2_size[1]) / 2))
        win.blit(rc2,(c2bx,c2by))
        rot2 -= 7
        p.display.update()
        sleep(1/160)
        
    cur_sca = s_sca
    k_sca = 0
    k_y_p = y_s_p + s_sca
    for n in range(0,30):
        win.fill((0,0,0))
        s_sca -= steps
        k_sca += steps
        k_y_p -= steps
        win.blit(p.transform.scale(synth,(cur_sca,s_sca)),(x_s_p,y_s_p))
        win.blit(p.transform.scale(proto,(cur_sca,k_sca)),(x_s_p,k_y_p))
        #c1 rotation
        rc1 = p.transform.rotate(c1, rot1)
        c1bx = c1x - int(((rc1.get_size()[0] - c1_size[0]) / 2))
        c1by = c1y - int(((rc1.get_size()[1] - c1_size[1]) / 2))
        win.blit(rc1,(c1bx,c1by))
        rot1 += 20
        #c2 rotation
        rc2 = p.transform.rotate(c2, rot2)
        c2bx = c2x - int(((rc2.get_size()[0] - c2_size[0]) / 2))
        c2by = c2y - int(((rc2.get_size()[1] - c2_size[1]) / 2))
        win.blit(rc2,(c2bx,c2by))
        rot2 -= 20
        p.display.update()
        sleep(1/160)
    
    s_sca = 0
    for n in range(0,30):
        win.fill((0,0,0))
        s_sca += steps
        x_l_p -= steps / 2
        y_l_p -= steps / 2
        win.blit(p.transform.scale(proto,(cur_sca,k_sca)),(x_s_p,k_y_p))
        win.blit(p.transform.scale(logo,(s_sca,s_sca)),(x_l_p,y_l_p))
        #c1 rotation
        rc1 = p.transform.rotate(c1, rot1)
        c1bx = c1x - int(((rc1.get_size()[0] - c1_size[0]) / 2))
        c1by = c1y - int(((rc1.get_size()[1] - c1_size[1]) / 2))
        win.blit(rc1,(c1bx,c1by))
        rot1 += 2
        #c2 rotation
        rc2 = p.transform.rotate(c2, rot2)
        c2bx = c2x - int(((rc2.get_size()[0] - c2_size[0]) / 2))
        c2by = c2y - int(((rc2.get_size()[1] - c2_size[1]) / 2))
        win.blit(rc2,(c2bx,c2by))
        rot2 -= 2
        p.display.update()
        sleep(1/160)

#test code. Remove this before uplad the finish function
win_w = 500
win_h = 500
test_win = p.display.set_mode((win_w, win_h))
intro(test_win, win_h, win_w, "./images/")