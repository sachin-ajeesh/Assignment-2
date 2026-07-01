ABC Company Employee Analysis

SUMMARY

An Dataset of 458 employees from ABC Company and wanted to figure out what it could actually tell me. How many people are on each team? Which job positions are the most common? Does age have anything to do with how much someone gets paid? Where is all the salary money actually going?
This repo is my attempt to answer those questions — starting with cleaning up some messy data, then exploring it, visualizing what stood out, and writing down what I actually learned along the way.
I used Python (Pandas, NumPy, Matplotlib, Seaborn) in a Jupyter Notebook to do all of this.
The Dataset
Nothing fancy here — just a spreadsheet with 458 rows and 9 columns, one row per employee.
Each row includes:NAME,TEAM,POSITION,AGE,HEIGHT,COLLEGE,SALARY
A few other employee attributes
Tools I Used
Nothing exotic — just the usual data analysis toolkit:PYTHON,PANDAS,NUMPY,MATPLOTLIB,SEABORN,JUPYTER NOTEBOOK
Like most real-world data, this dataset wasn't perfectly clean out of the box.
The Height column was a problem
The Height values in the original data were all over the place and didn't look trustworthy, so instead of trying to salvage them, I just regenerated the column with random values between 150–180 cm. I set a random seed so anyone re-running this notebook gets the exact same numbers I did:
What I Actually Looked At
1. Who's on which team?
I counted up how many employees belong to each team and worked out what percentage of the total workforce each one represents, then plotted it as a count plot to make the differences easy to see at a glance.
2. What jobs do people have?
Same idea, but for job positions. I made this one a horizontal bar chart instead, mostly because the job titles were too long to squeeze onto a normal x-axis without them overlapping.
3. What's the most common age range?
I split everyone into six age brackets — 18–25, 26–30, 31–35, 36–40, 41–45, and 46–50 — and charted how many employees fall into each one. This is a quick way to see whether the company skews younger, older, or somewhere in the middle.
4. Where's the salary budget going?
I added up total salary spend by team and by position separately, so it's obvious which departments and roles are pulling in the biggest chunk of payroll.
5. Does age affect salary?
I ran a Pearson correlation between age and salary and plotted it as a scatter plot with a regression line, just to see if there's any visible trend — do people earn more as they get older, or is it pretty much random?
The Charts You'll Find in the Notebook
Employee distribution across teams
Employee distribution by position
Age group distribution
Salary expenditure by team
Salary expenditure by position
Age vs. salary scatter plot
So, What Did I Learn?
Teams aren't sized evenly — a few are clearly bigger than the rest.
A small number of job positions make up a disproportionate chunk of the workforce.
There's one age group that shows up more than any other.
Salary spending isn't spread out evenly either — it's concentrated in specific teams and roles.
The age-vs-salary correlation gives a decent, if imperfect, sense of whether tenure/age translates into higher pay here.
This was a good exercise in taking a raw, slightly messy dataset and turning it into something you can actually learn from — clean it up, explore it, visualize it, and draw conclusions worth sharing. By the end, I had a much clearer picture of how ABC Company's employees are distributed, where the payroll budget really goes, and whether age has any real bearing on salary.
