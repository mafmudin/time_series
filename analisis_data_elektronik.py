import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

if __name__ == '__main__':
    # Baca data Excel
    data = pd.read_excel('dataset_electric_unclean.xls')

    print(data)
    # Konversi kolom tanggal menjadi datetime
    data['DATE'] = pd.to_datetime(data['DATE'])

    # Atur kolom tanggal sebagai index
    data.set_index('DATE', inplace=True)

    # Periksa data yang hilang
    print(data.isnull().sum())

    # Mengisi atau membuang data yang hilang jika diperlukan
    data = data.dropna()

    # Periksa statistik deskriptif
    print(data.describe())

    # Buat grafik time series
    data.plot()
    plt.title('Time Series Data')
    plt.show()

    # Dekomposisi time series
    decomposition = seasonal_decompose(data['IPG2211A2N'])

    # Visualisasikan komponen trend, musiman, dan noise
    decomposition.plot()
    plt.show()

    # Bangun model ARIMA
    model = ARIMA(data['IPG2211A2N'], order=(1, 1, 1))
    model_fit = model.fit()

    # Predict future values (replace start and end dates)
    prediksi = model_fit.predict(start='2019-01-01', end='2019-12-31')

    # Plot actual data and predictions
    plt.plot(data['IPG2211A2N'], label='Data Aktual')
    plt.plot(prediksi, label='Prediksi')
    plt.legend()
    plt.title('Actual Data vs Predictions')
    plt.show()
