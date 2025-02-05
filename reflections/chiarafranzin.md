# 1. Technical Contributions
- I handled all the visualisations for this project
- As seen in [this notebook](../code/Visualisations/NB03_gdp_art_visualisations.ipynb) and [this notebook](../code/Visualisations/NB03_gdp_social_movements.ipynb), I tried to use vary different graphs to plot similar data in order to understand which one shows the data the best.
- I often made changes to my graphs to ensure that they were accessible to people with colour blindness such as the final bubble graph in [this notebook](../code/Visualisations/NB03_gdp_social_movements.ipynb) as I changed the colour map to be more accessible and I changed the colour of the writing of the year in order to increase its visibility
- I wrote part of the [README](../README.md) in collaboration with my team mate as seen in [this](/files/ds105a-2024-project-data_dazzlers/commit/d7a61cf0648786ec3b885861c474513582791332), [this](/files/ds105a-2024-project-data_dazzlers/commit/a50aab0a5ef81f458500810ba1b9be6db13177ad) and [this](/files/ds105a-2024-project-data_dazzlers/commit/826a02f4e174edcd2feb3aae228ca388726accc8) and many other commit links 
- A big problem in our project was the fact that GDELT data went up to 2006, due to the recent nature of social media, but the Smithsonian data did not have many entries for artworks made in the 21st century. My team mate tried to make visualisations in [this notebook](../code/Visualisations/NB03_social_movements_visualisations.ipynb) however was unsuccessful in making any representative visualisations due to the nature of both the datasets. Using the data that we did have, I made a line graph at the very bottom of the notebook as seen by [this](/files/ds105a-2024-project-data_dazzlers/commit/9e4fba216517c71335af67a4872a7b922e1db201) commit link
- Furthermore, after encountering problems with visualisations between art themes and social movements, I suggested the idea of changing this part of the research to be focused on the relationship between social movements and GDP so that we didn't have to abandon looking at social movements. Then I made all the visualisations for this relationship [here](../code/Visualisations/NB03_gdp_social_movements.ipynb)

--------


# 2. Team Collaboration
- I went through this [data collection notebook](../code/GDELT_Data/NB01_Data_Collection.ipynb) made by team mate and added the notes and made sure that one of the functions did not print out numerous, repetitive warnings as seen by [this](/files/ds105a-2024-project-data_dazzlers/commit/784ed631b8bd8a4042f14f7f63c1a510debcff77) and [this](/files/ds105a-2024-project-data_dazzlers/commit/fd6cd3fa80bcc5524769923b968881705a8bf66d) commit links
- I contributed to the Word Document created by my team mate by writing the analysis and conclusion for some of the visualisations
- I also wrote "Background of this project" part of the website created by my team mate
- I was often quickly avaliable on our group chat, ensuring good communication especially if a team mate was running into an issue (as seen in the section above, I quickly came up with a new idea to the visualisation problem and acted from there). 
- Furthermore before committing to any visualisation, I often consulted my team mates to make sure that everyone was on the same page
- I made the 'reflections' folder with a markdown file for each one of my team mates
- I created a time line with dead lines for us to stick to



------


# 3. Learning Journey
- Throughout the whole Data Science course I developed crucial skills such as how to collect data, clean it and visualise it. But before this project, I did basic visualisations. This project forced me to go past these basic visualisations in order to create graphs that properly represent our data in an accessible manner (such as the heatmap for the Smithsonian and FRED data which conveys all the data, for the top 20 art themes and the GDP from the 1920s to the 2010s, at the same time). Furthermore, before this project I was not aware that it was possible to make interactive graphs so I was really happy when I learned to make them successfully
- I also have enhanced my ability to use Github, which I believe is vital for any future coding projects. Having worked on my own in the previous two projects, I was not comfortable with working with separate branches and having to pull everything from Github every time you want to make a change when working collaborately with team mates on the same branch
- A challenge was representing data in a heatmap when there were a limited amount of data points for recent years (meaning that a lot of the rows would just be fully dark and no trend would show). I fixed this by calculating the ratio of art works per year

Areas for future growth:
- Exploring more with visualisations such as learning to make short animations
- Learning to make plot with libraries other than matplotlib and plotly
