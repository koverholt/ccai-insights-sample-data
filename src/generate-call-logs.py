import argparse
import datetime
import json
import random

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "num_call_logs",
    nargs="?",
    default=30000,
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
    "It doesn't seem to turn on. The device does not respond to any buttons or commands. The power light does not turn on.",
    "The device is not connecting to the internet. The device cannot connect to a Wi-Fi network. The device cannot connect to the internet when plugged into a wired network.",
    "I cannot download any apps. I am only able to access the messaging app. I am not able to access other apps.",
    "I have not been able to connect to my account. I cannot log into my account. I cannot access my account. I do not know what to do to fix my account.",
    "The battery only lasts 30 minutes. The battery drains quickly after being fully charged. The battery does not last as long as it used to.",
]

problem_detail = [
    "It says that there is an error with the latest update. The device is stuck on the previous update. The update is not working properly.",
    "It's been happening for the last 4 days, when I dropped the device. It's possible that the fall caused some damage to the device.",
    "The device isn't responding when I try to factory reset it. I changed the power settings a few days ago, and it hasn't been working correctly since then.",
    "I tried using the troubleshooting wizard, but it didn't help. There was a warning to check that the device has enough storage space and if it's compatible with the software I'm trying to use.",
    "The problem is still happening since I last called in. I tried restarting it 3 times and the issue is still happening. It's reporting a memory error about once an hour.",
]

statuses = [
    "Error: Failed update. The update is not available for your current major version. Please check for updates again later.",
    "All systems normal. Your device is connected to the internet and functioning normally. There are no issues to report.",
    "Warning: No available storage. Your computer's hard drive is full. Please delete some files and try again. You can also try to free up some space by moving some files to an external storage device.",
    "Error: Your account is not authorized to access this resource. Please contact the administrator for assistance.",
    "Warning: No connection to the internet. Your internet connection is blocked by a firewall. Please contact the administrator to unblock it.",
]

solutions = [
    "Have you tried turning it off and on again? The device should be connected to the internet in order to contact our servers. If it is not, check your internet connection and make sure that your device is connected to the router.",
    "Can you update to the latest firmware version? You can check if your router's firmware is up to date by going to the router's settings and looking for a firmware update option. If there is an update available, install it.",
    "Check if your device is able to access streaming content. You can check if your device is able to access streaming content by trying to watch a show or movie on a streaming service. If you are unable to watch anything, check your internet connection and make sure that your device is connected to the correct network.",
    "Check if your devices are receiving a signal.? You can check if your devices are receiving a signal by using a signal strength meter. If the signal strength is low, you may need to move your devices closer to the router.",
    "Have you tried to factory reset the device? You can check if your router's settings are correct by going to the router's settings and looking for a default settings option. If there is a default settings option, reset your router to the default settings.",
]

check_solved = [
    "Sure, does that cover everything for today?",
    "No problem, is there anything else that I can help with?",
    "Sure thing, did that solve the issue for you?",
    "Sounds good, are there any other issues that I can help with?",
    "Great, did that fix the problem?",
]

problem_solved = [
    "Yes, my problem is solved now. I have checked the settings and made sure that everything is set up correctly.",
    "No, I'm still having the same problem. I have tried contacting the manufacturer of the device for help.",
    "Yes, everything is working fine now. I have tried using a different connection to see if the problem is with the router or with the internet service provider.",
    "Yes, it seems to be working now. I have checked the connections and made sure that everything is plugged in properly.",
    "No, I'm having a different problem now. I have tried using a different website or app to see if the problem is with the website or app itself.",
]


def generate_log():
    # Generate timestamps within the last 30 days in microseconds of epoch time
    dt = datetime.datetime.today() - random.random() * datetime.timedelta(days=30)
    timestamp = int(round(dt.timestamp()) * 1e6)
    response_delay = int(random.randint(10, 30) * 1e6)

    # Generate JSON object of conversation
    call_log = {
        "entries": [
            {
                "start_timestamp_usec": timestamp + response_delay * 0,
                "text": random.choice(greetings),
                "role": "AGENT",
                "user_id": 2,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 1,
                "text": "Hi, I'm having an issue with my " + random.choice(devices),
                "role": "CUSTOMER",
                "user_id": 1,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 2,
                "text": "Sorry to hear. Can you tell me what the problem is?",
                "role": "AGENT",
                "user_id": 2,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 3,
                "text": random.choice(problems),
                "role": "CUSTOMER",
                "user_id": 1,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 4,
                "text": "Can you give me more details about the problem?",
                "role": "AGENT",
                "user_id": 2,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 5,
                "text": random.choice(problem_detail),
                "role": "CUSTOMER",
                "user_id": 1,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 6,
                "text": "And what is the status shown in the application settings?",
                "role": "AGENT",
                "user_id": 2,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 7,
                "text": random.choice(statuses),
                "role": "CUSTOMER",
                "user_id": 1,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 8,
                "text": "Can you tell me your account number?",
                "role": "AGENT",
                "user_id": 2,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 9,
                "text": "Sure, it's " + str(random.randint(100000000, 999999999)),
                "role": "CUSTOMER",
                "user_id": 1,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 10,
                "text": random.choice(solutions),
                "role": "AGENT",
                "user_id": 2,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 11,
                "text": "I see, thanks for the information, I will give that a try.",
                "role": "CUSTOMER",
                "user_id": 1,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 12,
                "text": random.choice(check_solved),
                "role": "AGENT",
                "user_id": 2,
            },
            {
                "start_timestamp_usec": timestamp + response_delay * 13,
                "text": random.choice(problem_solved),
                "role": "CUSTOMER",
                "user_id": 1,
            },
        ]
    }

    json_object = json.dumps(call_log, indent=4)
    return json_object


for i in range(NUM_CALL_LOG_FILES):
    filename = "output/chat_" + str(i) + ".json"
    with open(filename, "w") as outfile:
        output = generate_log()
        outfile.write(output)
