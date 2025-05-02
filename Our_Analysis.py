import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import plotly as px 
import seaborn as sns


def show():

    st.title("Alex Apartments Dataset Analysis We Performed ")

    alex_df = pd.read_csv("alex_df.csv")
    st.subheader("Dataset")
    st.write(alex_df)


    #boxplots                                                                                            

    st.subheader("Price Distribution by Rental Frequency")


    # Set plot style
    #sns.set(style="whitegrid")

    # Create box plot to visualize price spread across rental frequencies
    plt.figure(figsize=(15, 8))
    sns.boxplot(data=alex_df, x='Rental Frequency', y='Price', palette='Set3')

    # Add title and labels
    #plt.title('Price Distribution by Rental Frequency')
    plt.xlabel('Rental Frequency')
    plt.ylabel('Price')
    plt.yscale('log')  # Use log scale to handle wide price range
    plt.tight_layout()
    st.pyplot(plt)




    #barplot

    # Compute average price per location
    top_locations = alex_df.groupby('Location')['Price'].mean().sort_values(ascending=False).head(10)

    st.subheader("Top 10 Locations by Average Price")
    # Bar plot of top 10 locations by average price
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_locations.values, y=top_locations.index, palette='viridis')

    # Add title and labels
    #plt.title('Top 10 Locations by Average Price')
    plt.xlabel('Average Price')
    plt.ylabel('Location')

    plt.tight_layout()
    st.pyplot(plt)



    #pie chart

    # Count furnished vs unfurnished
    furnishing_counts = alex_df['Furnished'].value_counts()

    st.subheader("Furnished vs Unfurnished Listings")
    
    plt.figure(figsize=(6, 6))
    plt.pie(furnishing_counts, labels=furnishing_counts.index, autopct='%1.1f%%', colors=['#edad8d','#ed8dd1', '#8dedc6'])
    #plt.title('Furnished vs Unfurnished Listings')
    plt.axis('equal')  # Equal aspect ratio for a perfect circle
    st.pyplot(plt)



    # Pivot the dataframe to get a matrix format (Bedrooms as rows, Bathrooms as columns)

    st.subheader("Average Price by Number of Bedrooms and Bathrooms")

    avgPrice_BedBath = alex_df.groupby(['Bedrooms', 'Bathrooms'])['Price'].mean().reset_index()
    heatmap_data = avgPrice_BedBath.pivot(index='Bedrooms', columns='Bathrooms', values='Price')

    # Plot the heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlGnBu")

    #plt.title('Average Price by Number of Bedrooms and Bathrooms')
    plt.xlabel('Number of Bathrooms')
    plt.ylabel('Number of Bedrooms')
    plt.tight_layout()

    st.pyplot(plt)



    #multiple bar cahrt
    # Define keyword mapping to group locations
    location_keywords = {
        'Smoha': 'Smoha',
        'Agami': 'Agami',
        'Moharam Bik': 'Moharam Bik',
        'Sidi Beshr': 'Sidi Beshr',
        'Miami': 'Miami',
        'Sidi Gaber': 'Sidi Gaber',
        'Kafr Abdo': 'Kafr Abdo',
        'Seyouf': 'Seyouf',
        'Al Ibrahimiyyah': 'Al Ibrahimiyyah',
        'Saba Pasha': 'Saba Pasha',
        'Mandara': 'Mandara',
        'Roushdy': 'Roushdy',
        'Sporting' : 'Sporting',
        'Stanley' : 'Stanley'
    }

    # Function to match and clean location names
    def match_location(location):
        for keyword, standard_name in location_keywords.items():
            if keyword.lower() in str(location).lower():
                return standard_name
        return None  # Not in our selected list

    # Create a new filtered column for standardized locations
    alex_df['Filtered_Location'] = alex_df['Location'].apply(match_location)

    # Drop rows not matching any of the selected keywords
    filtered_df = alex_df.dropna(subset=['Filtered_Location'])


    # Group by cleaned location and type
    avgPrice_Location_filtered = filtered_df.groupby(['Filtered_Location', 'Type'])['Price'].mean().reset_index()

    # Calculate average price per location and type
    avgPrice_Location_filtered = filtered_df.groupby(['Filtered_Location', 'Type'])['Price'].mean().reset_index()

    # Sort by descending average price (you can pick just one type or overall avg)
    # If you want to sort based on total average price regardless of type:
    order = avgPrice_Location_filtered.groupby('Filtered_Location')['Price'].mean().sort_values(ascending=False).index


    st.subheader("Average Price by Selected Locations and Property Type (Sorted Descending)")
    # Plot with sorted order
    plt.figure(figsize=(14, 8))

    sns.barplot(
        data=avgPrice_Location_filtered,
        x='Filtered_Location',
        y='Price',
        hue='Type',
        palette='Set2',
        order=order  # <-- enforce location order
    )

    # Formatting
    #plt.title('Average Price by Selected Locations and Property Type (Sorted Descending)')
    plt.xlabel('Location')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45, ha='right')
    plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x):,}'))
    plt.tight_layout()
    st.pyplot(plt)












