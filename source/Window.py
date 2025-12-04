import win32con
import win32gui

class Window:
    def __init__(self, title: str) -> None:
        self.__title : str = title
        self.__handle: int = self.__get_handle()

        if self.__handle == 0:
            raise Exception("The window could not be found")

    def __get_handle(self) -> int:
        return win32gui.FindWindow(None, self.__title)

    def bring_to_foreground(self) -> None:
        if win32gui.GetForegroundWindow() != self.__handle:
            win32gui.ShowWindow(self.__handle, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(self.__handle)