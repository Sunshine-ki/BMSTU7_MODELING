MAIN_COLOUR = "#000000"
ADD_COLOUR = "#ffffff"

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800

BORDERS_PART = 0.03
BORDERS_WIDTH = int(WINDOW_WIDTH * BORDERS_PART)
BORDERS_HEIGHT = int(WINDOW_HEIGHT * BORDERS_PART)

MATRIX_PART_WIDTH = 0.7
MATRIX_WIDTH = int(MATRIX_PART_WIDTH * WINDOW_WIDTH)

MATRIX_MAX_SIZE = 10

DATA_PART_WIDTH = 1 - MATRIX_PART_WIDTH - 3 * BORDERS_PART
DATA_PART_HEIGHT = 1 - 2 * BORDERS_PART
DATA_WIDTH = int(DATA_PART_WIDTH * WINDOW_WIDTH)
DATA_HEIGHT = int(DATA_PART_HEIGHT * WINDOW_HEIGHT)

ROWS = 12

MATRIX_FRAME_ROWS = 13
