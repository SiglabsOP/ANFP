import pandas as pd
import schedule
import time
import datetime

# Full path to the CSV file   you can change this path
csv_file_path = r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\quotes.csv'
def print_ascii_art(max_width=80):
    # Custom ASCII art
    ascii_art = r"""
      __              __       ___      ___           __       ____  ____  ___________  __     _______  
     |" \            /""\     |"  \    /"  |         /""\     ("  _||_ " |("     _   ")|" \   /"     "| 
     ||  |          /    \     \   \  //   |        /    \    |   (  ) : | )__/  \\__/ ||  | (: ______) 
     |:  |         /' /\  \    /\\  \/.    |       /' /\  \   (:  |  | . )    \\_ /    |:  |  \/    |   
     |.  |        //  __'  \  |: \.        |      //  __'  \   \\ \__/ //     |.  |    |.  |  // ___)_  
    /\  |\      /   /  \\  \ |.  \    /:  |     /   /  \\  \  /\\ __ //\     \:  |    /\  |\(:      "| 
   (__\_|_)    (___/    \___)|___|\__/|___|    (___/    \___)(__________)     \__|   (__\_|_)\_______) 
                                                                                                    
       ⣠⣴⣾⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⠀⢀⣿⣿⣿⣿⡿⠛⢿⡿⠛⢻⣿⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⢸⣷⣶⣾⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠈⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀
⠀⢀⣤⣀⣾⣿⣿⣿⠟⠛⠛⠛⠛⠻⣿⣿⣿⣷⣀⣤⡀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⡟⢿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡿⢻⣿⡇⠀
⠀⢸⣿⡇⠈⠙⠛⢛⣿⣿⣤⣤⣿⣿⡛⠛⠋⠁⢸⣿⡇⠀
⣤⣼⣿⣧⣤⡀⠀⠙⠛⠛⠛⠛⠛⠛⠋⠀⢀⣤⣼⣿⣧⣤
⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛


 (c) 2024 SIG Labs       Artificial and Intelligent! v 31.074
    """

    # Split the ASCII art into lines
    lines = ascii_art.splitlines()

    # Print each line with a maximum width
    for line in lines:
        print(line[:max_width])
        # Call the function with a specified maximum width (adjust as needed)
print_ascii_art(max_width=500)
def read_and_display_csv(chunksize=1):
    # Use 'iterator=True' to read the file in chunks
    csv_reader = pd.read_csv(csv_file_path, usecols=['quote', 'author'], chunksize=chunksize, iterator=True)

    # Define a file to store the current chunk number
    current_chunk_file = 'current_chunk.txt'

    # Read the current chunk number or default to 1
    try:
        with open(current_chunk_file, 'r') as f:
            current_chunk = int(f.read())
    except FileNotFoundError:
        current_chunk = 1

    # Display the current chunk
    print(f"Serving your hourly Quote {current_chunk}:")

    # Save the updated current chunk number
    with open(current_chunk_file, 'w') as f:
        f.write(str(current_chunk + 1))

    for i in range(current_chunk - 1):
        try:
            next(csv_reader)
        except StopIteration:
            print("No more quotes left.")
            return

    try:
        chunk = next(csv_reader)
        for index, row in chunk.iterrows():
            print(f"Quote: {row['quote']}")
            print(f"Author: {row['author']}")
            print("------------------------------")
    except StopIteration:
        print("No more quotes left.")


def job():
    read_and_display_csv()


if __name__ == "__main__":
    # Print introduction message
    print("I am Autie")
    print(f"Today is {datetime.date.today()}")
    print(f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}")
    print("I am imperfect, there are bugs but my creator sometimes lovingly looks away")
    print("\nI am friends with Bing")
    print("Bing thinks he's the clever one but my creator tends to disagree\n")
    print("My latest patch: improved encoding,logging, i now read greek letters")
    # Print quotation database information
    quotes_df = pd.read_csv(csv_file_path)
    total_quotes = len(quotes_df)
    print(f"My quotation database currently has half a million entries.")
    print(f"There are {total_quotes} quotes.\n")

    # Display the first quote immediately upon startup
    job()

    # Schedule the job to run every one hour after the first run
    schedule.every().hour.do(job)

    while True:
        # Run the scheduled jobs
        schedule.run_pending()

        # Wait for a short time
        time.sleep(1)
