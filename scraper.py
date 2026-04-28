from bs4 import BeautifulSoup
import requests

def get_lines(url: str, headers: dict[str,str]) -> list[str]:
   '''
   Saves subpage address for individual bus lines in a list.
   Args:
      url: 
         Str. Line catalog webpage.
      headers: 
         Dict. User-agent info for requests
   Returns:
      list: 
         List with subpage adresses
   '''

   response = requests.get(url, headers=headers, timeout=15)
   response.raise_for_status()
   html_text = response.text
   soup = BeautifulSoup(html_text, "lxml")

   lines_url = [
      u.get("href")
         for u in soup.find_all("a") 
         if u.get("href") and u.get("href").startswith("/horarios/")] # type: ignore

   lines_url = [u.replace("/horarios", "") for u in lines_url] #type: ignore

   return lines_url

def get_timetables(url: str, headers:dict[str,str], session: requests.Session | None = None) -> dict[str,dict]:
   """
   Get timetable data from individual line url.
   Args:
      url:
         Str: Specific line url
      headers:
         dict: Session headers
      session:
         session [optional]: requests session
   Returns:
      dict[str,dict]: timetable data
   """
   line: dict[str,dict] = {}
   client = session or requests
   response = client.get(url, headers=headers, timeout=15)
   response.raise_for_status()
   html_text: str = response.text
   soup = BeautifulSoup(html_text, "lxml")
   line_name: str = soup.find("h3").text.replace("\xa0", " ") #type:ignore
   timetable = soup.find("div", class_ = "content-horarios-int")
   terminals = timetable.find_all("h5", class_ = "font-bold") #type:ignore
   line[line_name] = {}

   for t in terminals: line[line_name][t.text] = {"Dias Úteis": [], "Sábado": [], "Domingos e Feriados": []}

   for t in terminals:
      departures = t.find_parent("div", class_ = "row d-none d-sm-flex")
      departures = departures.find_next_sibling("div", class_ = "row row-horarios") #type:ignore
      departures = departures.find_all("div", class_ = "col-4 col-md-2") #type:ignore  
      for departure in departures:
        line[line_name][t.text][departure["data-semana"]].append(departure["data-horario"])

   return line



def get_all_timetables(url: str, headers: dict, line_urls: list) -> dict[str,dict]:
   """
   Fetches data from all line urls in a list
   Args:
      url:
         str: base url
      headers:
         dict: requests session header
      line_url:
         list: list of suburls
   Returns:
      dict[str][dict]: timetable data for all lines in list
   """
   sim_timetable : dict[str,dict] = {}
   with requests.Session() as session:
      for suburl in line_urls:
         line_url = url + suburl
         line_timetable = get_timetables(line_url, headers, session=session)
         print(f"Scraped {line_url}...")
         sim_timetable.update(line_timetable)

   return sim_timetable
