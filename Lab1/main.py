############# Задача 1 ####################

import cv2

############# Задача 2 ####################

#
# folder = 'C:/Users/bigal/PycharmProjects/ATSOM/Lab1/Test/'
#
# img1 = cv2.imread(folder + 'Cat1.jpg', cv2.IMREAD_UNCHANGED)
# img2 = cv2.imread(folder + 'Cat2.png', cv2.IMREAD_ANYDEPTH)
# img3 = cv2.imread(folder + 'Dog1.bmp', cv2.IMREAD_GRAYSCALE)
#
# cv2.namedWindow('Cat1', cv2.WINDOW_NORMAL)
# cv2.namedWindow('Cat2', cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow('Dog1', cv2.WINDOW_FULLSCREEN)
#
# cv2.imshow('Cat1', img1)
# cv2.imshow('Cat2', img2)
# cv2.imshow('Dog1', img3)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


############# Задача 3 ####################

# # Путь
# folder = 'C:/Users/bigal/PycharmProjects/ATSOM/Lab1/Test/'
#
# # Создаем объект VideoCapture для чтения видео из файла
# cap = cv2.VideoCapture(folder + 'video.mp4', cv2.CAP_ANY)
#
#
# # Получаем параметры видео
# fps = cap.get(cv2.CAP_PROP_FPS)  # Частота кадров
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Ширина кадров
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Высота кадров
#
# # Определяем форматы для отображения видео
# formats = [
#     (width, height, cv2.COLOR_BGR2RGB),  # Оригинальный размер, цветовая гамма RGB
#     (int(width / 2), int(height / 2), cv2.COLOR_BGR2GRAY),  # Уменьшенный размер, оттенки серого
#     (int(width * 2), int(height * 2), cv2.COLOR_BGR2HSV)  # Увеличенный размер, цветовая гамма HSV
# ]
#
#
# for new_width, new_height, color_conv in formats: # Отображаем видео в различных форматах
#     window_name = f'Video ({new_width}x{new_height})' # Создаем окно с соответствующим названием
#     cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
#
#     while True:
#         # Читаем очередной кадр видео
#         ret, frame = cap.read()
#         if not ret:
#             break
#
#         # Изменяем размер и цветовую гамму кадра
#         frame = cv2.resize(frame, (new_width, new_height))
#         frame = cv2.cvtColor(frame, color_conv)
#
#         cv2.imshow(window_name, frame)
#
#         if cv2.waitKey(int(1000 / fps)) & 0xFF == 27:
#             break
#
#     # Закрываем окно
#     cv2.destroyWindow(window_name)
#
# cap.release()
# cv2.destroyAllWindows()

############# Задача 4 ####################

# # Путь
# folder = 'C:/Users/bigal/PycharmProjects/ATSOM/Lab1/Test/'
#
# # Создаем объект VideoCapture для чтения видео из файла
# cap = cv2.VideoCapture(folder + 'video.mp4')
#
# # Получаем параметры видео
# fps = cap.get(cv2.CAP_PROP_FPS)  # Частота кадров
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Ширина кадров
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Высота кадров
#
# #Запись выходного видео
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter(folder + 'output_video.avi', fourcc, fps, (width, height))
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

############ Задача 5 ####################

# # Путь
# folder = 'C:/Users/bigal/PycharmProjects/ATSOM/Lab1/Test/'
#
#
# image = cv2.imread(folder + 'Cat1.jpg')
#
# # Перевод изображения в формат HSV
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#
#
# cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
# cv2.namedWindow('HSV Image', cv2.WINDOW_NORMAL)
#
#
# cv2.imshow('Original Image', image)
# cv2.imshow('HSV Image', hsv_image)
#
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()
#

# ############ Задача 6 ####################

# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# # Получение размеров кадра
# frame_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Ширина
# frame_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Высота
#
# # Определение прямоугольных областей
# rectangles = np.array(    [  # значения [x1, y1], [x2, y2]
#     [[  0, 140], [260, 180]],
#     [[110,   0], [150, 140]],
#     [[110, 180], [150, 320]]
# ])
#
# # Вычисление координат центра кадра
# offset_x = frame_w // 2 - rectangles[:, :, 0].max() // 2  # Горизонтальное смещение прямоугольников
# offset_y = frame_h // 2 - rectangles[:, :, 1].max() // 2  # Вертикальное смещение прямоугольников
#
# while True:
#     ret, frame = cap.read()
#
#     height, width, _ = frame.shape  # Получение размеров кадра
#
#     # Применение размытия к определенной области
#     x1, y1 = rectangles[0][0]
#     x2, y2 = rectangles[0][1]
#     mask = np.zeros((frame_h, frame_w, 3), dtype=np.uint8)
#     mask = cv2.rectangle(mask, (x1 + offset_x, y1 + offset_y), (x2 + offset_x, y2 + offset_y), (255, 255, 255), -1)
#     blur = cv2.stackBlur(frame, (63, 63)) # Размытие
#     frame[mask == 255] = blur[mask == 255]
#
#     # Рисование прямоугольных областей
#     for rect in rectangles:
#         x1, y1 = rect[0]
#         x2, y2 = rect[1]
#         cv2.rectangle(frame, (x1 + offset_x, y1 + offset_y), (x2 + offset_x, y2 + offset_y), (255, 0, 0), 2)
#
#     cv2.imshow("Red cross", frame)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()


############# Задача 7 ####################


# older = 'C:/Users/bigal/PycharmProjects/ATSOM/Lab1/Test'
#
# cap = cv2.VideoCapture(0)
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Ширина
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Высота
# fps = cap.get(cv2.CAP_PROP_FPS)
#
# # Запись видео
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Кодек для записи видео в MP4
# out = cv2.VideoWriter('Candy_video.mp4', fourcc, fps, (width, height))
#
# while True:
#     ret, frame = cap.read()
#
#     out.write(frame)  # Запись кадра в выходной видеофайл
#
#     cv2.imshow('Camera', frame)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()
#
# cap = cv2.VideoCapture('Candy_video.mp4')
#
# while True:
#     ret, frame = cap.read()
#
#     if not ret:  # Проверка, есть ли кадры
#         break
#
#     cv2.imshow('Recorded Video', frame)  # Отображение кадра
#
#     if cv2.waitKey(30) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()



############# Задача 8 ####################


# # Открытие камеры
# cap = cv2.VideoCapture(0)
#
# while True:
#
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
#
#     cv2.imshow('Camera', frame)
#
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
#
# cap.release()
# cv2.destroyAllWindows()


############# Задача 9 ####################

# # URL-адрес камеры телефона
# url = 'http://10.131.137.231:8080/video'
#
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
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
#
# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
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
#     # Рисование яблока
#     # Красная часть
#     cv2.ellipse(frame, (center_x, center_y), (50, 60), 0, 0, 360, (0, 0, 255), -1)
#     # Зеленый хвостик
#     cv2.ellipse(frame, (center_x, center_y - 70), (10, 20), 0, 0, 360, (0, 255, 0), -1)
#
#
#     # Вырезание кусочка из яблока
#     # Координаты и размеры кусочка
#     chunk_x = center_x + 20
#     chunk_y = center_y
#     chunk_width = 60
#     chunk_height = 80
#     # Рисование кусочка
#     cv2.ellipse(frame, (chunk_x, chunk_y), (chunk_width // 2, chunk_height // 2), 0, 0, 360, (255, 255, 255), -1)
#
#     cv2.imshow('Camera', frame)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#


