import sqlite3

# 1. Veritabanı bağlantısı (dosya yoksa oluşturur)
conn = sqlite3.connect("ogrenciler.db")
cursor = conn.cursor()

# 2. Tablo oluşturma
cursor.execute("""
CREATE TABLE IF NOT EXISTS ogrenci (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isim TEXT NOT NULL,
    yas INTEGER,
    bolum TEXT
)
""")

# 3. Veri ekleme
cursor.execute("INSERT INTO ogrenci (isim, yas, bolum) VALUES (?, ?, ?)", ("Mithat", 24, "Yazılım"))
cursor.execute("INSERT INTO ogrenci (isim, yas, bolum) VALUES (?, ?, ?)", ("Zeynep", 22, "Bilgisayar"))
conn.commit()

# 4. Veri çekme
cursor.execute("SELECT * FROM ogrenci")
sonuclar = cursor.fetchall()
print("Veritabanındaki Öğrenciler:")
for satir in sonuclar:
    print(satir)

# 5. Veri güncelleme
cursor.execute("UPDATE ogrenci SET yas = ? WHERE isim = ?", (25, "Mithat"))
conn.commit()

# 6. Veri silme
cursor.execute("DELETE FROM ogrenci WHERE isim = ?", ("Zeynep",))
conn.commit()

# 7. Bağlantıyı kapat
conn.close()
