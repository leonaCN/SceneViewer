# -*- coding: utf-8 -*-
import numpy as np

from .utils import *

class Mesh:

    def __init__(self, vertices, lines=None, triangles=None):
        self.vertices = vertices
        self.lines = lines if lines is not None else []
        self.triangles = triangles if triangles is not None else []


class MeshProxy:

    @classmethod
    def generate_terrain_mesh(cls, resolution: int, length: int, width: int):
        """
        Generate default terrain mesh
        :param resolution: interval of 2 nearby vertices
        :param length: total length of mesh, must be multiple of resolution
        :param width: total width of mesh, must be multiple of resolution
        :return: Mesh object or None(if invalid)
        """
        if length % resolution != 0 or width % resolution != 0:
            return None
        # generate vertices
        x_cnt = length // resolution
        z_cnt = width // resolution
        point_matrix = [[None for i in range(x_cnt)] for j in range(z_cnt)]
        vertices = []
        for x in range(x_cnt):
            for z in range(z_cnt):
                vert = VERTEX_3D(x * resolution, 0, z * resolution)
                vertices.append(vert)
                # save to matrix
                point_matrix[x][z] = vert


        return vertices, point_matrix

    @staticmethod
    def get_point_index(x_coord, z_coord):
        # TODO
        pass
