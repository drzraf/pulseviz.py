import threading
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class OpenGLWindow(threading.Thread):
    window_name = 'pulseviz.py'

    def __init__(self, refresh_rate, **kwargs):
        super(OpenGLWindow, self).__init__(**kwargs)
        self.refresh_rate = refresh_rate

    def _display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glutSwapBuffers()

    def _resize(self, width, height):
        self.width = width
        self.height = height
        glViewport(0, 0, width, height)

    def _keypress(self, key, x, y):
        if key == b'q':
            self.quit()

    def _init_opengl(self):
        glutInit(sys.argv)
        glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_CONTINUE_EXECUTION) # TODO
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        glutCreateWindow(self.window_name)
        glutDisplayFunc(self._display)
        glutReshapeFunc(self._resize)
        glutKeyboardFunc(self._keypress)
        glutIdleFunc(self._idle)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)

    def run(self):
        self._init_opengl()
        glutMainLoop()

    def _idle(self):
        time.sleep(1.0 / self.refresh_rate)
        glutPostRedisplay()

    # TODO: Rename this one.
    def quit(self):
        glutLeaveMainLoop()


class OpenGLWindow2D(OpenGLWindow):
    def _resize(self, width, height):
        super(OpenGLWindow2D, self)._resize(width, height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, 0, 128) # TODO: gluOrtho2D?
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
