import keyboard
import pyautogui
import cv2
import numpy as np
import time
import random


def compare_images(image1, image2):
    # Преобразовываем изображения в черно-белый формат
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Вычисляем среднеквадратичную ошибку (MSE) между изображениями
    mse = np.mean((gray1 - gray2) ** 2)
    similarity = 1.0 / (1.0 + mse)  # Используем обратное значение
    return similarity * 1000

def simple_clicks():
    is_paused = True  # Флаг паузы программый
    while True:
        if keyboard.is_pressed('q'):  # Проверяем, нажата ли клавиша Q
            if is_paused:
                is_paused = False
                pyautogui.click(219,334)
            else:
                is_paused = True
            time.sleep(0.3)  # Задержка для избежания множественного восприятия нажатия

        if is_paused:
            continue


        catch_cookie()
def catch_cookie():
    # Загружаем изображение золотой печеньки
    cookie_image = cv2.imread("Gold.png")
    screenshot = pyautogui.screenshot()

        # Преобразуем скриншот в массив numpy и изменяем его размеры
    screenshot_np = np.array(screenshot)
    screenshot_resized = cv2.resize(screenshot_np, (cookie_image.shape[1], cookie_image.shape[0]))

        # Сравниваем изображения печенки
    similarity = compare_images(cookie_image, screenshot_resized)

    # Если сходство больше определенного порога, считаем это золотой печенькой и ловим ее
    if similarity > 5:  # Настройте порог в зависимости от ваших потребностей(По факту бесполезная проверка, но пусть стоит, мне лень убирать)
        # Получаем координаты печеньки на экране
        location = pyautogui.locateOnScreen("Gold.png", confidence=0.6)
        if location is not None:
            # Ловим печеньку
            x, y, _, _ = location
            pyautogui.click(x + 70,y + 70)


    pyautogui.click(219, 334) # Переход на позицию главной печеньки, на которую нужно кликать(не золотая)



# Запускаем функцию ловли печенек
simple_clicks()
