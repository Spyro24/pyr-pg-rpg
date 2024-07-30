import pygame as p

class shader():
    def __init__(self, gw,w,h):
        self.shader = [] #contains the backed shader
        self.gw = gw #pygame display like object
        self.shader_type = "init" #contains the type of the shader
        self.known_shaders = ["torch"] #the list ofthe prgrammed shaders
        self.w = w
        self.h = h
        self.state = True
        self.counter = 0
        self.cycle_count = 0
        
    def create(self, pos_aray, shader_type, steps, *args):
        if shader_type not in self.known_shaders:
            raise ValueError("your shader type: '" + str(shader_type) + "' are not known. Follow shaders are available: " + str(self.known_shaders))
        elif shader_type == "torch":
            self.shader_type = "torch"
            sample_steps = args[0] #how many steps the shader has
            min_range = args[1] #the minimum range of a torch
            max_range = args[2] #the maximum range of a torch
            min_b = args[3] #the minimum brightness of a torch
            max_b = args[4] #the maximum brighness of a torch
            col = args[5] # the shader color
            b_range = max_b - min_b
            b_step = max_range - min_range
            b_b_step = b_range / b_step
            r,g,b = col
            cur_b = min_b
            for bake in range(b_step):
                cur_shader = p.Surface((self.w,self.h),flags=p.SRCALPHA)
                cur_shader.fill((r,g,b,max_b))
                for torch in pos_aray:
                    x,y = torch
                    p.draw.rect(cur_shader,(r,g,b,cur_b),p.Rect(x,y,(max_range * 2 + 1) - 2*bake,(max_range * 2 + 1) - 2*bake))
                self.shader.append(cur_shader.copy())
            self.cycle_count = len(self.shader) - 1
            self.counter = 0
        
    
    def render(self):
        self.gw.blit(p.transform.scale(self.shader[self.counter],self.gw.get_size()), (0, 0))
        print(self.counter)
        if self.shader_type == "torch":
            if self.state:
                self.counter += 1
            else:
                self.counter -= 1
            if self.counter >= self.cycle_count:
                self.state = False
            elif self.counter <= 0:
                self.state = True