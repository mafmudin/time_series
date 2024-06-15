import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


def forecast_day(data, day_name):
    # Menerapkan model ARIMA
    model = ARIMA(data['jumlah_data'], order=(1, 1, 1))
    model_fit = model.fit()

    # Melakukan prediksi untuk 5 periode ke depan (5 minggu berikutnya)
    forecast = model_fit.forecast(steps=5)

    # Memvisualisasikan hasil prediksi
    plt.figure(figsize=(12, 6))
    plt.scatter(data.index, data['jumlah_data'], label='Actual')
    plt.plot(data.index, data['jumlah_data'], color='gray', alpha=0.5)  # Add a faint line for reference
    plt.plot(pd.date_range(start=data.index[-1] + pd.Timedelta(weeks=1), periods=5, freq='W'), forecast,
             label='Forecast', color='red')  # Plot forecast
    plt.title(f'ARIMA Forecast for {day_name}')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Data')
    plt.legend()
    plt.show()

    print(f"Prediksi kedatangan pasien pada hari {day_name} untuk 5 periode ke depan:")
    for i, value in enumerate(forecast):
        print(f"Periode {i + 1}: {value}")

if __name__ == '__main__':
    # Membaca data dari file Excel
    file_path = 'rekam_medik_perhari_dengan_nama.xls'  # Ganti dengan lokasi file Excel yang sesuai
    df = pd.read_excel(file_path)

    # Mengubah kolom 'tanggal' menjadi tipe data datetime dan mengatur sebagai index
    df['tanggal'] = pd.to_datetime(df['tanggal'])
    df.set_index('tanggal', inplace=True)

    # Memisahkan data berdasarkan hari Senin, Rabu, dan Jumat
    senin_data = df[df['hari_label'] == 'Senin']
    rabu_data = df[df['hari_label'] == 'Rabu']
    jumat_data = df[df['hari_label'] == 'Jumat']


    # Membuat prediksi untuk hari Senin, Rabu, dan Jumat
    forecast_day(senin_data, 'Senin')
    forecast_day(rabu_data, 'Rabu')
    forecast_day(jumat_data, 'Jumat')
