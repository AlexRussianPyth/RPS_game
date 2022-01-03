import cv2

COLORS = {
    'TEXT_RED' : (0, 0, 200),
    'TEXT_GOLD' : (100, 255, 255),
    'TEXT_BLACK' : (0, 0, 0),
    'TEXT_GREEN' : (0, 180, 0),
}

def write_text(frame, text, text_color, location:int, fontsize=3):
    """This function uses to easily place text in our frame"""

    locations = {
        0 : (int(frame.shape[1]/3), int(frame.shape[0]/2)),
        1 : (30, 30),
        6 : (int(frame.shape[1]/3), int(frame.shape[0] - 50)),
        7 : (30, int(frame.shape[0] - 50))
    }

    cv2.putText(frame, text, locations[location], cv2.FONT_HERSHEY_PLAIN, fontsize, text_color, 4)


def rescaleFrame(frame, scale=0.75):
    """Скейлит фрейм, подходит для изображений, видео и лайвов. В основе лежит cv2.resize()"""
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)