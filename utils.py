import cv2

WIDTH, HEIGHT = 107, 48

def check_parking_space(img, positions):
    space_counter = 0

    for pos in positions:
        x, y = pos

        img_crop = img[y:y + HEIGHT, x:x + WIDTH]

        gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)

        # 🔥 Improve preprocessing
        blur = cv2.GaussianBlur(gray, (5, 5), 1)
        _, thresh = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY_INV)

        # 🔥 Morphological cleanup
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        thresh = cv2.dilate(thresh, kernel, iterations=1)

        count = cv2.countNonZero(thresh)

        # 🔥 Tuned threshold
        if count < 4700:
            color = (0, 255, 0)
            thickness = 3
            space_counter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, (x, y), (x + WIDTH, y + HEIGHT), color, thickness)

    return img, space_counter