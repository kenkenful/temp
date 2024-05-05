import platform
from compatilib.windows.WinSystem import WinSystem
from compatilib.windows.WinPart import WinPart

class CVReset():
    def __init__(self):
        pass

    def do_on_windows(self):
        sys = WinSystem()
        part = WinPart()
        sys.func()
        part.func()
        sys.func()

    def do_on_linux(self):
        pass

    def run(self):
        if platform.system() == "Windows":
            self.do_on_windows()
        else:
            self.do_on_linux()

if __name__ == '__main__':
    reset = CVReset()
    reset.run()