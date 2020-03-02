from PyQt5 import QtWidgets, uic
import sys

'''
contato jamersonwalderson@gmail.com
Hello world em python usando a biblioteca PyQt5 e QtDesigner

Material usado como apoio:
    PYTHON #1 - Criando O Primeiro Programa - https://www.youtube.com/watch?v=d1uk0Nc1Vgc&t=45s
    Doc - https://www.riverbankcomputing.com/static/Docs/PyQt4/qabstractbutton.html#pressed
    https://medium.com/@wilfilho/pyqt5-o-fantastico-mundo-das-guis-62914b1b39c1
    https://doc.qt.io/archives/qt-4.8/
    http://cta.if.ufrgs.br/projects/visuino/wiki/PyQt
'''

janela = QtWidgets.QApplication(sys.argv)
interface = uic.loadUi('MainWindow.ui')

interface.lbHide.hide()

def quebrar_maldicao():
    interface.lbHelloWorld.setText("Hello world!")
    interface.lbHide.show()

interface.btClick.clicked.connect(quebrar_maldicao)

interface.show()
sys.exit(janela.exec_())
