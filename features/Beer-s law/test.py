from relaxrender.beerlaw.Point2D import Point2D
from relaxrender.beerlaw.Ray import Ray
from relaxrender.beerlaw.Object import Object
from relaxrender.beerlaw.Opengl import opengl
from OpenGL.GLU import *
from OpenGL.GLUT import *
if __name__ == '__main__':
    p1=Point2D(0,0)
    o=Object(4,2,p1,3,4)
    p0=Point2D(-1,0)
    ray=Ray(p0,2,p0,0,o)
    glutInit(sys.argv)  # 初始化
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # 设置显示模式
    glutInitWindowPosition(100, 100)  # 窗口打开的位置，左上角坐标在屏幕坐标
    glutInitWindowSize(900, 600)  # 窗口大小
    glutCreateWindow(b"Function Plotter")  # 窗口名字，二进制
 # 设置当前窗口的显示回调
    glutDisplayFunc(opengl(ray,o).show());
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)    # 设置显示范围
    glutMainLoop()
