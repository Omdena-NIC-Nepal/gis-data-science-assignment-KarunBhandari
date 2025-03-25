###Objective
To understand the GIS Data Science, specifically focusing on climate data analysis for Nepal. 
To perform data reading, visualization, and exploratory data analysis (EDA) tasks using Python.

###Activity
The required libraries like Python, Numpy, matplotlib, seaborn, etc were installed. The data were collected from sources like
- https://github.com/Desmondonam/Nepal_Climate_change
- https://opendatanepal.com/
- https://rds.icimod.org/Home/DataDetail?metadataId=36003&utm_source=chatgpt.com
  The data thus collected were analyzed for climate data analysis. The two tasks were performed:

  Task 1: Visualize the GIS data to explore climate patterns
  info_climatechange() function accepting temperature Excel data and district boundaries the file as parameters.
  The file dimension was reduced as it includes data of over a century. The new file contains average data for a decade.
  A plot was drawn that defines increasing temperature based on a color map.
  The precipitation data was plotted for analysis.

  Task 2: Perform EDS analysis of the climate data
  EDA_analysis() function analyzes the data provided.
  A regression plot was created based on selected districts from terai region, region with increasing population, region most effected due to globalwarming and a district from himalayan region.

  Insight from climate patterns
  From the 10 different subplots, it can be insisted that the climate change trend in Nepal resonated with the global warming trend. Though the average temperature was almost consistent till 2011, the temperature then started to rise consistently. Some ditricts in himalayan region faces cooler climate for some decades but the long-term trend in warmer.

  Insight from EDA analysis
  From the regression plot of four different districts lying on different climatic region, it can be seen that the temperature is rising consistently in all the regions irrespective if geography of Nepal.
  
  
  
  
