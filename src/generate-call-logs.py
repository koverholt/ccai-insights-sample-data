import argparse
import json
import random

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "num_call_logs",
    nargs="?",
    default=10,
    type=int,
    help="Number of call log files to generate",
)
args = parser.parse_args()
config = vars(args)

NUM_CALL_LOG_FILES = config["num_call_logs"]

greetings = [
    "Hello, how can I assist you today?",
    "Hi there, what can I help you with today?",
    "Greetings, how can I help you?",
    "Hi, welcome to support, how can I help you today?",
    "Hello, what can I assist you with?",
]

devices = [
    "television",
    "laptop",
    "router",
    "mobile phone",
    "camera",
]

problems = [
    "It doesn't seem to turn on",
    "The device is not connecting to the internet",
    "I cannot download any apps",
    "I have not been able to connect to my account",
    "The battery only lasts 30 minutes",
]

problem_detail = [
    "It says that there is an error with the latest update",
    "It's been happening for the last 4 days",
    "The device isn't responding when I try to factory reset it",
    "I tried using the troubleshooting wizard, but it didn't help",
    "The problem is still happening since I last called in",
]

statuses = [
    "Error: Failed update",
    "All systems normal",
    "Warning: No available storage",
    "Error: Account is inactive",
    "Warning: No connection to the internet",
]

solutions = [
    "Have you tried turning it off and on again?",
    "Can you update to the latest firmware version?",
    "Have you tried to log out and log in again?",
    "Can you try to remove and reset the battery?",
    "Have you tried to factory reset the device?",
]

check_solved = [
    "Sure, does that cover everything for today?",
    "No problem, is there anything else that I can help with?",
    "Sure thing, did that solve the issue for you?",
    "Sounds good, are there any other issues that I can help with?",
    "Great, did that fix the problem?",
]

problem_solved = [
    "Yes, my problem is solved now",
    "No, I'm still having the same problem",
    "Yes, everything is working fine now",
    "Yes, it seems to be working now",
    "No, I'm having a different problem now",
]


def generate_log():
    call_log = {
        "entries": [
            {"text": random.choice(greetings), "role": "AGENT", "user_id": 2},
            {
                "text": "Hi, I'm having an issue with my " + random.choice(devices),
                "role": "CUSTOMER",
                "user_id": 1,
            },
            {
                "text": "Sorry to hear. Can you tell me what the problem is?",
                "role": "AGENT",
                "user_id": 2,
            },
            {"text": random.choice(problems), "role": "CUSTOMER", "user_id": 1},
            {
                "text": "Can you give me more details about the problem?",
                "role": "AGENT",
                "user_id": 2,
            },
            {"text": random.choice(problem_detail), "role": "CUSTOMER", "user_id": 1},
            {
                "text": "And what is the status shown in the application settings?",
                "role": "AGENT",
                "user_id": 2,
            },
            {"text": random.choice(statuses), "role": "CUSTOMER", "user_id": 1},
            {
                "text": "Can you tell me your account number?",
                "role": "AGENT",
                "user_id": 2,
            },
            {
                "text": "Sure, it's " + str(random.randint(100000000, 999999999)),
                "role": "CUSTOMER",
                "user_id": 1,
            },
            {"text": random.choice(solutions), "role": "AGENT", "user_id": 2},
            {
                "text": "I see, thanks for the information, I will give that a try.",
                "role": "CUSTOMER",
                "user_id": 1,
            },
            {"text": random.choice(check_solved), "role": "AGENT", "user_id": 2},
            {"text": random.choice(problem_solved), "role": "CUSTOMER", "user_id": 1},
        ]
    }

    json_object = json.dumps(call_log, indent=4)
    return json_object


for i in range(NUM_CALL_LOG_FILES):
    filename = "output/chat_" + str(i) + ".json"
    with open(filename, "w") as outfile:
        output = generate_log()
        outfile.write(output)
