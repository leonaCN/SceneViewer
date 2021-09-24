# -*- coding: utf-8 -*-

class VERTEX_3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def toCoordList(self):
        return [self.x, self.y, self.z]


class TRIANGLES:

    def __init__(self, vert_a: VERTEX_3D, vert_b: VERTEX_3D, vert_c: VERTEX_3D):
        self.A = vert_a
        self.B = vert_b
        self.C = vert_c
