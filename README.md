```markdown
# Folder Synchronization Script

This Python script performs one-way synchronization of files from a source folder to a replica folder. It can be scheduled to run periodically to ensure that the replica stays updated with the latest changes in the source.

## Usage

### Prerequisites

- Python installed on your machine

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/miguelsoliveira005/Sync-folders.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Sync-folders
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Run the Script

Execute the script with the following command:

```bash
python Sync.py /path-to-source /path-to-replica /path-to-LogFile.txt
```

Replace `/path-to-source`, `/path-to-replica`, and `/path-to-LogFile.txt` with the actual paths.

### Schedule Periodic Execution

To schedule the script to run periodically, you can use cron jobs on Linux/Mac or Task Scheduler on Windows. For example, to run the script every minute:

#### Linux/Mac

```bash
* * * * * /path-to-python /path-to-your-Sync.py /path-to-source /path-to-replica /path-to-LogFile.txt
```

#### Windows

Use Task Scheduler to create a new task and set the trigger to run the script at your preferred interval.


Make sure to replace placeholders like `/path-to-source` with the actual paths. Adjust the content as needed for your specific project details.
