#!/usr/bin/env python
# coding: utf-8

# # Job Notifications Automation
# 
# ## Automate Your Job Search: Let Python Handle It!
# 
# #### This Python script scrapes job listings from job boards and notifies you via WhatsApp if your desired job is posted within a specified time frame. I prefer to receive notifications every morning at 9 AM, so I’ve scheduled this script using Windows Task Scheduler to run automatically every day at that time and send me the results.
# 
# ### How to Schedule the Script in Task Scheduler:
# 
# 1. Open Task Scheduler.
# 2. Select "Create Basic Task" from the "Actions" menu.
# 3. Name your task and provide a description, then click "Next."
# 4. Set the frequency of the task, then click "Next" and specify the time.
# 5. Choose "Start a program" and click "Next."
# 6. Browse to the location of your Python executable:
#    - If you're unsure where it's located, press `Win + R`, type `cmd`, then type `where python` in the command prompt.
# 7. In the "Add arguments" field, enter the path to your script (e.g., `"C:\Users\keval\OneDrive\Desktop\Python\Job_Automation.py"`).
# 8. Click "Finish" to complete the setup.
# 
# ### Setting up Twilio for WhatsApp notifications is straightforward. Visit [twilio.com](https://www.twilio.com) to get a WhatsApp number, `account_sid`, and `auth_token`
# 
# 

# In[1]:


from jobspy import scrape_jobs
from twilio.rest import Client

def generate_result(search_term="Data Analyst at Meta"):
    jobs = scrape_jobs(
        site_name=["LinkedIn"], # or Indeed, zip_recruiter, glassdoor. You can put all of them as well
        search_term=search_term,
        hours_old=24
        #location="Remote",
        #num_jobs=20,
        #linkedin_fetch_description=True,
        #include_salary=True,
        #experience_level="Mid Level",
        #job_type="Full-time",
        #remote=True
    )
    
    jobs = jobs[jobs['company'] == 'Meta'] # Adding additional filter just in case other promoted jobs are fetched too
    # add more filters as well like specific words in job description (i.e security clearance ), minimum salary, company industry etc
    
    if not jobs.empty:
        message = f"Here are the latest {search_term} jobs :\n\n"
        for index, job in jobs.iterrows():
            message += f"{job['title']}\nLink: {job['job_url']}\n\n"
    else:
        message = "No new jobs found."
    return message


# In[2]:


from jobspy import scrape_jobs
from twilio.rest import Client

def generate_result(search_term="Data Analyst at Meta"):
    jobs = scrape_jobs(
        site_name=["LinkedIn"], # or Indeed, zip_recruiter, glassdoor. You can put all of them as well
        search_term=search_term,
        hours_old=240
        #location="Remote",
        #num_jobs=20,
        #linkedin_fetch_description=True,
        #include_salary=True,
        #experience_level="Mid Level",
        #job_type="Full-time",
        #remote=True
    )
    
    jobs = jobs[jobs['company'] == 'Meta'] # Adding additional filter just in case other promoted jobs are fetched too
    # add more filters as well like specific words in job description (i.e security clearance ), minimum salary, company industry etc
    
    if not jobs.empty:
        message = f"Here are the latest {search_term} jobs :\n\n"
        for index, job in jobs.iterrows():
            message += f"{job['title']}\nLink: {job['job_url']}\n\n"
    else:
        message = "No new jobs found."
    return message


# In[3]:


# I have used Twilio to send messages to my whatsapp. It also provides services to send messages in SMS. It's very inexpensive but 
# if you prefer something free and in email, smtplib is an excellent library to use. Just make sure you're using app password if you have 2FA

def send_whatsapp_message(result):
    # Your Twilio account SID and Auth Token
    account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Replace with your Twilio Account SID
    auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'    # Replace with your Twilio Auth Token
    client = Client(account_sid, auth_token)

    # Sending the message
    message = client.messages.create(
        body=result,  
        from_='whatsapp:+1xxxxxxxxxx',  # Your Twilio number 
        to='whatsapp:+1xxxxxxxxxx'    # Your WhatsApp number 
    )

    print(f"Message sent with SID: {message.sid}")


# In[ ]:


def main():
    # Generate the result
    result = generate_result()

    # Send the result via WhatsApp
    send_whatsapp_message(result)


# In[ ]:


if __name__ == "__main__":
    main()

