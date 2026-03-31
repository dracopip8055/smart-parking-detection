import cv2
import pickle
from utils import check_parking_space

# Load parking slot positions
with open('parking_slots.pkl', 'rb') as f:
    positions = pickle.load(f)

# Use image (or replace with video path)
img = cv2.imread('images/parking.jpg')

while True:
    img_copy = img.copy()

    img_out, free_spaces = check_parking_space(img_copy, positions)

    cv2.putText(img_out, f'Free: {free_spaces}/{len(positions)}',
                (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2)

    cv2.imshow("Parking Detection", img_out)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()