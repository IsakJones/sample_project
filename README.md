# sample_project

Hi! This is my sample project in my application to the Recurse Center. 

In this project, I amass a large amount of data, mostly taken from Google Trends through an unofficial API, and generate some cool visualizations. The goal was to show the unprecedented search traffic for the 2020 presidential elections, collecting global data and analyzing individual countries, and explore some trends in global search traffic. I originally created this project in May 2021 for a university paper, but it was a class on Foreign Policy, and coding was not expected! I mostly used the class as an excuse to embark on a fun, challenging programming project.

I think this is a good sample project because it shows strong familiarity with Python and the ability to juggle different libraries (e.g. pandas, matplotlib) and APIs (e.g. the wbgapi API that provides economic data from the World Bank).

I originally published my code in this other repository. Since then, I've cleaned up the code to make it more readable. I will now describe the contents of each table:

 - country_table.csv: a table with (almost) all UN member states, including their name, alpha 2 & 3 codes, G20 membership, and other statistical factors like 2019 GDP per capita in USD
 - monthly_df.csv: a table with almost all UN member states and their search traffic over time for the "United States" topic.
 - hourly_df.csv: a one-column table with global hourly traffic for "United States" during a two-week period surrounding the election.

I will now describe the content of each script:

 - grapher.ipynb: the file that generates all the visualizations. All cells can only be run if the other three tables have already been generated.
 - country_table_creator.py: the first file that assembles country_table.csv.
 - statistical_additions.py: the second file that assembles country_table.csv. It cannot be executed before country_table_creator.py has run.
 - monthly_df_reator.py: assembles monthly_df.csv.
 - hourly_df_creator.py: assembles hourly_df.csv.

Lastly, the Jones_Final_Paper.pdf is the final paper I wrote. I made sure to have the visualizations' font and general aesthetic match those of the Word file.

Thank you for reviewing this! 
