'''This module contains any configuration variables required for the program to run'''

# External Libraries
import cv2

# Calibration Settings
PIXEL_WIDTHS = [383.5, 378.0, 367.0] # px
PIXEL_HEIGHTS = [44.0, 43.2, 40.0] # px

# Camera Settings
CAM_WIDTH = 1920
CAM_HEIGHT = 1080
CAM_FPS = 30
FRAME_WIDTH = 1440
FRAME_HEIGHT = 1080

# Setup cropped image width
CAM_WIDTH_MIDPOINT = CAM_WIDTH / 2
HALF_FRAME_WIDTH = FRAME_WIDTH / 2
FRAME_WIDTH_START = CAM_WIDTH_MIDPOINT - HALF_FRAME_WIDTH
FRAME_WIDTH_END = CAM_WIDTH_MIDPOINT + HALF_FRAME_WIDTH

# Setup cropped image height
CAM_HEIGHT_MIDPOINT = CAM_HEIGHT / 2
HALF_FRAME_HEIGHT = FRAME_HEIGHT / 2
FRAME_HEIGHT_START = CAM_HEIGHT_MIDPOINT - HALF_FRAME_HEIGHT
FRAME_HEIGHT_END = CAM_HEIGHT_MIDPOINT + HALF_FRAME_HEIGHT

# Lane Settings
LANE_COUNT = 3
LANE_WIDTH = 480
LANE_HEIGHT = 200
LANE_WIDTH_START = [0, 480, 960] # Creating manually for now
LANE_WIDTH_END = [480, 960, 1440]
LANE_HEIGHT_START = [460, 460, 460]
LANE_HEIGHT_END = [650, 650, 650]
EDGE_GAP = 40 # How far roll has to be in to count

# Setup bounding box
LANE_X1 = LANE_WIDTH_START[0] - 10
LANE_Y1 = LANE_HEIGHT_START[0] + EDGE_GAP
LANE_X2 = LANE_WIDTH_END[LANE_COUNT - 1] + 10
LANE_Y2 = LANE_HEIGHT_END[0] - EDGE_GAP
SPLIT_X1 = LANE_WIDTH_START[1]
SPLIT_X2 = LANE_WIDTH_END[1]

# Size Settings - Calibration Settings
ACTUAL_WIDTH = 300.0 # mm
ACTUAL_HEIGHT = 30.0 # mm
WIDTH_RATIOS = [ACTUAL_WIDTH / PIXEL_WIDTHS[0], ACTUAL_WIDTH / PIXEL_WIDTHS[1], ACTUAL_WIDTH / PIXEL_WIDTHS[2]]
HEIGHT_RATIOS = [ACTUAL_HEIGHT / PIXEL_HEIGHTS[0], ACTUAL_HEIGHT / PIXEL_HEIGHTS[1], ACTUAL_HEIGHT / PIXEL_HEIGHTS[2]]

# Draw Settings
FONT = cv2.FONT_HERSHEY_SIMPLEX
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
PASS_FAIL_X = [120, 610, 1080]
PASS_FAIL_Y = [0, 100, 200]

# Threshold Settings
WHITE_THRESH = 228
MIN_AREA = 2000 # Pixels
FAIL_WIDTH_LOW = 260.0 # mm
FAIL_WIDTH_HIGH = 300.0 # mm
FAIL_HEIGHT_LOW = 20.0 # mm
FAIL_HEIGHT_HIGH = 38.0 # mm
LANE_FAIL_WIDTHS_LOW = [FAIL_WIDTH_LOW / WIDTH_RATIOS[0], FAIL_WIDTH_LOW / WIDTH_RATIOS[1], FAIL_WIDTH_LOW / WIDTH_RATIOS[2]]
LANE_FAIL_WIDTHS_HIGH = [FAIL_WIDTH_LOW / WIDTH_RATIOS[0], FAIL_WIDTH_LOW / WIDTH_RATIOS[1], FAIL_WIDTH_LOW / WIDTH_RATIOS[2]]
LANE_FAIL_HEIGHTS_LOW = [FAIL_WIDTH_LOW / HEIGHT_RATIOS[0], FAIL_WIDTH_LOW / HEIGHT_RATIOS[1], FAIL_WIDTH_LOW / HEIGHT_RATIOS[2]]
LANE_FAIL_HEIGHTS_HIGH = [FAIL_WIDTH_LOW / HEIGHT_RATIOS[0], FAIL_WIDTH_LOW / HEIGHT_RATIOS[1], FAIL_WIDTH_LOW / HEIGHT_RATIOS[2]]

# Dev Mode - An array containing options
# Options:
#   pixels - displays pixel dimensions
#   thresh - shows thresh images
#   record  - records video
DEV_MODE = []

def dimension_calc(lane, width, height):
    '''This function takes the pixel width and using the defined ratios converts to mm'''
    converted_width = int(width * WIDTH_RATIOS[lane])
    converted_height = int(height * HEIGHT_RATIOS[lane])
    return '{0}mm x {1}mm'.format(converted_width, converted_height)
