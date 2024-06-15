import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


# Function to reformat 'minggu' value
def reformat_minggu(minggu):
    minggu = str(minggu)  # Convert integer to string
    year = minggu[:4]
    week = minggu[4:]
    return f"{year}({week})"


if __name__ == '__main__':
    # Load the CSV file with the correct delimiter
    file_path = 'rekam_medik_perminggu.csv'
    df = pd.read_csv(file_path, delimiter=';')

    # Apply the reformat function to 'minggu' column
    df['minggu'] = df['minggu'].apply(reformat_minggu)

    # Set 'minggu' as the index
    df.set_index('minggu', inplace=True)

    # Analisis deskriptif
    deskripsi = df['jumlah_data'].describe()
    print(deskripsi)

    # Plot the time series data (Scatter Plot)
    plt.figure(figsize=(12, 6))
    plt.scatter(df.index, df['jumlah_data'], label='Actual')
    plt.plot(df.index, df['jumlah_data'], color='gray', alpha=0.5)  # Add a faint line for reference
    plt.title('ARIMA Forecast (Scatter Plot)')
    plt.xlabel('Minggu')
    plt.ylabel('Jumlah Data')
    plt.legend()
    plt.show()

    # Plot the time series data (Line Graph)
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['jumlah_data'], label='Actual', marker='o')  # Plot actual data with markers
    plt.plot(df.index, df['jumlah_data'], color='gray', alpha=0.5)  # Add a faint line for reference
    plt.title('ARIMA Forecast (Line Graph)')
    plt.xlabel('Minggu')
    plt.ylabel('Jumlah Data')
    plt.legend()
    plt.show()

    # Fit an ARIMA model
    model = ARIMA(df['jumlah_data'], order=(1, 1, 1))
    model_fit = model.fit()

    # Print summary of the model
    print(model_fit.summary())

    # Forecast for the next 10 weeks
    forecast = model_fit.forecast(steps=100)

    # Plot the forecast
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['jumlah_data'], label='Actual', marker='o')  # Plot actual data with markers
    plt.plot(df.index, df['jumlah_data'], color='gray', alpha=0.5)  # Add a faint line for reference
    plt.plot(df.index[-1] + pd.date_range(start=df.index[-1], periods=10, freq='W'), forecast, label='Forecast',
             color='red')  # Plot forecast
    plt.title('ARIMA Forecast')
    plt.xlabel('Minggu')
    plt.ylabel('Jumlah Data')
    plt.legend()
    plt.show()
