import psycopg2

# PostgreSQL veritabanına bağlan
conn = psycopg2.connect(
    host="localhost",
    database="okul",
    user="postgres",
    password="sifre123"
)
cur = conn.cursor()

# Tablo oluştur
cur.execute("""
CREATE TABLE IF NOT EXISTS dersler (
    id SERIAL PRIMARY KEY,
    ad VARCHAR(50),
    kredi INTEGER
)
""")

# Veri ekle
cur.execute("INSERT INTO dersler (ad, kredi) VALUES (%s, %s)", ("Veritabanları", 4))
conn.commit()

# Veri sorgula
cur.execute("SELECT * FROM dersler")
dersler = cur.fetchall()
print("Dersler:")
for d in dersler:
    print(d)

# Güncelle
cur.execute("UPDATE dersler SET kredi = %s WHERE ad = %s", (5, "Veritabanları"))
conn.commit()

# Sil
cur.execute("DELETE FROM dersler WHERE kredi < %s", (3,))
conn.commit()

# Bağlantıyı kapat
cur.close()
conn.close()
