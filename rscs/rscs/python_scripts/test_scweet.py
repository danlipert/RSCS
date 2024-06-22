 # rscs/python_scripts/test_scweet.py

from Scweet.scweet import scrape

data = scrape(words=['Milady'], since="2023-01-01", until="2023-12-31", interval=1, headless=True, display_type="Top")
print(data)