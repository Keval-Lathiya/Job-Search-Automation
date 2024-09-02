# Job-Search-Automation

## Automate Your Job Search: Let Python Handle It!

#### This Python script scrapes job listings from job boards (well well well xD) and notifies you via WhatsApp if your desired job is posted within a specified time frame. I prefer to receive notifications every morning at 9 AM, so I’ve scheduled this script using Windows Task Scheduler to run automatically every day at that time and send me the results.

### How to Schedule the Script in Task Scheduler:

1. Open Task Scheduler.
2. Select "Create Basic Task" from the "Actions" menu.
3. Name your task and provide a description, then click "Next."
4. Set the frequency of the task, then click "Next" and specify the time.
5. Choose "Start a program" and click "Next."
6. Browse to the location of your Python executable:
   - If you're unsure where it's located, press `Win + R`, type `cmd`, then type `where python` in the command prompt.
7. In the "Add arguments" field, enter the path to your script (e.g., `"C:\Users\keval\OneDrive\Desktop\Python\Job_Automation.py"`).
8. Click "Finish" to complete the setup.

### Setting up Twilio for WhatsApp notifications is straightforward. Visit [twilio.com](https://www.twilio.com) to get a WhatsApp number, `account_sid`, and `auth_token`.

### Please let me know your feedback. Best of luck !!!

