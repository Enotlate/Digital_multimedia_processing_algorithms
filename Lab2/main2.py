############# Задача 1 ####################

# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     cv2.imshow("HSV_image", hsv)
#
#     cv2.imwrite("../Lab2/task_1.png", hsv)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

############# Задача 2 ####################

# import cv2
# import numpy as np
#
#
# # phone_ip = "http://192.168.68.110:8080"
# # video_stream_url = f"{phone_ip}/video"  # Для IP Webcam
# # cap = cv2.VideoCapture(video_stream_url)
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Ошибка подключения к камере!")
#         break
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     lower_red = np.array([0, 120, 220])
#     upper_red = np.array([10, 255, 255])
#
#     mask = cv2.inRange(hsv, lower_red, upper_red)
#     onlyRed_frame = cv2.bitwise_and(frame, frame, mask = mask)
#
#     cv2.imshow('Red Filtered Image', onlyRed_frame)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

############# Задача 3 ####################
#
# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     #Определяем диапазон красного цвета в HSV
#     lower_red = np.array([0, 0, 100])      #Min значения
#     upper_red = np.array([100, 100, 255])  #Max значения
#
#     mask = cv2.inRange(hsv, lower_red, upper_red)
#
#     #Применяем маску на изображение
#     res = cv2.bitwise_and(frame, frame, mask=mask)
#
#     #Структурирующий элемент, определяющий размер и форму области
#     kernel = np.ones((5, 5), np.uint8)
#
#     #Применяем операцию открытия, чтобы удалить шумы и мелкие объекты на изображении
#     opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
#
#     #Применяем операцию закрытия, чтобы заполнить маленькие пробелы и разрывы в объектах на изображении
#     closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)
#
#     cv2.imshow('Opening', opening)
#     cv2.imshow('Closing', closing)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

############# Задача 4-5 ####################

# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     lower_red = np.array([0, 50, 50])
#     upper_red = np.array([10, 255, 255])
#
#     mask = cv2.inRange(hsv, lower_red, upper_red)
#
#     res = cv2.bitwise_and(frame, frame, mask=mask)
#
#     #Вычисляем момент на основе маски
#     moments = cv2.moments(mask)
#
#     #Поиск момента первого порядка
#     area = moments['m00']
#
#     if area > 0:
#         width = height = int(np.sqrt(area))
#
#         #Вычисляем координаты центра объекта на изображении с использованием момент первого порядка
#         c_x = int(moments["m10"] / moments["m00"])
#         c_y = int(moments["m01"] / moments["m00"])
#
#         #Отрисовка прямоугольника
#         color = (0, 0, 0)
#         thickness = 2
#         cv2.rectangle(frame,
#                       (c_x - (width // 8), c_y - (height // 8)),
#                       (c_x + (width // 8), c_y + (height // 8)),
#                       color, thickness)
#
#     cv2.imshow('HSV_frame', hsv)
#     cv2.imshow('Result_frame', frame)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# print("Площадь объекта:", area)
#
# cap.release()
# cv2.destroyAllWindows()