# sim_scraper

A small Python scraper that collects bus timetable data from a company in the Integrated Mobility System (SIM) from Florianópolis, Brazil and saves it as JSON.

Made for learning and possible future projects.

No AI used for writing the code.

## Requirements

- `requests`
- `beautifulsoup4`
- `lxml`
- `datetime`

```bash
pip install requests beautifulsoup4 lxml datetime
```

## Project structure

```text
main.py
scraper.py
log/
  *.json
```