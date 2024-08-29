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

longest_col = 'Longest Option'
shortest_col = 'Shortest Option'


for index, keyword in enumerate(df['Keywords']):
    driver.get("https://www.google.com/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)

    # get the suggestions
    suggestions = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul[role="listbox"] li span'))
    )

    suggestions_text = [suggestion.text for suggestion in suggestions if suggestion.text.strip()]

    longest_suggestion = ''
    shortest_suggestion = ''

    if suggestions_text:
        longest_suggestion = max(suggestions_text, key=len)
        shortest_suggestion = min(suggestions_text, key=len)

    df.at[index, longest_col] = longest_suggestion
    df.at[index, shortest_col] = shortest_suggestion
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

driver.quit()

# write on the execle sheet
df.to_excel(excel_file_path, index=False)

print("Search completed and results saved to the Excel file.")



