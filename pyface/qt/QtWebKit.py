from . import qt_api

if qt_api == 'pyqt':
    from PyQt4.QtWebKit import *

elif qt_api == 'pyqt5':
    from PyQt5.QtWidgets import *
    try:
        from PyQt5.QtWebKitWidgets import *
    except:
        from PyQt5.QtWebEngineWidgets import *

else:
    from PySide.QtWebKit import *
