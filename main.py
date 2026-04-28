import scraper
import json
from datetime import datetime as dt

def main():

   url = "https://www.consorciofenix.com.br/horarios"
   headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}

   print("Fetching individual line urls...")
   line_urls: list[str] = scraper.get_lines(url, headers)

   print("Read line urls. Scrapping...")
   sim_timetables: dict[str,dict] = scraper.get_all_timetables(url, headers, line_urls)

   print("Scrape succesful. Saving...")

   filename = f"log/{dt.now().isoformat()}.json"
   with open(filename, "w", encoding="utf-8") as f:
      json.dump(sim_timetables, f, indent=3, ensure_ascii=False)
   print("Saved.")

if __name__ == "__main__":
   main()

