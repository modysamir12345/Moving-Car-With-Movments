from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *



def draw_XYZ():
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)

    glColor3f(1, 1, 1)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)

    glColor3f(1, 1,1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()

def draw_road():
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex(10, 2, 0)
    glVertex(10, -5, 0)
    glVertex(-50, -5, 0)
    glVertex(-50, 2, 0)
    glEnd()

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 30)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(0.5, 0.5, 0.5, 1)


angle = 0
x = 0
forward = True


def draw():
    global angle
    global x
    global forward
    global z

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    #draw_XYZ()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(10, 0, 0)
    glVertex(10, 0, -0.5)
    glVertex(5, 0, -0.5)
    glVertex(5, 0, 0)
    glEnd()



    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.2, 0)
    glVertex(-20, 3, -4)
    glVertex(-19, 3, -4)
    glVertex(-19, -1, -4)
    glVertex(-20, -1, -4)
    glEnd()
    glLoadIdentity()




    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.2, 0)
    glVertex(-12, 3, -4)
    glVertex(-11, 3, -4)
    glVertex(-11, -1, -4)
    glVertex(-12, -1, -4)
    glEnd()
    glLoadIdentity()



    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(3, 0, 0)
    glVertex(3, 0, -0.5)
    glVertex(-2, 0, -0.5)
    glVertex(-2, 0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-4, 0, 0)
    glVertex(-4, 0, -0.5)
    glVertex(-9, 0, -0.5)
    glVertex(-9, 0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-11, 0, 0)
    glVertex(-11, 0, -0.5)
    glVertex(-16, 0, -0.5)
    glVertex(-16, 0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-18, 0, 0)
    glVertex(-18, 0, -0.5)
    glVertex(-23, 0, -0.5)
    glVertex(-23, 0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(10, 0, 2)
    glVertex(10, 0, 1.5)
    glVertex(5, 0, 1.5)
    glVertex(5, 0, 2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(3, 0, 2)
    glVertex(3, 0, 1.5)
    glVertex(-2, 0, 1.5)
    glVertex(-2, 0, 2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-4, 0, 2)
    glVertex(-4, 0, 1.5)
    glVertex(-9, 0, 1.5)
    glVertex(-9, 0, 2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-11, 0, 2)
    glVertex(-11, 0, 1.5)
    glVertex(-16, 0, 1.5)
    glVertex(-16, 0, 2)
    glEnd()


    glColor3f(0, 0, 0)
    glTranslate(x, 0, z)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glColor3f(1, 1, 1)
    glLoadIdentity()
    glTranslate(x, 5*0.25, z)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)



    glColor3f(0.5, 0.5, 0)
    glLoadIdentity()
    glTranslate(x+0.5*5, -0.5 * 0.25*5, 0.5 * 0.5*5+z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x+0.5*5, -0.5 * 0.25*5, - 0.5 * 0.5*5+z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x - 0.5 * 5, -0.5 * 0.25 * 5, 0.5 * 0.5 * 5+z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x - 0.5 * 5, -0.5 * 0.25 * 5, -0.5 * 0.5 * 5 + z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glColor3f(1, 1, 0)
    glLoadIdentity()
    glTranslate(x + 2.4, 0, 0.5+z)
    glutSolidSphere(0.2, 100, 100)

    glColor3f(1, 1, 0)
    glLoadIdentity()
    glTranslate(x + 2.4, 0, -0.8+z)
    glutSolidSphere(0.2, 100, 100)

    glColor3f(1, 0, 0)
    glLoadIdentity()
    glTranslate(x, 5 * 0.25, -2+z)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(2)

    glColor3f(1, 1, 1)
    glLoadIdentity()
    glTranslate(x, 5 * 0.25, -1+z)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(2)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x, 5 * 0.25, z)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(2)

    glLoadIdentity()
    glTranslate(-x - 0.5, -0.5 * 0.25, - 0.5 - z)
    glutSolidSphere(1.5, 100, 100)

    glutSwapBuffers()

    if forward:
        angle -= 0.001
        x += 0.02
        if x > 5:
            forward = False
    else:
        angle += 0.001
        x -= 0.02
        if x < -5:
            forward = True

def rotate():
    glRotate(90,0,1,0)
    draw()

z =0
def arrowHandler(key,x,y):
    global z
    if key== GLUT_KEY_RIGHT:
        z+=1
    elif key== GLUT_KEY_LEFT:
        z-=1



glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(rotate)
glutIdleFunc(rotate)
glutSpecialFunc(arrowHandler)
glutMainLoop()
