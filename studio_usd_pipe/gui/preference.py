#!/usr/bin/python

import sys
from PySide2 import QtWidgets

from studio_usd_pipe.utils import smaya
from studio_usd_pipe.resource.ui import preference


def show_window(standalone=False):    
    if not standalone:        
        main_window = smaya.get_qwidget()
        # main_window = None
        smaya.remove_exists_window('widget_preferences')        
        my_window = preference.Window(
            parent=main_window,
            type='preference',
            value=None,
            title='Preference',
            width=570,
            height=314)
        my_window.show()
    if standalone:
        # if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        my_window = preference.Window(
            parent=None,
            type='preferences',
            value=None,
            title='Preferences',
            width=570,
            height=314
            )
        my_window.show()
        sys.exit(app.exec_())
    