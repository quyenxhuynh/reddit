import praw
import webbrowser

def get_post():
    reddit = praw.Reddit(client_id='personal use script id',
                         client_secret='secret',
                         user_agent='app_name',
                         username='username',  # reddit username
                         password='password')  # reddit password

    for submission in reddit.subreddit('subreddit').new(limit=1): # can be changed to .top, .hot, etc.
        return submission.url

if __name__ == "__main__":
    most_recent = ""
    while True:
        temp = get_post()
        if temp != most_recent:
            most_recent = temp
            webbrowser.open_new_tab(most_recent)
