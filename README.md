# Compatibility Predictor

## Functionality

Read a JSON file and parse the data into a "team" and "applicants" list and score each applicant between 0 and 1 depending on how compatible they are in the team.

## Scoring Algorithm
Each attribute has a calculated mean and standard deviation. To be considered "compatible", the applicant's attributes must be within the range of the team's attributes. Likewise, the applicant's attributes should benefit the overall team's attributes.

For example, if the team's mean intelligence increases with the addition of the new applicant, then it benefits the team. However, if the standard deviation increases, then the spread in attributes increases which makes that applicant less fit for the team.

Every applicant starts with a score of 1.

For every time the applicant does not benefit the team (i.e. decreasing the attribute mean or increasing the attribute standard deviation), the percent change is multiplied by the current score, and continues until it iterates through every attribute. If the applicant is a good fit based on the attribute, the score remains the same.

The greater the decrease of the mean, the greater the affect on the score. Likewise, the greater the increase of the standard deviation, the greater the affect on the score.

## Execution
The input JSON is located in the `input.json` file.

The output JSON is located in the `output.json` file. If this file does not exist, the program will create it.

The program can be run using Python3:
```
$ python3 app.py
```
