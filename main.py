from fastai.vision.all import *
import cv2
import numpy as np
from PIL import Image

learn = load_learner('brainrot_emotion_finder_1.pkl')  
locked_in_img = cv2.imread("locked_in.jpg")
shocked_img = cv2.imread("shocked.png")
freaky_img = cv2.imread("freaky.jpeg")
tongue_img = cv2.imread("tongue.jpeg")

def resize_static(frame, target_shape):
    return cv2.resize(frame, (target_shape[1], target_shape[0]))

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

def get_current_frame(pred_class, frame_shape):
    if pred_class == "locked_in":
        return resize_static(locked_in_img, frame_shape)
    elif pred_class == "shocked":
        return resize_static(shocked_img, frame_shape)
    elif pred_class == "freaky":
        return resize_static(freaky_img, frame_shape)
    elif pred_class == "tongue":
        return resize_static(tongue_img, frame_shape)
    else:
        return 255 * np.ones(frame_shape, dtype=np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    pred_class, pred_idx, probs = learn.predict(img)
    confidence = float(probs[pred_idx]) * 100
    label = f"{pred_class} ({confidence:.1f}%)"

    cv2.putText(frame, label, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    static_frame = get_current_frame(pred_class, frame.shape)

    combined_frame = cv2.hconcat([frame, static_frame])

    cv2.imshow("Brainrot Finder", combined_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()