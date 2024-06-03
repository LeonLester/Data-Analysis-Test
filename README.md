# Data-Analysis-Test
Interview technical task for IDC

First version is a simple implementation, without any CRM db connection mocking for the tests, as the original task emphasizes on the string matching logic.

## Task 1 – Python

Finish the Python test here: ./Test Files/01_Python_test.py

## Task 2 – SQL

Let’s have a following table in PostgreSQL or Snowflake that contains the data about # of clicks on a websites per user and client

| Name              | Day         | Clicks |
|-------------------|-------------|--------|
| Oakley Sosa       | 2022-01-31  | 10     |
| Francesca Dotson  | 2022-02-15  | 321    |
| Abel Valdez       | 2022-01-15  | 56     |
| Yasin Rowland     | 2022-01-15  | 12     |

[-] Show a number of clicks by User and calendar month
[-] Show a share of clicks of each user by month
Test data are stored in ./Test Files/Website Statistics Data.csv
Please use the service https://sqliteonline.com/ and use any database there.

### Solution can be found in file queries.sql

## Task 3 – Architecture

The users mentioned in Task 2 also have records in the CRM database. At the end of each month, the sales department needs to match the usage data from website and with the CRM database for each user for further analysis. The user names in CRM and Website database are inconsistent, CRM has names in the following format:

| User Name              | Start Date  | Subscription Revenue in Past 3 Months |
|------------------------|-------------|---------------------------------------|
| O. Sosa                | 1998-03-01  | $1,500                                |
| Mrs. Francesca Dotson  | 2005-04-01  | $200                                  |
| Abel Valdez, Phd.      | 2000-12-01  | $350                                  |
| Yasin Rowland, MBA     | 2010-01-01  | $100                                  |

1. Propose a Python solution that will solve the matching problem above – reads the data from source databases > matches both inputs by client name > save the result back to the database
2. Client names in both sources may not be consistent so exact matching/comparison may not work for 100% cases. The solution should include multiple matching strategies that can be applied to maximize the match rate.
3. Implement the solution using Python. The implementation should address key areas, although a production-ready implementation is not mandatory.
4. Describe how you would validate the result of the matching result during initial implementation and also during possible future enhancements of the matching algorithm by another developer

### Solution

The file string_match.py contains the functions needed for the string matching.
It uses Levenshtein and Jaccard string similarity.

For future enhancements, there could be more algorithms added to get better accuracy.
A list of top 5 (or n) matches can be filtered and them a different algorithm can be re-applied to the reduced list, in case a different answer arises.

The implementation can be tested with the test_string_match.py test file.
