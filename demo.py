import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

excel_file_path = 'keywords.xlsx'

df = pd.read_excel(excel_file_path)

driver = webdriver.Chrome()

driver.maximize_window()


for keyword in df['Keywords']:

    driver.get("https://www.google.com/")


    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)

    suggestions = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul[role="listbox"] li span'))
    )

    suggestions_text = [suggestion.text for suggestion in suggestions if suggestion.text.strip()]

    if suggestions_text:
        # Find the longest and shortest suggestions
        longest_suggestion = max(suggestions_text, key=len)
        shortest_suggestion = min(suggestions_text, key=len)

        print("Longest suggestion:", longest_suggestion)
        print("Shortest suggestion:", shortest_suggestion)
    else:
        print("No suggestions found or all suggestions were empty.")

    search_box.send_keys(Keys.RETURN)

    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "search"))
    # )

    time.sleep(3)

driver.quit()

print("Search completed for all keywords.")










# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time


# driver = webdriver.Chrome()

# driver.maximize_window()
# driver.get("https://www.google.com/")

# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("javatpoint")


# time.sleep(2)  # Allow time for the suggestions to load
#

# suggestions = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul[role="listbox"] li span'))
# )

# suggestions_text = [suggestion.text for suggestion in suggestions if suggestion.text.strip()]

# if suggestions_text:
#     # Find the longest and shortest suggestions
#     longest_suggestion = max(suggestions_text, key=len)
#     shortest_suggestion = min(suggestions_text, key=len)
#
#     print("Longest suggestion:", longest_suggestion)
#     print("Shortest suggestion:", shortest_suggestion)
# else:
#     print("No suggestions found or all suggestions were empty.")
#

# time.sleep(3)

# # Close the browser
# driver.quit()


# from selenium import webdriver
# import time

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# print("Here the sample test case will be started")
# driver = webdriver.Chrome()

# driver.maximize_window()

# driver.get("https://www.google.com/")

# driver.find_element(By.NAME, "q").send_keys("javatpoint")
# time.sleep(3)   # here, the system will remain in sleep for 3sec

# driver.find_element(By.NAME,"btnK").send_keys(Keys.ENTER)
# time.sleep(3)   # here, the system will remain in sleep for 3sec

# driver.close()
# print("sample test case successfully completed")