import scraper
import json
import os

def main():

   url = os.getenv("SCRAPER_URL")
   user_agent = os.getenv("SCRAPER_USER_AGENT")

   if not url or not user_agent:
      raise ValueError("Set SCRAPER_URL and SCRAPER_USER_AGENT environment variables")
   
   headers = {"User-Agent": user_agent}

   print("Fetching individual line urls...")
   line_urls: list[str] = scraper.get_lines(url, headers)

   print("Read line urls. Scrapping...")
   sim_timetables: dict[str,dict] = scraper.get_all_timetables(url, headers, line_urls)

   print("Scrape succesful. Saving...")
   with open("tables/timetable.json", "w", encoding="utf-8") as f:
      json.dump(sim_timetables, f, indent=3, ensure_ascii=False)
   print("Saved.")

if __name__ == "__main__":
   main()

