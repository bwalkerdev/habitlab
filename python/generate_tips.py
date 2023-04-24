import prompts
import creds
import openai
import sys

openai.api_key = creds.open_ai_api_key


def generate_tips(data):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompts.generate_tips_insights(data)}
            ],
        )

        greeting = response.choices[0].message
        return greeting["content"].replace('"', "")
    except:
        return "Unable to generate tips"


def main(arg):
    print(generate_tips(arg))


if __name__ == "__main__":
    main(sys.argv[1])

# input("Press the any key: ")
