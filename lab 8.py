#2 задание
import cv2

cap = cv2.VideoCapture(0)

center_x = 0
center_y = 0
while True:
    success, image = cap.read()
    if not success:
        break

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    #находим контуры
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, a, b = cv2.boundingRect(contour)
            #рисуем прямоугльник вокруг контура
            cv2.rectangle(image, (x, y), (x + a, y + b), (255, 0, 0), 2)
            center_x = x + a // 2
            center_y = y + b // 2
    with open('marker_coordinates.txt', 'a') as file:
        file.write(f'{center_x}, {center_y}\n')


    cv2.imshow('image with label', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()




