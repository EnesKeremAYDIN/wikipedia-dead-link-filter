# Wikipedia Dead Link Filter

This project scans pages in Wikipedia that contain dead external links, extracts the links, and optionally filters them based on specific keywords.

## Features

- Scans pages in Wikipedia that contain dead links.
- Saves found dead links to `links.txt` file.
- Optionally filters links based on a specific keyword and saves them to `filter.txt` file.
- Can process with page count limitation.
- Logs all operations to `bot.log` file.

## Requirements

The following dependencies need to be installed for this project:

- Python 3
- `requests` library
- `beautifulsoup4` library

To install dependencies:

```bash
pip install requests beautifulsoup4
```

## Installation and Usage

1. **Clone or download the repository:**

```bash
git clone https://github.com/EnesKeremAYDIN/wikipedia-dead-link-filter.git
cd wikipedia-dead-link-filter
```

2. **Run the script:**

```bash
python bot.py
```

### Usage Steps

1. When the script is run, it will ask if you want to filter:
   - `yes`: Filters based on a specific keyword.
   - `no`: Lists all dead links.

2. Enter how many pages to scan:
   - `0`: Performs unlimited page scanning.

### Outputs

- **`links.txt`**: All found links are stored in this file.
- **`filter.txt`**: Links filtered by keyword are stored here (only when filtering is enabled).
- **`bot.log`**: Log records of the process are kept in this file.

## Example Usage

```bash
python bot.py
Do you want to filter? (yes-no): yes
Enter the filter keyword: Atatürk
Enter the number of pages to scan (0 = unlimited): 0
```

This command filters dead links by the "Atatürk" keyword and scans unlimited pages.
