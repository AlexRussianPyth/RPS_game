import cv2
import mediapipe as mp
import time


class HandDetector:

    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.track_confidence
        )
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, image, draw=True):
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, hand_landmarks, self.mpHands.HAND_CONNECTIONS)
        return image
    
    def find_position(self, image, hand_number=0, draw=True):

        lm_list = []

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_number]

            for id, lm in enumerate(my_hand.landmark):
                height, width, channels = image.shape
                center_x, center_y = int(lm.x * width), int(lm.y * height)
                lm_list.append([id, center_x, center_y])
                if draw:
                    cv2.circle(image, (center_x, center_y), 5, (255,0,0), 2)

        return lm_list

    def detect_rps_hand_shape(self, lm_list):
        """Returns a list with number for a hand shape and name of a shape, or 0 and 'no shape' string"""

        if lm_list:
            if (lm_list[12][2] - lm_list[8][2]) > 70: 
                return [3, "scissors"]
            elif (lm_list[12][1] - lm_list[0][1]) > 200:
                return [2, "paper"]
            else:
                return [1, "rock"]

        return [0, "no shape"]