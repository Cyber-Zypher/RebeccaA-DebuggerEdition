import pymysql.cursors
import random
import speech_recognition as sr
from gtts import gTTS
import os
import requests
from bs4 import BeautifulSoup
import bs4
import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from PIL import Image

def demo(n, block_orientation, rotate, inreverse):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    print("Created device")

    msg = "M E D U S A INFOSYTEMS INDIA"
    print(msg)
    # time.sleep(3)
    show_message(device, msg, fill="white", font=proportional(TINY_FONT), scroll_delay=0.1)
    time.sleep(1)
    title = "R E B E C C A AI"
    print(title)
    # time.sleep(3)
    show_message(device, title, fill="white", font=proportional(TINY_FONT), scroll_delay=0.1)

    #args = parser.parse_args()

    pass

demo(n=1, block_orientation=-90, rotate=0, inreverse=False)



# Connect to the MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Sidharth8',
    db='REBECCA',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def get_response(category):
    # Fetch all responses for the given category from the database
    with conn.cursor() as cursor:
        cursor.execute("SELECT response FROM responses WHERE category=%s", (category,))
        responses = cursor.fetchall()
        if responses:
            return random.choice(responses)['response']
        else:
            return "I don't have a response for that."

def text_to_speech(text):
    # Convert text to speech using gTTS
    tts = gTTS(text, lang='en', slow=False)
    tts.save('response.mp3')
    os.system('mpg321 response.mp3')

def listen_microphone():
    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... Say something!")
        display_smiley_open()
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio).strip().lower()
        print("You:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, speech recognition service is unavailable.")
        return ""
    
def display_smiley_open():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)

    # Define the two smiley faces as 8x8 bitmaps (open mouth and closed mouth)
    smiley_open = [
        0b00111100,
        0b01000010,
        0b10100101,
        0b10000001,
        0b10111101,
        0b10000001,
        0b01000010,
        0b00111100,
    ]

    # Loop to display the animated smiley
        # Display the open mouth smiley
    with canvas(device) as draw:
        for row in range(8):
            for col in range(8):
                draw.point((col, row), fill="white" if (smiley_open[row] >> (7 - col)) & 1 else "black")
    time.sleep(1)

        # Display the closed mouth smiley

def display_smiley_closed():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)
    smiley_closed = [
        0b00111100,
        0b01000010,
        0b10100101,
        0b10000001,
        0b10100101,
        0b10011001,
        0b01000010,
        0b00111100,
    ]
    with canvas(device) as draw:
            for row in range(8):
                for col in range(8):
                    draw.point((col, row), fill="white" if (smiley_closed[row] >> (7 - col)) & 1 else "black")
    time.sleep(1)

def display_dead_face():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)
    dead_face = [
        0b10111101,
        0b01000010,
        0b10100101,
        0b10000001,
        0b10011001,
        0b10100101,
        0b01000010,
        0b00111100,
    ]
    with canvas(device) as draw:
            for row in range(8):
                for col in range(8):
                    draw.point((col, row), fill="white" if (dead_face[row] >> (7 - col)) & 1 else "black")
    time.sleep(1)
        
def led_clear():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)
    device.clear

def display_windows_loading():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=0, rotate=0, blocks_arranged_in_reverse_order=False)

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
            time.sleep(0.6)

def main():
    while True:
        user_input = listen_microphone()

        if 'hello' in user_input or 'hi' in user_input:
            display_smiley_closed()
            response = get_response('greeting')
            # demo(n=1, block_orientation=0, rotate=0, inreverse=False)
        elif 'goodbye' in user_input or 'bye' in user_input or 'see you later' in user_input:
            display_smiley_closed()
            response = get_response('bye')
        elif 'thank you' in user_input or 'thanks' in user_input:
            display_smiley_closed()
            response = get_response('thanks')
        elif 'enable debugging' in user_input:
            response = get_response('debug')
            display_windows_loading()
        elif 'how are you' in user_input:
            display_smiley_closed()
            response = get_response('wellbeing')
        elif 'who are you' in user_input or 'what are you' in user_input or 'who is this' in user_input:
            display_smiley_closed()
            response = get_response('intro')
        elif 'who created you' in user_input or 'who is your father' in user_input or 'who is your god' in user_input:
            display_smiley_closed()
            response = get_response('auth')
        elif 'who is' in user_input or 'what is' in user_input or 'is it' in user_input or 'is there' in user_input or 'was there' in user_input or 'what are' in user_input or 'who are' in user_input or 'where are' in user_input or 'where is' in user_input:
            display_smiley_closed()
            try:
                googlesearch = user_input
                url = f"https://www.google.com/search?q={googlesearch}"
                request_results = requests.get(url)
                soup = bs4.BeautifulSoup(request_results.text, "html.parser")
                result = soup.find("div", class_="BNeawe").text
                response = result
            except Exception as e:
                response = e
        elif 'introduce' in user_input:
            display_smiley_closed()
            response = get_response('selfintro')
        elif 'meet' in user_input:
            display_smiley_closed()
            hello = user_input.replace('meet', '')
            response = f"Hello {hello}, I am Rebecca!"
        elif 'you suck' in user_input or 'you are so annoying' in user_input or 'fuck' in user_input or 'bitch' in user_input or 'you are ugly' in user_input or 'you are stupid' in user_input or 'no one likes you' in user_input or 'you are waste' in user_input or 'i hate you' in user_input.lower():
            display_dead_face()
            response = get_response('rant')
        elif 'i like you' in user_input or 'i love you' in user_input or 'i want to marry you' in user_input or 'will you be my girlfriend' in user_input or 'can we be together' in user_input or 'i want to be your boyfriend' in user_input:
            display_smiley_closed()
            response = get_response('flirt')
        else:
            display_smiley_closed()
            response = "I'm sorry, I didn't understand that."

        print("AI Voice Assistant:", response)
        text_to_speech(response)

        if 'exit' in user_input:
            break

    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--reverse-order', type=bool, default=False, help='Set to true if blocks are in reverse order')
    main()
