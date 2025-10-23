Airbnb Data Analysis
This project analyzes Airbnb data to gain insights into pricing trends, availability patterns, and the impact of various factors like location, property type, and amenities on pricing.

Data Source
The data is retrieved from a MongoDB Atlas cluster.

Analysis and Insights
The analysis covers several key areas:

Geospatial Visualization: Visualizing the distribution of Airbnb listings and their prices globally to identify price hotspots.
Price Analysis: Examining the distribution of prices and identifying outliers.
Location-Based Insights: Analyzing average prices in different locations to understand regional pricing variations.
Property Type Analysis: Investigating the average prices for different property types to identify premium and budget-friendly options.
Seasonal Availability and Pricing: Analyzing how availability and pricing vary across different seasons.
Correlation Analysis: Exploring the relationships between numerical features like price, bedrooms, bathrooms, and availability.
Amenities Analysis: Examining the impact of different amenities on average prices and their distribution across property types.
Some key insights from the analysis include:

Properties with more bedrooms and bathrooms tend to have higher prices.
Certain locations and property types are associated with significantly higher average prices.
Availability across different time periods is highly correlated.
Some amenities are associated with higher average prices, likely due to catering to luxury stays.
Future Implementation
This project can be further enhanced by deploying it as a web application using Streamlit. This would allow users to interact with the data and visualizations, making the insights more accessible and actionable.

How to Run the Notebook
Ensure you have Python and the necessary libraries installed (pymongo, pandas, numpy, plotly, geopy, seaborn, matplotlib). You can install them using pip:
