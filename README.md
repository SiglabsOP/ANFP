# ANFP - Automated News Fetcher and Processor
ANFP 
v 31.074

 

ANFP is a fully automated tool designed to fetch, process, and share news content from multiple sources. It simplifies the workflow of aggregating, sorting, and distributing news by eliminating duplicates and ensuring streamlined updates.
ANFP is very adaptable, in this case we provide the source code of Autie, the Autism X Campaign. 

## Key Features

1. **Automated News Fetching**:
   - Integrates with multiple APIs to fetch news articles from various sources.
   - Supports dynamic updates to ensure you receive the latest content.

2. **Content Processing**:
   - Logs changes in fetched content using an SQLite database.
   - Provides a fallback mechanism to record changes in a local text file (`FALLBACK.txt`).
   - Detects and eliminates duplicate entries.

3. **Sorting and Organization**:
   - Efficiently sorts news articles based on custom parameters.
   - Prepares content for easy sharing and archiving.

4. **Social Media Integration**:
   - Automatically tweets curated content.
   - Avoids duplication in shared posts.

5. **Customizable and Modular**:
   - Modular design allows for easy updates and integration of additional features.
   - Includes executable versions for quick deployment.

Autie was used to maintain and run a longterm autism awareness campaign on X. 
Autie has the ability to access the X API. All you need to do is obtain an API key from X and set your key.
In case you need to update the parsers, it can easily be done with the aid of AI.
 

### Starting the Program
1 Run updater.py to start the updater it will stay in the background and keep the system up to date

2 Run the launcher to start all necessary components:
```bash
python launch.py
```
 
### Configuration
- check `BINGLIST.txt` with the combined list of parsed news sources or queries.
- Modify the settings in `Autie.py` to suit your requirements for logging and deduplication.

### Logs and History
- Changes are logged in an SQLite database (`changes.db`).
- A fallback log (`FALLBACK.txt`) is maintained for redundancy.

## File Structure

- `Autie.py`: Core logic for tracking changes and processing content.
- `APIaccess.py`: Handles API integrations for fetching news.
- `cleaner.py`: Removes duplicate or outdated entries. This is an extension module and though required for Autie to run, has been disabled.
- `Sort.py`: Organizes and sorts news articles.
- `launch.py`: Entry point to start the program and its components.
- `history.txt`: Tracks previously fetched and processed data.
- `parser/`: Contains additional utilities for parsing and processing content.

 .

## Acknowledgments

Thank you to the X community for making this happen!



If you enjoy this program, buy me a coffee https://buymeacoffee.com/siglabo
You can use it free of charge or build upon my code. 
 
(c) Peter De Ceuster 2024
Software Distribution Notice: https://peterdeceuster.uk/doc/code-terms 
This software is released under the FPA General Code License.
