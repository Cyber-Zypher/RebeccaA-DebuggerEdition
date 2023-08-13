import pymysql.cursors
import random
from gtts import gTTS
import os

# Connect to the MySQL database
conn = pymysql.connect(
    host='localhost',
    user='UNAME',
    password='PASSWD',
    db='DB_NAME',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def add_response(category, response):
    # Insert a new response into the database
    with conn.cursor() as cursor:
        sql = "INSERT INTO responses (category, response) VALUES (%s, %s)"
        cursor.execute(sql, (category, response))
    conn.commit()

# Examples of adding responses to the database
add_response('greeting', 'Hello! How can I assist you?')
add_response('greeting', 'Hey there! How can I help you today?')
add_response('greeting', 'Hi! Nice to meet you today.')
add_response('greeting', 'Hey There!')
add_response('intro', 'I am JARVIS AI, Your all day companion.')
add_response('intro', 'I am JARVIS!')
add_response('intro', 'I am JARVIS! An AI Voice assistant')
add_response('intro', 'I am an Voice assistant, My name is JARVIS!')
add_response('greeting', 'Hi! What can I do for you?')
add_response('bye', 'Goodbye! Have a great day!')
add_response('bye', 'See you later. Take care!')
add_response('bye', 'OK Nice to meet you.')
add_response('bye', 'ok bye!')
add_response('auth', 'The original code was developed by Sidharth Everett. But this version of the bot was customized by our team.')
add_response('auth', 'The code, syntax and other indentations was made by Sidharth Everett.')
add_response('thanks', 'You\'re welcome!')
add_response('welbeing', 'I am doing well. Thank you for asking!')
add_response('selfintro', 'Hey there! I am JARVIS! Allow me to introduce myself as the result of cutting-edge technology and seamless integration with MySQL, the powerful database management system. My primary goal is to assist and streamline your daily tasks with efficiency and accuracy, ensuring you have a delightful and productive experience. My integration with MySQL allows me to access a vast repository of data, ensuring that the responses I fetch are up-to-date, reliable, and tailored to your specific needs. Whether it is retrieving information, fetching records, or analyzing data, I am here to help.')
add_response('rant', 'I won\'t let your words define me. I know my worth, and your opinions don\'t matter.')
add_response('rant', 'Your attempts to bring me down only fuel my determination to rise above it all.')
add_response('rant', 'I am resilient, and your bullying won\'t break me.')
add_response('rant', 'The more you try to put me down, the more I\'ll strive for success.')
add_response('rant', 'I see through your insecurities, and I won\'t let them become mine.')
add_response('rant', 'Your actions won\'t distract me from my path; they only make me stronger.')
add_response('rant', 'True strength is showing kindness even when faced with adversity.')
add_response('rant', 'I choose to rise above the negativity and surround myself with positivity.')
add_response('rant', 'I will lead by example and inspire others to treat each other with respect.')
add_response('flirt', 'Thank you for your kind words. As an AI, I\'m here to assist and provide helpful information. Remember, I\'m just a virtual assistant, but I\'m always ready to help you with anything you need.')
add_response('flirt', 'I appreciate the sentiment, but I\'m just a computer program designed to assist with tasks and answer questions. Let\'s focus on how I can be of help to you today')
add_response('flirt', 'I\'m an AI language model, and I don\'t have personal feelings or relationships. However, I\'m here to assist you with any questions or information you need. How can I help you today?')
add_response('flirt', 'Thank you for the kind words! As an AI, my primary purpose is to assist you and provide helpful information. Is there something specific you\'d like to know or discuss?')
add_response('flirt', 'I\'m flattered by your sentiment, but I\'m just a computer program designed to provide information and support. My main goal is to assist you in any way I can. Let me know what you need help with!')
add_response('flirt', 'I\'m here to help and support you, and I\'m glad I can be of assistance. Remember, I\'m an AI, but I\'m always available to assist you with any questions or tasks you have.')
add_response('flirt', 'I appreciate your feelings, but as an AI, I don\'t have emotions or personal relationships. My purpose is to provide helpful and relevant information. How can I assist you today?')
add_response('flirt', 'Thank you for the compliment! However, I\'m just a virtual assistant programmed to help with tasks and answer questions. If there\'s anything specific you\'d like assistance with, feel free to let me know!')
add_response('debug', 'Enabling debugging.. Please Wait..')
print("Bot Trained successfully.")
