# Singapore HDB Flat Resale Analysis

This project analyzes Singapore HDB resale flat data to gain insights into pricing trends, factors affecting resale prices, and the impact of various attributes like flat type, floor area, town, and lease period on pricing.

---

## Analysis and Insights

The analysis covers several key areas:

- **Geospatial Visualization:** Mapping resale prices across towns to identify price hotspots and regional trends.  
- **Price Analysis:** Examining the distribution of resale prices and detecting outliers.  
- **Location-Based Insights:** Comparing average resale prices in different towns to understand regional variations.  
- **Flat Type Analysis:** Investigating resale price differences among flat types such as 2-room, 3-room, and 5-room flats.  
- **Lease and Age Analysis:** Analyzing how the remaining lease and age of the flat impact resale prices.  
- **Correlation Analysis:** Exploring relationships between numerical features like floor area, lease duration, and resale price.

### Key Insights

- Flats with larger floor areas and more rooms tend to have higher resale prices.  
- Certain towns are associated with significantly higher average prices.  
- Older flats or flats with shorter remaining leases generally have lower prices.  
- Flat type and location together are strong indicators of resale price trends.

---

## Future Implementation

This project can be further enhanced by deploying it as an interactive web application using **Streamlit**, allowing users to explore pricing trends, visualize geospatial distributions, and predict resale prices based on selected parameters.

---

## How to Run the Notebook

Ensure you have **Python** and the necessary libraries installed:

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn streamlit
