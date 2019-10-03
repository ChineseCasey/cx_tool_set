import sys,os

def run():
    sys.path.append(os.path.dirname(__file__))
    import ID_window.ID_main_Window;ID_window.ID_main_Window.run()