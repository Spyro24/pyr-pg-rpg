import pygame as p

win = p.display.set_mode((512,512))
run=True
bar = p.Rect(5, 5, 50, 20)
render = True
not_move = True
last_m_pos = None

while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    
    m_click = p.mouse.get_pressed()
    m_pos = p.mouse.get_pos()
    
    if not_move:
        if m_click == (True,False,False):
            if bar.collidepoint(m_pos):
                print("mouse in bar")
                last_m_pos = m_pos
                not_move = False
                
    else:
        bar = bar.move(m_pos[0] - last_m_pos[0], m_pos[1] - last_m_pos[1])
        not_move = True
        render = True
        if m_click == (True,False,False):
            if bar.collidepoint(m_pos):
                    print("mouse in bar")
                    last_m_pos = m_pos
                    not_move = False
    
    if render:
        win.fill((0,0,0))
        p.draw.rect(win,(255,100,100),bar)
        render = False
        p.display.flip()
        
p.quit()
    
    
    