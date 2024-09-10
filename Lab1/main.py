############# Задача 1 ####################

import cv2

############# Задача 2 ####################

# Расширения 3 шт
# extensions = ['.jpg', '.png', '.bmp']
#
# # Создания окна 3 шт
# window_flags = [cv2.WINDOW_NORMAL, cv2.WINDOW_AUTOSIZE, cv2.WINDOW_FULLSCREEN]
#
# # Чтение изображения 3 шт
# read_flags = [cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED]
#
# image_path = r'Test/Screenshot_1.png'
#
# for ext in extensions:
#     for w_flag in window_flags:
#         for r_flag in read_flags:
#
#             image = cv2.imread(image_path, r_flag)
#
#
#             window_name = f'Image ({ext}, {w_flag}, {r_flag})'
#             cv2.namedWindow(window_name, w_flag)
#
#
#             cv2.imshow(window_name, image)
#
#
#             cv2.waitKey(0)
#
#
#             cv2.destroyWindow(window_name)

############# Задача 3 ####################

# Путь
# video_path = r'C:\Users\bigal\PycharmProjects\ATSOM\Lab1\Test\video.mp4'
#
#
# cap = cv2.VideoCapture(video_path)
#
# # Проверка
# if not cap.isOpened():
#     print("Не удалось открыть видео!")
#     exit()
#
# # Получение параметров видео
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
#
# formats = [
#     (width, height, cv2.COLOR_BGR2RGB),
#     (int(width / 2), int(height / 2), cv2.COLOR_BGR2GRAY),
#     (int(width * 2), int(height * 2), cv2.COLOR_BGR2HSV)
# ]
#
# # Отображение видео
# for new_width, new_height, color_conv in formats:
#     # Создание окна
#     window_name = f'Video ({new_width}x{new_height})'
#     cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
#
#     while True:
#         # Чтение кадра
#         ret, frame = cap.read()
#         if not ret:
#             break
#
#         # Изменение размера и цветов
#         frame = cv2.resize(frame, (new_width, new_height))
#         frame = cv2.cvtColor(frame, color_conv)
#
#
#         cv2.imshow(window_name, frame)
#
#
#         key = cv2.waitKey(int(1000 / fps)) & 0xFF
#         if key == ord('q'):
#             break
#
#
#     cv2.destroyWindow(window_name)
#
#
# cap.release()
# cv2.destroyAllWindows()

############# Задача 4 ####################

# # Путь к исходному видео
# input_video_path = r'C:\Users\bigal\PycharmProjects\ATSOM\Lab1\Test\video.mp4'
#
# # Путь к выходному видео
# output_video_path = r'C:\Users\bigal\PycharmProjects\ATSOM\Lab1\Test\output_video.avi'
#
#
# cap = cv2.VideoCapture(input_video_path)
#
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
#
# #Запись выходного видео
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
#
# # Копирование кадров
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     out.write(frame)
#
#
# cap.release()
# out.release()

############# Задача 5 ####################


# # Путь
# image_path = r'C:\Users\bigal\PycharmProjects\ATSOM\Lab1\Test\Screenshot_1.png'
#

# image = cv2.imread(image_path)
#
# # Перевод изображения в формат HSV
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#

# cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
# cv2.namedWindow('HSV Image', cv2.WINDOW_NORMAL)
#

# cv2.imshow('Original Image', image)
# cv2.imshow('HSV Image', hsv_image)
#
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


############# Задача 6 ####################

#
# # Открытие камеры
# cap = cv2.VideoCapture(0)
#
# while True:

#     ret, frame = cap.read()
#

#     height, width, _ = frame.shape
#
#     # Вычисление координат центра кадра
#     center_x = width // 2
#     center_y = height // 2
#
#     # Рисование красного креста в центре кадра
#     # Горизонтальная линия
#     cv2.rectangle(frame, (center_x - 100, center_y - 10), (center_x + 100, center_y + 10), (0, 0, 255), 0)
#     # Вертикальная линия
#     cv2.rectangle(frame, (center_x - 10, center_y - 100), (center_x + 10, center_y + 100), (0, 0, 255), 0)
#

#     cv2.imshow('Camera', frame)
#

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#

# cap.release()
# cv2.destroyAllWindows()

############# Задача 7 ####################

# import os
#
#
# output_dir = r'C:\Users\bigal\PycharmProjects\ATSOM\Lab1\Test'
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
#
# cap = cv2.VideoCapture(0)
#
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
#
# # Запись видео
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(os.path.join(output_dir, 'output_video.mp4'), fourcc, fps, (width, height))
#
# while True:
#
#     ret, frame = cap.read()
#
#     # Запись кадра в файл
#     out.write(frame)
#
#
#     cv2.imshow('Camera', frame)
#
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Освобождение ресурсов
# cap.release()
# out.release()
# cv2.destroyAllWindows()
#
# # Демонстрация записанного видео
# cap = cv2.VideoCapture(os.path.join(output_dir, 'output_video.mp4'))
#
# while True:
#     # Считывание кадра с видео
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     cv2.imshow('Recorded Video', frame)
#
#     # Уменьшение скорости воспроизведения
#     cv2.waitKey(10)
#
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Освобождение ресурсов
# cap.release()
# cv2.destroyAllWindows()


############# Задача 8 ####################


# # Открытие камеры
# cap = cv2.VideoCapture(0)
#
# while True:

#     ret, frame = cap.read()
#
#     # Получение размеров кадра
#     height, width, _ = frame.shape
#
#     # Вычисление координат центра кадра
#     center_x = width // 2
#     center_y = height // 2
#
#     # Получение значения центрального пикселя
#     center_pixel = frame[center_y, center_x]
#
#     # Определение преобладающего цвета центрального пикселя
#     if center_pixel[2] > center_pixel[1] and center_pixel[2] > center_pixel[0]:
#         # Красный
#         color = (0, 0, 255)
#     elif center_pixel[1] > center_pixel[2] and center_pixel[1] > center_pixel[0]:
#         # Зеленый
#         color = (0, 255, 0)
#     else:
#         # Синий
#         color = (255, 0, 0)
#
#     # Рисование креста в центре кадра
#     # Горизонтальная линия
#     cv2.rectangle(frame, (center_x - 100, center_y - 10), (center_x + 100, center_y + 10), color, -1)
#     # Вертикальная линия
#     cv2.rectangle(frame, (center_x - 10, center_y - 100), (center_x + 10, center_y + 100), color, -1)
#

#     cv2.imshow('Camera', frame)
#

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#

# cap.release()
# cv2.destroyAllWindows()


############# Задача 9 ####################

# # URL-адрес камеры телефона
# url = 'http://10.73.159.42:8080/video'
#

# cap = cv2.VideoCapture(url)
#
# while True:
#     # Считывание кадра с камеры телефона
#     ret, frame = cap.read()
#
#     # Отображение кадра
#     cv2.imshow('Camera', frame)
#

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#

# cap.release()
# cv2.destroyAllWindows()
#


