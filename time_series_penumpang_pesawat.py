import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

if __name__ == '__main__':
    # Data from the image
    data = {
        'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November'],
        'Tahun 1': [110, 115, 132, 128, 127, 135, 145, 125, 119, 126, 138],
        'Tahun 2': [120, 125, 140, 120, 130, 125, 140, 135, 124, 135, 127]
    }
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Combine data for both years into a single time series
    df['Combined'] = df['Tahun 1'] + df['Tahun 2']

    # Create a time index
    df.index = pd.date_range(start='1/1/2023', periods=len(df), freq='M')

    # Extend data to have at least 24 points by repeating it and adding more points
    df_extended = pd.concat([df] * 2, ignore_index=True)

    # Adding two more months by extrapolation
    additional_data = {
        'Bulan': ['Desember', 'Januari'],
        'Tahun 1': [130, 110],
        'Tahun 2': [130, 120],
        'Combined': [260, 230]
    }
    additional_df = pd.DataFrame(additional_data)
    df_extended = pd.concat([df_extended, additional_df], ignore_index=True)

    df_extended.index = pd.date_range(start='1/1/2023', periods=len(df_extended), freq='M')

    # Decompose the time series
    result = seasonal_decompose(df_extended['Combined'], model='additive', period=12)

    # Plot the decomposition
    plt.figure(figsize=(12, 8))
    plt.subplot(411)
    plt.plot(result.observed, label='Observed')
    plt.legend(loc='upper left')
    plt.subplot(412)
    plt.plot(result.trend, label='Trend')
    plt.legend(loc='upper left')
    plt.subplot(413)
    plt.plot(result.seasonal, label='Seasonal')
    plt.legend(loc='upper left')
    plt.subplot(414)
    plt.plot(result.resid, label='Residual')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
