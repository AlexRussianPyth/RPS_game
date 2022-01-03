import time
import random
from utils import write_text, rescaleFrame, COLORS
import numpy as np
import cv2

class RpsGame:
    
    def computer_move(self):
        """Делает случайный ход"""
        return random.randint(1, 3)

    def choose_winner(self, computer_move, human_move):

        losing_combinations = [(1, 3), (2, 1), (3, 2)]

        if human_move == 0:
            return "Lets Play, Fucker! Move Your Hand!"
        elif computer_move == human_move:
            return "1:1, nutfuck. Kill u next time..."
        elif (computer_move, human_move) in losing_combinations:
            return "More Intelligent Being Won, fucker!"
        else:
            return "Random Fuck destroys the MACHINE?"
             
    def show_results(self, frame, human_move):
        
        c_move = self.computer_move()
        result_message = self.choose_winner(c_move, human_move)

        write_text(frame, result_message, COLORS['TEXT_GREEN'], 7, fontsize=2)

        c_move_img = cv2.imread(f"images/{c_move}.jpg")

        x_offset=400
        y_offset=10
        frame[y_offset:y_offset+c_move_img.shape[0], x_offset:x_offset+c_move_img.shape[1]] = c_move_img

        return frame