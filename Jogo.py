from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import os

global alturaJanela, larguraJanela, xpasso, ypasso, x, y, tamanho, xf, yf, texto, yy, xx, tiro, ponto, x1, y1, ypasso, tamanho2, pause

passo = 1
ypasso = 2

size = 10
tamanho = 30
tamanho2 = 15

x = 0
y = 75

x1 = 100
y1 = 90

xf = 250
yf = 75

xx = xf - size - 19
yy = yf - size + 1

ponto = 0

pause = True

tiro = False


def Desenha():

    global tiro

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glBegin(GL_QUADS)  # fundo verde
    glColor3f(0, 0.5, 0)
    glVertex2d(0, 0)
    glVertex2d(0, alturaJanela)
    glVertex2d(larguraJanela, alturaJanela)
    glVertex2d(larguraJanela, 0)
    glEnd()

    glBegin(GL_QUADS)  # linha esq
    glColor3f(1, 0.9, 0.7)
    glVertex2d(x + tamanho / 2 - 1, 0)
    glVertex2d(x + tamanho / 2 - 1, alturaJanela)
    glVertex2d(x + tamanho / 2 + 1, alturaJanela)
    glVertex2d(x + tamanho / 2 + 1, 0)
    glEnd()

    glBegin(GL_QUADS)  # linha meio
    glColor3f(1, 0.9, 0.7)
    glVertex2d(x1 + tamanho2 / 2 - 1, 0)
    glVertex2d(x1 + tamanho2 / 2 - 1, alturaJanela)
    glVertex2d(x1 + tamanho2 / 2 + 1, alturaJanela)
    glVertex2d(x1 + tamanho2 / 2 + 1, 0)
    glEnd()

    # alvo1

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2d(x, y)
    glVertex2d(x, y + tamanho)
    glVertex2d(x + tamanho, y + tamanho)
    glVertex2d(x + tamanho, y)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex2d(x + tamanho * 0.15, y + tamanho * 0.15)
    glVertex2d(x + tamanho * 0.15, y + tamanho * 0.85)
    glVertex2d(x + tamanho * 0.85, y + tamanho * 0.85)
    glVertex2d(x + tamanho * 0.85, y + tamanho * 0.15)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2d(x + tamanho * 0.3, y + tamanho * 0.3)
    glVertex2d(x + tamanho * 0.3, y + tamanho * 0.7)
    glVertex2d(x + tamanho * 0.7, y + tamanho * 0.7)
    glVertex2d(x + tamanho * 0.7, y + tamanho * 0.3)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex2d(x + tamanho * 0.45, y + tamanho * 0.45)
    glVertex2d(x + tamanho * 0.45, y + tamanho * 0.55)
    glVertex2d(x + tamanho * 0.55, y + tamanho * 0.55)
    glVertex2d(x + tamanho * 0.55, y + tamanho * 0.45)
    glEnd()

    # alvo 2

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2d(x1, y1)
    glVertex2d(x1, y1 + tamanho2)
    glVertex2d(x1 + tamanho2, y1 + tamanho2)
    glVertex2d(x1 + tamanho2, y1)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex2d(x1 + tamanho2 * 0.15, y1 + tamanho2 * 0.15)
    glVertex2d(x1 + tamanho2 * 0.15, y1 + tamanho2 * 0.85)
    glVertex2d(x1 + tamanho2 * 0.85, y1 + tamanho2 * 0.85)
    glVertex2d(x1 + tamanho2 * 0.85, y1 + tamanho2 * 0.15)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2d(x1 + tamanho2 * 0.3, y1 + tamanho2 * 0.3)
    glVertex2d(x1 + tamanho2 * 0.3, y1 + tamanho2 * 0.7)
    glVertex2d(x1 + tamanho2 * 0.7, y1 + tamanho2 * 0.7)
    glVertex2d(x1 + tamanho2 * 0.7, y1 + tamanho2 * 0.3)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex2d(x1 + tamanho2 * 0.45, y1 + tamanho2 * 0.45)
    glVertex2d(x1 + tamanho2 * 0.45, y1 + tamanho2 * 0.55)
    glVertex2d(x1 + tamanho2 * 0.55, y1 + tamanho2 * 0.55)
    glVertex2d(x1 + tamanho2 * 0.55, y1 + tamanho2 * 0.45)
    glEnd()

    glBegin(GL_QUADS)  # cara
    glColor3f(1, 0.7, 0.5)
    glVertex2d(xf - 5, yf)
    glVertex2d(xf - 5, yf - size)
    glVertex2d(xf - size - 5, yf - size)
    glVertex2d(xf - size - 5, yf)
    glEnd()

    glBegin(GL_QUADS)  # olho
    glColor3f(0, 0, 0)
    glVertex2d(xf - size - 2, yf - 4)
    glVertex2d(xf - size - 2, yf - 2)
    glVertex2d(xf - size - 4, yf - 2)
    glVertex2d(xf - size - 4, yf - 4)
    glEnd()

    glBegin(GL_QUADS)  # nariz
    glColor3f(1, 0.7, 0.5)
    glVertex2d(xf - size - 5, yf - 6)
    glVertex2d(xf - size - 5, yf - 4)
    glVertex2d(xf - size - 7, yf - 4)
    glVertex2d(xf - size - 7, yf - 6)
    glEnd()

    glBegin(GL_QUADS)  # parte inferior do chapeu
    glColor3f(0.4, 0.3, 0.3)
    glVertex2d(xf - 3, yf)
    glVertex2d(xf - 3, yf + 2)
    glVertex2d(xf - size - 7, yf + 2)
    glVertex2d(xf - size - 7, yf)
    glEnd()

    glBegin(GL_QUADS)  # parte superior do chapeu
    glColor3f(0.4, 0.3, 0.3)
    glVertex2d(xf - 5, yf + 2)
    glVertex2d(xf - 5, yf + 5)
    glVertex2d(xf - size - 5, yf + 5)
    glVertex2d(xf - size - 5, yf + 2)
    glEnd()

    glBegin(GL_QUADS)  # tronco
    glColor3f(0.3, 0.6, 1)
    glVertex2d(xf - 6, yf - size)
    glVertex2d(xf - 6, yf - size - 12)
    glVertex2d(xf - size - 4, yf - size - 12)
    glVertex2d(xf - size - 4, yf - size)
    glEnd()

    glBegin(GL_QUADS)  # perna esquerda
    glColor3f(0.1, 0.2, 1)
    glVertex2d(xf - 6, yf - size - 12)
    glVertex2d(xf - 6, yf - size - 18)
    glVertex2d(xf - 9, yf - size - 18)
    glVertex2d(xf - 9, yf - size - 12)
    glEnd()

    glBegin(GL_QUADS)  # perna direita
    glColor3f(0.1, 0.2, 1)
    glVertex2d(xf - 11, yf - size - 12)
    glVertex2d(xf - 11, yf - size - 18)
    glVertex2d(xf - 14, yf - size - 18)
    glVertex2d(xf - 14, yf - size - 12)
    glEnd()

    glBegin(GL_QUADS)  # bota direita
    glColor3f(0.4, 0.3, 0.3)
    glVertex2d(xf - 11, yf - size - 18)
    glVertex2d(xf - 11, yf - size - 21)
    glVertex2d(xf - 14, yf - size - 21)
    glVertex2d(xf - 14, yf - size - 18)
    glEnd()

    glBegin(GL_QUADS)  # bota esquerda
    glColor3f(0.4, 0.3, 0.3)
    glVertex2d(xf - 6, yf - size - 18)
    glVertex2d(xf - 6, yf - size - 21)
    glVertex2d(xf - 9, yf - size - 21)
    glVertex2d(xf - 9, yf - size - 18)
    glEnd()

    glBegin(GL_QUADS)  # braco esquerdo
    glColor3f(0.3, 0.6, 1)
    glVertex2d(xf - size - 4, yf - size)
    glVertex2d(xf - size - 4, yf - size - 3)
    glVertex2d(xf - size - 10, yf - size - 3)
    glVertex2d(xf - size - 10, yf - size)
    glEnd()

    glBegin(GL_QUADS)  # mao esquerda
    glColor3f(1, 0.7, 0.5)
    glVertex2d(xf - size - 12, yf - size)
    glVertex2d(xf - size - 12, yf - size - 3)
    glVertex2d(xf - size - 10, yf - size - 3)
    glVertex2d(xf - size - 10, yf - size)
    glEnd()

    glBegin(GL_QUADS)  # cabo da arma
    glColor3f(0.7, 0.7, 0.7)
    glVertex2d(xf - size - 14, yf - size)
    glVertex2d(xf - size - 14, yf - size - 4)
    glVertex2d(xf - size - 12, yf - size - 4)
    glVertex2d(xf - size - 12, yf - size)
    glEnd()

    glBegin(GL_QUADS)  # corpo da arma
    glColor3f(0.7, 0.7, 0.7)
    glVertex2d(xf - size - 16, yf - size + 2)
    glVertex2d(xf - size - 16, yf - size - 1)
    glVertex2d(xf - size - 12, yf - size - 1)
    glVertex2d(xf - size - 12, yf - size + 2)
    glEnd()

    glBegin(GL_QUADS)  # cano da arma
    glColor3f(0.7, 0.7, 0.7)
    glVertex2d(xf - size - 19, yf - size + 2)
    glVertex2d(xf - size - 19, yf - size)
    glVertex2d(xf - size - 16, yf - size)
    glVertex2d(xf - size - 16, yf - size + 2)
    glEnd()

    glBegin(GL_QUADS)  # braco direito
    glColor3f(0.3, 0.6, 1)
    glVertex2d(xf - 6, yf - size)
    glVertex2d(xf - 6, yf - size - 7)
    glVertex2d(xf - 4, yf - size - 7)
    glVertex2d(xf - 4, yf - size)
    glEnd()

    glBegin(GL_QUADS)  # mao direita
    glColor3f(1, 0.7, 0.5)
    glVertex2d(xf - 6, yf - size - 7)
    glVertex2d(xf - 6, yf - size - 9)
    glVertex2d(xf - 4, yf - size - 9)
    glVertex2d(xf - 4, yf - size - 7)
    glEnd()

    if tiro:
        glBegin(GL_QUADS)  # tiro
        glColor3f(0.2, 0.2, 0.2)
        glVertex2d(xx, yy + 1)
        glVertex2d(xx, yy - 1)
        glVertex2d(xx - 1, yy - 1)
        glVertex2d(xx - 1, yy + 1)
        glEnd()

    glColor3f(0, 0, 0)
    DesenhaTexto(texto)

    glutSwapBuffers()


def DesenhaTexto(string):

    glPushMatrix()

    glRasterPos2f(larguraJanela * 0.18, alturaJanela * 0.95)

    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
    glPopMatrix()


def Timer(value):

    global y, larguraJanela, alturaJanela, passo, tamanho, y1, ypasso

    if y > alturaJanela - tamanho or y < 0:
        passo = -passo

    if y > alturaJanela - tamanho:
        y = alturaJanela - tamanho - 1

    if y < 0:
        y = 0 + 1

    if pause:
        y += passo

    if y1 > alturaJanela - tamanho2 or y1 < 0:
        ypasso = -ypasso

    if y1 > alturaJanela - tamanho2:
        y1 = alturaJanela - tamanho2 - 1

    if y1 < 0:
        y1 = 0 + 1

    if pause:
        y1 += ypasso

    glutPostRedisplay()

    glutTimerFunc(15, Timer, 1)


def Timer2(value):

    global xx, larguraJanela, alturaJanela, xxpasso, tamanho, tiro, xf, x, y, yy, ponto, texto, x1, x2, tamanho2

    if xx <= 0:
        xx = xf - size - 19
        tiro = False
        ponto = 0

    if x + tamanho >= xx >= x and y + tamanho >= yy >= y:
        xx = xf - size - 19
        tiro = False
        ponto += 1

    if x1 + tamanho2 >= xx >= x1 and y1 + tamanho2 >= yy >= y1:
        xx = xf - size - 19
        tiro = False
        ponto += 2

    if tiro:
        if pause:
            xx -= 2

    texto = "Pontuação = " + str(ponto)

    glutPostRedisplay()

    glutTimerFunc(3, Timer2, 1)


def Inicializa():

    global texto, tiro, ponto

    glClearColor(0, 0, 0, 1)

    texto = "Pontuação = 0"


def AlterarTamanhoJanela(w, h):

    global alturaJanela, larguraJanela

    if h == 0:
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    larguraJanela = 250
    alturaJanela = 166.666

    gluOrtho2D(0, larguraJanela, 0, alturaJanela)


def GerenciaMouse(button, state, x, y):

    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            CriaMenu()

    glutPostRedisplay()


def TeclasEspeciais(key, x, y):

    global xf, yf, alturaJanela, tiro, yy

    if key == GLUT_KEY_UP:
        if pause:
            yf = yf + 3
            yy = yf - size + 1
            if yf + 5 > alturaJanela:
                yf = alturaJanela - 5
                yy = yf - size + 1

    if key == GLUT_KEY_DOWN:
        if pause:
            yf = yf - 3
            yy = yf - size + 1
            if yf < 31:
                yf = 31
                yy = yf - size + 1

    if key == GLUT_KEY_LEFT:
        if pause:
            tiro = True

    glutPostRedisplay()


def Menu(op):

    global pause

    if op == 0:
        pause = False

    if op == 1:
        pause = True

    if op == 2:
        #os.system("taskkill /im python.exe")
        quit(main())

    glutPostRedisplay()

    return 0


def MenuPrincipal(op):

    return 0


def CriaMenu():

    submenu1 = glutCreateMenu(Menu)
    glutAddMenuEntry("Pausar", 0)
    glutAddMenuEntry("Iniciar", 1)
    glutAddMenuEntry("Desligar", 2)

    menu = glutCreateMenu(MenuPrincipal)
    glutAddSubMenu("Opcoes", submenu1)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    return 0


def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1200, 800)
    glutInitWindowPosition(50, 0)
    glutCreateWindow(b"Jogo")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlterarTamanhoJanela)
    glutTimerFunc(15, Timer, 1)
    glutTimerFunc(3, Timer2, 1)
    glutSpecialFunc(TeclasEspeciais)
    glutMouseFunc(GerenciaMouse)
    Inicializa()
    glutMainLoop()


main()
