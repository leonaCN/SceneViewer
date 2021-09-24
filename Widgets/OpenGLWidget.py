# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from Math3d.utils import *

class OpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(OpenGLWidget, self).__init__(parent)

    def initializeGL(self) -> None:
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)

    def paintGL(self) -> None:
        glMatrixMode(GL_PROJECTION)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)

        p1 = np.array([0.0, 0.0, 0.0])
        p2 = np.array([1.0, 0.0, 0.0])
        p3 = np.array([0.0, 1.0, 0.0])

        vertices = [p1, p2, p3]
        edges = [(p1, p2), (p1, p3), (p2, p3)]
        triangles = [(p1, p2, p3)]

        for edge in edges:
            self.draw_line(edge[0], edge[1])

    def resizeGL(self, w:int, h:int) -> None:
        glViewport(0, 0, w, h)

    def draw_line(self, point_a: np.array, point_b: np.array):
        glBegin(GL_LINES)
        glVertex3f(point_a[0], point_a[1], point_a[2])
        glVertex3f(point_b[0], point_b[1], point_b[2])
        glEnd()