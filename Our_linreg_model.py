import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import plotly as px 
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from mpl_toolkits.mplot3d import Axes3D

def show():


    st.title("Linear Regression Model")
    alex_df = pd.read_csv("alex_df.csv")

    sale=alex_df[alex_df['Rental Frequency']=='Sale'].drop(['Title','Location','Link','Ownership','Rental Frequency'],axis=1)
    sale = sale.reset_index(drop=True)

    #we will see the distribution of the price
    sale['Price'].plot(kind='hist', bins=20, title='Price')
    plt.gca().spines[['top', 'right',]].set_visible(False)
    st.pyplot(plt)

    st.markdown("The price is highly skewed to the right so we will see the possible reasons")    

    sale=sale[sale['Furnished']!='Not specified'] #we are not interested in non specified data
    sns.boxplot(data=sale, x='Type', y='Price') #drawing the boxplot to see if there is any outliers
    plt.title('Price by Property Type')
    plt.tight_layout()
    st.pyplot(plt)

    st.markdown("There are many outliers in the apartment type so we will see with other possible categories")

    sns.boxplot(data=sale[sale['Type']=='Apartment'], y='Area')  #the outliers of the apartments based on area
    plt.title('Price of Apartments with respect to Area')
    plt.tight_layout()
    st.pyplot(plt)

    st.markdown("There is a nonsense area here so we will remove it")

    sale=sale[sale['Area']<200000] #this will remove this area
    sns.scatterplot(data=sale , x='Price', y='Area',hue='Type')   #a scatter plot to see the relation of price and area
    plt.title('Price with respect to Area')
    plt.tight_layout()
    st.pyplot(plt)

    st.markdown("There seem to be a linear relation between them ,but there is somthing wierd in the areas above 1000 so we will check what's the problem")

    st.write(alex_df[alex_df['Area']>1000])
    st.markdown("after cheking the links there is a misleading information in the area of the appartement and its actual area so we will drop it")

    sns.scatterplot(data=sale , x='Price', y='Area',hue='Near Sea')
    plt.title('Price with respect to Area')
    plt.tight_layout()
    st.pyplot(plt)


    figsize = (12, 1.2 * len(sale['Type'].unique()))
    plt.figure(figsize=figsize)
    sns.violinplot(sale, x='Price', y='Type', inner='box', palette='Dark2')
    sns.despine(top=True, right=True, bottom=True, left=True)
    st.pyplot(plt)


    st.subheader("Preprocessing for models")

    sale['Near Sea']=sale['Near Sea'].astype('int64') #one hot encoding
    sale['Furnished']=(sale['Furnished']=='Yes').astype('int64')

    sale = pd.get_dummies(sale, columns=['Type'], drop_first=True)  #dummy encoding for more than one category variables
    sale.iloc[:, -4:] = sale.iloc[:, -4:].astype(int)  #true->1 ,false->0

    sns.heatmap(sale.corr(),annot=True , fmt='.2f')  #correlation matrix if it approches 1 the relation is strong
    plt.title('Correlation matrix')
    st.pyplot(plt)

    st.markdown("The features thst have strong correlation with price are (bedrooms ,bathrooms ,area) we will choose area for simple linear regression first because it numeric feature")

    st.subheader("Simple Linear Model")

    x=sale['Area'].values.reshape(-1, 1) #we will reshape the x into 2d array so we can model it
    y=sale['Price'].values
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0) #splitting data 80,20
    simple_model=LinearRegression()
    simple_model.fit(X_train,y_train)
    y_pred = simple_model.predict(X_test) #predict the y with the test data

    plt.scatter(X_test, y_test, color='blue', label='Actual Data') #see actial data

    plt.plot(X_test, y_pred, color='red', label='Predicted Line')  #see the predicted line

    plt.title('Linear Regression Model')
    plt.xlabel('Area (X)')
    plt.ylabel('Price (y)')
    plt.legend()
    st.pyplot(plt)

    st.write(r2_score(y_test, y_pred))
    st.markdown("Its actually good if you are going to depend on the area alone not that bad")

    st.subheader("Multiple Linear Regression")

    multiple_model=LinearRegression()

    x=sale.loc[:,sale.columns!='Price'].values
    y=sale['Price']

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

    multiple_model.fit(X_train,y_train)
    st.write("Coefficients:", multiple_model.coef_)
    st.write("Intercept:", multiple_model.intercept_)

    y_pred=multiple_model.predict(X_test)

    mse_mult=mean_squared_error(y_test, y_pred)
    st.write("Mean Squared Error:", mean_squared_error(y_test, y_pred))
    r2_mult = r2_score(y_test, y_pred)
    st.write("R-squared (R²):", r2_mult)

    st.markdown("After using the multiple linear model it became better")

    # Choose high corelated features
    features_3d = ['Area', 'Bedrooms']
    X_3d = sale[features_3d].values
    y_3d = sale['Price']

    # Fit model on those two
    model_3d = LinearRegression()
    model_3d.fit(X_3d, y_3d)

    # Create grid
    area_range = np.linspace(X_3d[:,0].min(), X_3d[:,0].max(), 50)
    bedrooms_range = np.linspace(X_3d[:,1].min(), X_3d[:,1].max(), 50)
    area_grid, bedrooms_grid = np.meshgrid(area_range, bedrooms_range)
    X_grid = np.column_stack((area_grid.ravel(), bedrooms_grid.ravel()))

    # Predict surface
    price_grid = model_3d.predict(X_grid).reshape(area_grid.shape)

    # Plot
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X_3d[:,0], X_3d[:,1], y_3d, color='blue', alpha=0.6, label='Data')
    ax.plot_surface(area_grid, bedrooms_grid, price_grid, color='orange', alpha=0.5)
    ax.set_xlabel('Area')
    ax.set_ylabel('Bedrooms')
    ax.set_zlabel('Price')
    ax.set_title('3D Regression Surface')
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)

