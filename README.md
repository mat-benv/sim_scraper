# sim_scraper

A small Python scraper that collects bus timetable data from a company in the Integrated Mobility System (SIM) from Florianópolis, Brazil and saves it as JSON.

Made for learning and possible future projects.

No AI used for writing the code.

## Requirements

- `requests`
- `beautifulsoup4`
- `lxml`

```bash
pip install requests beautifulsoup4 lxml
```

## Required environment variables:

```bash
export SCRAPER_URL="https://www.c********f****.com.br/horarios" #change to proper url
export SCRAPER_USER_AGENT="Mozilla/5.0 ..." #change to your user agent of choice
```

## Project structure

```text
main.py
scraper.py
tables/
  timetable.json
```