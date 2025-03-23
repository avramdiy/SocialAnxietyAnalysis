# TRG Week 16 Project

- Link to Dataset : https://www.kaggle.com/datasets/natezhang123/social-anxiety-dataset?resource=download

# 1st Commit

- Created data.py, table.html, & associated folders to load enhanced_anxiety_dataset.csv into a HTML Dataframe.

# 2nd Commit

- Filter Data For Analysis

- Remove "Occupation", does not have enough information regarding enhanced anxiety

- Remove "Breathing Rate (breaths/min)", "Sweating Level (1-5)", "Dizziness" I feel that Heart Rate will suffice.

- Remove "Stress Level (1-10)", we are measuring against the Anxiety Level (1-10).

Data is cleaned and ready for analysis.

# 3rd Commit

- Added app.route('/female-anxiety-scatterplot') to define the correlation between higher caffeine intake and higher anxiety for females.

# 4th Commit

- Added app.route('/male-anxiety-scatterplot') to define the correlation between higher caffeine intake and higher anxiety for males.

# 5th Commit