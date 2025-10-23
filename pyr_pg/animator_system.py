class bone:
    def __init__(self):
        self.rotation = 0
        self.parentBone: bone
        self.hasParentone = False
        self.midPoint = (0, 0)
        self.childBones = set()