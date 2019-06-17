from . import qt_api

if qt_api == 'pyqt':
    from PyQt4.QtWebKit import *

elif qt_api == 'pyqt5':
    
    try:
        from PyQt5.QtWebKitWidgets import *
    except:
        from PyQt5.QtWebEngineWidgets import *
        from PyQt5 import QtWidgets, QtCore
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    from PyQt5.QtWidgets import *    

else:
    from PySide.QtWebKit import *
