import cv2
import mediapipe as mp
import time
from HandTrackingModule import HandDetector
from gamelogic import RpsGame
from utils import write_text, COLORS

# Main Classes
detector = HandDetector(max_hands=1, detection_confidence=0.7, track_confidence=0.7)
game_engine = RpsGame()

play = True

def capturing():
    """Function, that operates all of the game process"""
    capture = cv2.VideoCapture(0)

    current_time = past_time = 0 # for FPS Counter

    time_start = time.perf_counter()

    while True:

        # Our Frame and Game Board
        istrue, frame = capture.read()
        
        # FPS Counter
        current_time = time.time()
        fps = int(1/(current_time - past_time))
        past_time = current_time 
        write_text(frame, str(fps), COLORS["TEXT_GREEN"], 1, 1)

        # HandDetecting
        detector.find_hands(frame)
        lm_list = detector.find_position(frame, draw=False)

        hand_shape = detector.detect_rps_hand_shape(lm_list)
        
        if lm_list:
            write_text(frame, hand_shape[1], COLORS['TEXT_RED'], 1)
        
        # Timed actions
        time_now = time.perf_counter()
        if time_now - time_start < 4:
            write_text(frame, "Are U Ready?", COLORS['TEXT_RED'], 0)
        elif time_now - time_start < 6:
            write_text(frame, "3!", COLORS['TEXT_RED'], 0)
        elif time_now - time_start < 7:
            write_text(frame, "2!", COLORS['TEXT_RED'], 0)
        elif time_now - time_start < 8:
            write_text(frame, "1!", COLORS['TEXT_RED'], 0)
        else:
            result_frame = game_engine.show_results(frame, hand_shape[0])
            capture.release()
            cv2.imshow('Frame', result_frame)
            cv2.waitKey(5000)
            break
            cv2.destroyAllWindows()

        cv2.imshow('Frame', frame)

        # Exit key "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            global play
            play = False
            break

if __name__ == "__main__":
    while play:
        capturing()
