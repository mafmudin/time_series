import mysql.connector


# Fungsi untuk membuat koneksi ke database MySQL atau MariaDB
def create_connection():
    try:
        # Konfigurasi koneksi ke database MySQL atau MariaDB
        connection = mysql.connector.connect(
            host='mysql',  # Nama layanan MySQL dalam Docker Compose
            port=3306,  # Port default untuk MySQL atau MariaDB
            user='root',
            password='',
            database='sarjito'  # Nama database yang ingin Anda gunakan
        )
        print("Koneksi ke database berhasil!")
        return connection
    except mysql.connector.Error as error:
        print("Error saat membuat koneksi ke database:", error)
        return None


# Contoh penggunaan fungsi create_connection
if __name__ == "__main__":
    # Membuat koneksi
    connection = create_connection()
    if connection:
        # Melakukan query atau operasi database lainnya
        # ...

        # Menutup koneksi
        connection.close()
        print("Koneksi ditutup.")
