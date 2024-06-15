import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

if __name__ == '__main__':
    # 1. Membaca data dari file Excel
    file_path = 'rekam_medik_perhari_dengan_nama.xls'  # Ganti dengan lokasi file Excel yang sesuai
    df = pd.read_excel(file_path)

    # Mengubah kolom 'tanggal' menjadi tipe data datetime dan mengatur sebagai index
    df['tanggal'] = pd.to_datetime(df['tanggal'])
    df.set_index('tanggal', inplace=True)

    # 2. Visualisasi data asli (Scatter Plot)
    plt.figure(figsize=(12, 6))
    plt.scatter(df.index, df['jumlah_data'], label='Actual')
    plt.plot(df.index, df['jumlah_data'], color='gray', alpha=0.5)  # Add a faint line for reference
    plt.title('Data Asli (Scatter Plot)')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Data')
    plt.legend()
    plt.show()

    # 3. Menerapkan model ARIMA
    model = ARIMA(df['jumlah_data'], order=(1, 1, 1))
    model_fit = model.fit()

    # 4. Melakukan prediksi untuk beberapa periode ke depan
    forecast = model_fit.forecast(steps=5)  # Prediksi 5 periode ke depan

    # 5. Memvisualisasikan hasil prediksi (Scatter Plot)
    plt.figure(figsize=(12, 6))
    plt.scatter(df.index, df['jumlah_data'], label='Actual')
    plt.plot(df.index, df['jumlah_data'], color='gray', alpha=0.5)  # Add a faint line for reference
    plt.plot(pd.date_range(start=df.index[-1], periods=5, freq='D'), forecast, label='Forecast', color='red')  # Plot forecast
    plt.title('ARIMA Forecast (Scatter Plot)')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Data')
    plt.legend()
    plt.show()

    # 6. Analisis hari kemungkinan pengunjung membeludak
    mean_visits_per_day = df.groupby('hari_label')['jumlah_data'].mean()
    print("mean_visits_per_day", mean_visits_per_day)
    threshold = mean_visits_per_day.mean() + mean_visits_per_day.std()  # Menentukan ambang batas, misalnya, satu standar deviasi dari rata-rata
    peak_days = mean_visits_per_day[mean_visits_per_day > threshold].index.tolist()

    print("threshold", threshold)
    print("peak day", peak_days)
    # Menampilkan insight tentang hari-hari tersebut
    if peak_days:
        print("Berdasarkan data historis, pengunjung kemungkinan akan membeludak pada hari-hari berikut:")
        for day in peak_days:
            print(day)
    else:
        print("Berdasarkan data historis, tidak ada hari di mana pengunjung kemungkinan akan membeludak.")
