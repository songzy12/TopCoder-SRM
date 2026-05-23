import os
import json
import requests
from bs4 import BeautifulSoup


def main():
    url = "https://archive.topcoder.com/ProblemArchive"

    if os.path.exists("archive/tc.html"):
        print("Using local tc.html...")
        with open("archive/tc.html", "r", encoding="utf-8") as f:
            html_content = f.read()
    else:
        print(f"Fetching {url}... This might take a few seconds.")
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text
        except Exception as e:
            print(f"Error fetching the page: {e}")
            return

    soup = BeautifulSoup(html_content, 'html.parser')
    tbody = soup.find('tbody')

    if not tbody:
        print("Could not find the table body.")
        return

    problems = {}

    for row in tbody.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) < 9:
            continue

        prob_name = cols[0].text.strip()
        challenge = cols[1].text.strip()

        # Date string typically looks like '2024-05-22 16:46:00.0'
        raw_date = cols[2].text.strip()
        date_only = raw_date.split(' ')[0] if raw_date else ""

        year = date_only.split('-')[0] if date_only else "Unknown"

        # Categories usually comma-separated
        raw_categories = cols[4].text.strip()
        categories = [c.strip() for c in raw_categories.split(',')
                      ] if raw_categories else []

        div1_level = cols[5].text.strip()
        div2_level = cols[7].text.strip()

        div_levels = []
        if div1_level:
            div_levels.append(("1", div1_level))
        if div2_level:
            div_levels.append(("2", div2_level))

        if not div_levels:
            div_levels.append(("Unknown", "Unknown"))

        if year not in problems:
            problems[year] = {}
        if challenge not in problems[year]:
            problems[year][challenge] = {}

        for div, level in div_levels:
            if div not in problems[year][challenge]:
                problems[year][challenge][div] = []

            problems[year][challenge][div].append({
                "level": level,
                "problem_name": prob_name,
                "categories": categories
            })

    for year in problems:
        for challenge in problems[year]:
            div_list = []
            for div in problems[year][challenge]:
                problems[year][challenge][div].sort(key=lambda x: x["level"])
                div_list.append({
                    "div": div,
                    "problems": problems[year][challenge][div]
                })
            div_list.sort(key=lambda x: x["div"])
            problems[year][challenge] = div_list

    output_file = "metadata.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(problems, f, indent=4)

    print(
        f"Successfully extracted {len(problems)} problems into {output_file}.")


if __name__ == "__main__":
    main()
