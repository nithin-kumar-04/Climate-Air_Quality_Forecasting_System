import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

def generate_mock_data(start_date='2020-01-01', periods=1000):
    """
    Generates mock climate and air quality data.
    """
    date_rng = pd.date_range(start=start_date, periods=periods, freq='D')
    
    # Generate mock features with some realistic-ish distributions
    temp = np.random.normal(loc=25, scale=5, size=periods) # Normal distribution for temperature
    humidity = np.random.uniform(low=30, high=90, size=periods) # Uniform distribution for humidity
    pm25 = np.random.lognormal(mean=3, sigma=0.8, size=periods) # Lognormal for PM2.5 (often skewed right)
    no2 = np.random.gamma(shape=2, scale=10, size=periods) # Gamma for NO2
    co = np.random.exponential(scale=1.5, size=periods) # Exponential for CO
    
    df = pd.DataFrame({
        'date': date_rng,
        'temperature': temp,
        'humidity': humidity,
        'pm2_5': pm25,
        'no2': no2,
        'co': co
    })
    return df

def analyze_baseline_distribution(df):
    """
    Analyzes baseline data distribution and creates plots.
    """
    print("Dataset Info:")
    print(df.info())
    print("\nDataset Describe:")
    print(df.describe())
    
    # Plotting distributions
    features = ['temperature', 'humidity', 'pm2_5', 'no2', 'co']
    
    fig, axes = plt.subplots(len(features), 1, figsize=(10, 15))
    fig.tight_layout(pad=5.0)
    
    for i, feature in enumerate(features):
        sns.histplot(df[feature], kde=True, ax=axes[i], color='skyblue')
        axes[i].set_title(f'Distribution of {feature}')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Frequency')
        
    plt.show()

if __name__ == "__main__":
    print("Setting up exploratory environment for Climate/Air Quality Forecasting...")
    mock_df = generate_mock_data()
    analyze_baseline_distribution(mock_df)
    print("Baseline distribution analysis complete.")
