from . import Operasi

def read_console():
    data_file = Operasi.read()
    
    if not data_file:
        print("Tidak ada data untuk ditampilkan.")
        return
    
    # header kolom
    print("\n" + "=" * 100)
    print(f"{'No':<4} | {'Judul':<30} | {'Deskripsi':<40} | {'Diberikan ke':<15}")
    print("-" * 100)

    # data rows
    for index, data in enumerate(data_file):
        data_break = [d.strip() for d in data.split(",")]

        # cegah error kalau jumlah kolom tidak pas
        if len(data_break) < 5:
            continue

        pk        = data_break[0]
        date_at   = data_break[1]
        judul     = data_break[2]
        deskripsi = data_break[3]
        assign    = data_break[4]

        print(
            f"{str(index):<4} | "
            f"{judul[:30].ljust(30)} | "
            f"{deskripsi[:40].ljust(40)} | "
            f"{assign[:15].ljust(15)}"
        )

    print("=" * 100 + "\n")
