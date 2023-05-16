# Restore Scheduled Jobs From Backup

If you're looking to restore scheduled jobs from backup files, this can be accomplished through this script. Services like OwnBackup store the data, but cannot restore the jobs by scheduling.

## Required Files
- `apex_classes.csv`
- `async_apex_jobs.csv`
- `cron_job_details.csv`
- `cron_triggers.csv`

## Requirements
- Python 3.10+

## Setup

1. Clone the repo locally
2. Add `csv` files to the folder
3. Run `pipenv install`

## Run

```bash
pipenv shell
python main.py
```

The output will be in `output.txt` which will be in the correct format to schedule through the execute anonymous window in the developer console.