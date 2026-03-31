import cv2
import pickle

positions = []

def mouse_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        positions.append((x, y))

    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(positions):
            px, py = pos
            if px < x < px + 107 and py < y < py + 48:
                positions.pop(i)
                break

    with open('parking_slots.pkl', 'wb') as f:
        pickle.dump(positions, f)

img = cv2.imread('images/parking.jpg')

while True:
    img_copy = img.copy()

    for pos in positions:
        cv2.rectangle(img_copy, pos,
                      (pos[0] + 107, pos[1] + 48),
                      (255, 0, 255), 2)

    cv2.imshow("Mark Parking Slots", img_copy)
    cv2.setMouseCallback("Mark Parking Slots", mouse_click)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()