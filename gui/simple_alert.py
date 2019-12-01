from tkinter import Tk
from tkinter import messagebox


def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Not a valid alert type.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)


Tk().withdraw()
alert('Hello', 'Hello World')
alert('Hello Again', 'Hello World 2', kind='warning')
