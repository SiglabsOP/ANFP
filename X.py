import tweepy
import logging
import os
import sys

# Delete the twitter.log file if it exists
if os.path.exists('twitter.log'):
    os.remove('twitter.log')

# Set up logging without timestamp and log level for regular messages
logging.basicConfig(filename='twitter.log', level=logging.INFO, format='%(message)s')

# Set up logging for errors
error_log = logging.FileHandler('ERRORS.log')
error_log.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_log.setFormatter(error_formatter)

# Add the error log handler to the root logger
logging.getLogger().addHandler(error_log)

# Twitter API credentials
consumer_key = " "
consumer_secret = " "
access_token = "   "
access_token_secret = " "

# Set up Tweepy authentication
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

def tweet_headlines(headlines):
    global valid_tweets_count  # Use global variable for counting valid tweets
    for headline, url in headlines:
        try:
            # Check if similar content has been tweeted before
            if is_similar_content_present(headline):
                print("Similar content has been tweeted before. Skipping this headline.")
                # Write the skipped headline to cancelled.txt
                with open("cancelled.txt", "a") as cancelled_file:
                    cancelled_file.write(f"{headline}\n")
                continue

            # Create a message without actually posting it
            message = f"{headline} {url}"

            # Log the message to the file
            logging.info(f"{message}")

            # Print the message
            print(f"Message: {message}")

            # Write an entry to HISTORY.txt
            with open("HISTORY.txt", "a") as history_file:
                history_file.write(f"{headline}\n")

            # Write a simple tweet
            tweet = client.create_tweet(text=message)

            # Get the tweet id from the JSON object
            tweet_id = tweet.id

            # Print the tweet id
            print(f"Tweeted {tweet_id}")

            # Increment the count of valid tweets
            valid_tweets_count += 1

            # Terminate the script after one valid tweet
            sys.exit()

        except Exception as e:
            # Log the error to the separate error log file
            logging.error(f"Error preparing tweet {headline}: {str(e)}")
            # Continue to the next headline if an error occurs

# Function to check if similar content has been tweeted before
def is_similar_content_present(new_headline):
    with open("HISTORY.txt", "r") as history_file:
        for line in history_file:
            if new_headline in line:
                return True
    return False

def get_first_valid_headline(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            headline = line.strip().split("\t")
            if len(headline) != 2:
                # Log the line to EMPTYBING.txt
                with open("EMPTYBING.txt", "a") as empty_bing_file:
                    empty_bing_file.write(f"Invalid format in line: {line.strip()}\n")
                continue
            if not is_similar_content_present(headline[0]):
                return headline
    return None


# Read headlines from the file
file_name = "BINGLIST.txt"

# Get the first valid headline from the file
first_valid_headline = get_first_valid_headline(file_name)

# Initialize a counter for valid tweets
valid_tweets_count = 0

# Tweet the first valid headline
if first_valid_headline:
    tweet_headlines([first_valid_headline])
else:
    print("No valid headlines found in the file.")