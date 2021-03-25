#agar bisa mendaftar kursus online siswa diharuskan beruumur minimal 21 tahun dan sudah lulus ujian kualifikasi

print("uji kesesuaian pendaftar kursus online")
#usia
usia=int(input("berapa usia kamu?"))
print(usia>=21)
#kelulusan ujian
lulus=str(input("apakah kamu sudah lulus ujian kualifikasi?(lulus/belum)"))


if usia>=21 and lulus=="lulus":
    print("Anda dapat mendaftar di kursus")


else:
    print("Anda tidak dapat mendaftar di kursus")







