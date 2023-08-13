from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
import time

def display_windows_loading():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)

    # Define the frames for the Windows-like loading animation (8x8 bitmaps)
    frames = [
        [
            0b11111111,
            0b10000001,
            0b10000001,
            0b10000001,
            0b10000001,
            0b10000001,
            0b10000001,
            0b11111111,
        ],
        [
            0b11111111,
            0b10000001,
            0b10000001,
            0b10000001,
            0b10000001,
            0b10000001,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b10000001,
            0b10000001,
            0b10000001,
            0b10000001,
            0b11111111,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b10000001,
            0b10000001,
            0b10000001,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b10000001,
            0b10000001,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b10000001,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b11100111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b11100111,
            0b11100111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b11100111,
            0b11100111,
            0b11000011,
            0b11111111,
            0b11111111,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b11100111,
            0b11100111,
            0b11000011,
            0b11100111,
            0b11111111,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b11100111,
            0b11100111,
            0b11000011,
            0b11100111,
            0b10000001,
            0b11111111,
            0b11111111,
        ],
        [
            0b11111111,
            0b11100111,
            0b11100111,
            0b11100111,
            0b11000011,
            0b11100111,
            0b10000001,
            0b11111111,
        ],
    ]

    # Loop to display the Windows-like loading animation
    while True:
        for frame in frames:
            with canvas(device) as draw:
                for row in range(8):
                    for col in range(8):
                        draw.point((col, row), fill="white" if (frame[row] >> (7 - col)) & 1 else "black")
            time.sleep(0.6)  # Adjust the interval between frames to control the speed of the animation

# Call the function to display the Windows-like loading animation
display_windows_loading()
