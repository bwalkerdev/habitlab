import datetime
import random
import creds
import openai
import os

openai.api_key = creds.open_ai_api_key

offline_morning_greet = [
    "Rise and whine, sunshine!",
    "Good morning, or whatever...",
    "Ugh, mornings. Can't live with 'em, can't live without 'em.",
    "Welcome back to the land of the living... barely.",
    "Just a friendly reminder: you can't hit snooze on life.",
    "Wakey wakey, eggs and... meh, who cares.",
    "You're awake? How unfortunate.",
    "Morning already? Time flies when you're unconscious.",
    "Up and at 'em, early bird. The worm won't catch itself.",
    "Another morning, another opportunity to press snooze.",
]

offline_afternoon_greet = [
    "Hey there, afternoon delight (or not).",
    "Afternoon, time to pretend you're being productive.",
    "Oh, look! The day's half gone, just like your motivation.",
    "Halfway through the day, but who's counting?",
    "The afternoon: when the coffee wears off and reality sets in.",
    "Good afternoon? More like, 'Meh' afternoon.",
    "Sun's up, fun's down. Welcome to the afternoon.",
    "Yawn... is it nap time yet?",
    "If only afternoons came with a snooze button...",
    "Afternoon: the time when you realize your to-do list is still a mile long.",
]

offline_evening_greet = [
    "Evening already? Time to exchange work for pajamas.",
    "Night falls, and so does your energy level.",
    "Congrats, you survived another day. Barely.",
    "Evening: when the couch calls your name.",
    "The day's over, but is it ever really over?",
    "Good evening? More like, 'Good, it's evening'.",
    "You made it through the day... or did the day make it through you?",
    "Now entering: the part of the day you've been waiting for.",
    "Time to start counting down the hours till bedtime.",
    "Evening's here, just in time for some well-deserved procrastination.",
]


def generate_greeting():
    try:
        prompt = ""
        now = datetime.datetime.now()
        if now.hour < 12:
            prompt = "Generate a short and snarky morning greeting. Generate the greeting only."
        elif now.hour < 18:
            prompt = "Generate a short and snarky afternoon greeting. Generate the greeting only."
        else:
            prompt = "Generate a short and snarky evening greeting. Generate the greeting only."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )

        greeting = response.choices[0].message
        return greeting["content"].replace('"', "")
    except:
        random.seed()
        if now.hour < 12:
            return random.choice(offline_morning_greet)
        elif now.hour < 18:
            return random.choice(offline_afternoon_greet)
        else:
            return random.choice(offline_evening_greet)


def main():
    now = datetime.datetime.now()
    now = now.hour
    print(generate_greeting())


if __name__ == "__main__":
    main()

# input("Press the any key: ")
