# Stockprice Reminder
Note: Get your free API Key here https://www.alphavantage.co/support/#api-key

## Automation Setup:
1. `sudo su` to switch to root user
2. `crontab -e`
3. Add line for the job, i.e.: `1 0-23 * * 1-5 python /path/to/script/stockprice-reminder.py`
4. Save