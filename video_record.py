from asyncio import wait

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_record_video():
   with sync_playwright() as p:
       # Launch the browser
       browser = p.chromium.launch(headless=False)
       # Create a context with video recording enabled
       context = browser.new_context(record_video_dir="videos/")
       # Open a new page and perform actions
       page = context.new_page()
       page.goto("https://qaplayground.com/bank/login")
       page.wait_for_timeout(5000) 
       login_page = LoginPage(page)
       login_page.login("standard_user", "bank_sauce")
       page.wait_for_timeout(5000) 

       # Close the context to save the video
       context.close()
       page.video.save_as("recording.webm")
       browser.close()