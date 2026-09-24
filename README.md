# TopCoder-SRM

- https://archive.topcoder.com/
    - https://archive.topcoder.com/SRM/index.html
    - https://archive.topcoder.com/TCO/index.html
- https://clist.by/standings/?resource=12

* 2012: SRM 529 ~ 565
* 2013: SRM 566 ~ 602
* 2014: SRM 603 ~ 643
* 2015: SRM 645 ~ 677
* 2016: SRM 678 ~ 704
* 2017: SRM 705 ~ 726
* 2018: SRM 727 ~ 745
* 2019: SRM 746 ~ 773
* 2020: SRM 774 ~ 796
* 2021: SRM 797 ~ 820
* 2022: SRM 821 ~ 842
* 2023: SRM 843 ~ 851
* 2024: SRM 852 ~ 855

## Clone

```bash
git clone git@github.com:songzy12/TopCoder-SRM.git --single-branch

cd TopCoder-SRM
git clone -b archive git@github.com:songzy12/TopCoder-SRM.git data/archive
git clone -b tests git@github.com:songzy12/TopCoder-SRM.git tests
```

## Project layout

The repository is organized into three main areas:

- `SRM/`: the contest source of truth. Problem solutions are grouped by year and round.
- `app/`: web application code and templates.
- `data/`: generated metadata, problem mapping, and archived HTML content.
- `scripts/`: automation for crawling, parsing, and running validation.
- `tests/`: JSON-based test cases for solutions.

```text
TopCoder-SRM/
├── SRM/
├── app/
│   └── web/
├── data/
│   ├── archive/
│   ├── metadata.json
│   └── problem_mapping.json
├── scripts/
│   ├── crawler/
│   └── tools/
├── tests/
├── README.md
├── run_tests.sh
├── run_webapp.sh
├── requirements.txt
└── .gitignore
```

## Common workflows

### Run the web app

```bash
./run_webapp.sh
```

### Run a solution against a test file

```bash
./run_tests.sh
```

The script expects a config file named `run_tests.conf` with `SOLUTION` and `TESTS` values set.

### Regenerate archive metadata

```bash
cd scripts/crawler
python parse_archive.py
```

### Regenerate test JSON files

```bash
cd scripts/tools
python generate_test_cases.py
```
