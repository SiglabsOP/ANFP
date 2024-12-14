import subprocess
import os
import time
import logging

# Configure logging
logging.basicConfig(filename='siterrors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# List of script paths            // change the paths as needed      // change the paths as needed   
scripts = [
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdepthneuronewz.py',
    #r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdepth three .py',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdepthfour.py',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdeptheight.py',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\adrotation.py',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdepthsky.py',
    #enbalelaterr'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdepthfive.py',    
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdepthsix.py',    
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdepthnature.py',       
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdepthseven.py',   
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\parseanalyzerdepth two.py'
]

# Run each script in sequence
for script in scripts:
    try:
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running script {script}: {e}")

# Wait for the files to be created  // change the paths as needed    
file_paths = [
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\reportdepth2.txt',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\neurosciencenews_autism_news.txt',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\sky_news_autism.txt',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\ads.txt',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\articlesnature.txt',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\autism_news.txt',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\eight.txt',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\positive_news.txt',
    r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\sciencedaily_autism_news.txt',
    #renable r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\autism_news2.txt',
   # r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\reportdepth_cna.txt'
]

# Function to check if files exist
def check_files_exist():
    return all(os.path.exists(file_path) for file_path in file_paths)

# Wait until all files are created
while not check_files_exist():
    time.sleep(5)  # Adjust the sleep duration as needed

# Combine files into a single file
output_file_path = r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\combined_report.txt'
with open(output_file_path, 'w', encoding='utf-8') as combined_file:
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            combined_file.write(input_file.read())

# Delete source files
for file_path in file_paths:
    os.remove(file_path)

print(f"Combined report created at {output_file_path}")

# Wait until the combined report is fully created
while not os.path.exists(output_file_path):
    time.sleep(5)  # Adjust the sleep duration as needed

# Run the formatter.py script // change the paths as needed 
formatter_script_path = r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\formatter.py'
try:
    subprocess.run(['python', formatter_script_path], check=True)
except subprocess.CalledProcessError as e:
    logging.error(f"Error running formatter script: {e}")
else:
    print("Formatter script executed successfully.")

# Run the dupecheck.py script
dupecheck_script_path = r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\dupecheck.py'
try:
    subprocess.run(['python', dupecheck_script_path], check=True)
except subprocess.CalledProcessError as e:
    logging.error(f"Error running dupecheck script: {e}")
else:
    print("Dupecheck script executed successfully.")
