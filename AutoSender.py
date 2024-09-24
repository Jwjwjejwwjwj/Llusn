from telethon import TelegramClient
import time

# ANSI escape codes for colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"

# ASCII Art Logo
def print_logo():
    logo = r"""
       
  _____    _____    _____   _____   _______   _____    ____  
 |  __ \  |_   _|  / ____| |_   _| |__   __| |_   _|  / __ \ 
 | |  | |   | |   | |  __    | |      | |      | |   | |  | |
 | |  | |   | |   | | |_ |   | |      | |      | |   | |  | |
 | |__| |  _| |_  | |__| |  _| |_     | |     _| |_  | |__| |
 |_____/  |_____|  \_____| |_____|    |_|    |_____|  \____/ 
                                                             
                                                             

    """
    print(logo, flush=True)  # Ensure the output is immediately flushed

# Call the print_logo function as early as possible to ensure it displays
print_logo()

# Prompt user for API ID, API Hash, and Phone number
api_id = input("Enter your API ID: ")
api_hash = input("Enter your API Hash: ")
phone_number = input("Enter your Phone Number (with country code): ")

# List of group chat IDs (replace with actual group IDs or usernames)
group_chat_ids = input("Enter group usernames or IDs separated by commas: ").split(",")

# Create a new Telegram client instance
client = TelegramClient('session_name', api_id, api_hash)

# Function to send messages to each group
async def send_messages(message):
    for group_id in group_chat_ids:
        await client.send_message(group_id.strip(), message)

# Main function to manage message sending
async def main():
    # Start the client and log in
    await client.start(phone_number)

    # Prompt user for message content, duration, and interval
    message = input("Enter the message you want to send: ")
    duration = int(input("Enter the total duration in seconds: "))
    interval = int(input("Enter the interval between messages in seconds: "))

    # Keep sending messages until the duration is over
    start_time = time.time()
    
    while time.time() - start_time < duration:
        await send_messages(message)
        # Print message with color formatting
        print(f"Message sent to {', '.join(group_chat_ids)} {RED}SCRIPT BY{RESET} {GREEN}@DIGITIO{RESET}.")
        time.sleep(interval)  # Wait for the next interval

# Run the client and start sending messages
with client:
    client.loop.run_until_complete(main())
