# ==========================================
# RENTAL MOBIL SPORT PREMIUM INDONESIA
# ==========================================

mobil = [
    "BMW M3 Competition 3000cc",
    "Mercedes-Benz C63 AMG 4000cc",
    "Audi RS5 Sportback 2900cc",
    "Lexus IS500 F Sport 5000cc",
    "Toyota GR Supra 3000cc",
    "BMW M5 Competition 4400cc",
    "Mercedes-Benz E63 AMG 4000cc",
    "Audi RS7 Sportback 4000cc",
    "Porsche Panamera GTS 4000cc",
    "Maserati Ghibli Trofeo 3800cc"
]

harga = [
    2500000,
    3500000,
    3000000,
    2800000,
    3200000,
    4500000,
    5000000,
    4800000,
    5500000,
    6000000
]

status = [True] * len(mobil)

riwayat = []
total_transaksi = 0
total_pendapatan = 0

while True:

    print("\n")
    print("=" * 85)
    print("           RENTAL MOBIL SPORT PREMIUM INDONESIA")
    print("=" * 85)
    print("[1] Lihat Daftar Mobil")
    print("[2] Sewa Mobil")
    print("[3] Kembalikan Mobil")
    print("[4] Cari Mobil")
    print("[5] Lihat Mobil Tersedia")
    print("[6] Lihat Mobil Disewa")
    print("[7] Riwayat Transaksi")
    print("[8] Statistik Rental")
    print("[9] Keluar")
    print("=" * 85)

    pilihan = input("Pilih Menu : ")

    # ==================================================
    # 1. DAFTAR MOBIL
    # ==================================================
    if pilihan == "1":

        print("\nDAFTAR MOBIL")
        print("-" * 110)
        print(f"{'No':<5}{'Mobil':<45}{'Harga/Hari':<20}{'Status'}")
        print("-" * 110)

        for i in range(len(mobil)):
            kondisi = "Tersedia" if status[i] else "Disewa"

            print(
                f"{i+1:<5}"
                f"{mobil[i]:<45}"
                f"Rp{harga[i]:<18,}"
                f"{kondisi}"
            )

        print("-" * 110)

    # ==================================================
    # 2. SEWA MOBIL
    # ==================================================
    elif pilihan == "2":

        nomor = int(input("Masukkan Nomor Mobil : ")) - 1

        if 0 <= nomor < len(mobil):

            if status[nomor]:

                nama = input("Nama Penyewa     : ")
                hari = int(input("Lama Sewa (Hari) : "))

                total = harga[nomor] * hari

                status[nomor] = False

                total_transaksi += 1
                total_pendapatan += total

                riwayat.append(
                    f"{nama} menyewa {mobil[nomor]} selama {hari} hari "
                    f"(Rp{total:,.0f})"
                )

                print("\n")
                print("=" * 55)
                print("              STRUK PENYEWAAN")
                print("=" * 55)
                print("Nama Penyewa :", nama)
                print("Mobil        :", mobil[nomor])
                print("Harga/Hari   : Rp{:,.0f}".format(harga[nomor]))
                print("Lama Sewa    :", hari, "Hari")
                print("Total Bayar  : Rp{:,.0f}".format(total))
                print("=" * 55)

            else:
                print("Mobil sedang disewa!")

        else:
            print("Nomor mobil tidak valid!")

    # ==================================================
    # 3. KEMBALIKAN MOBIL
    # ==================================================
    elif pilihan == "3":

        nomor = int(input("Masukkan Nomor Mobil : ")) - 1

        if 0 <= nomor < len(mobil):

            if not status[nomor]:
                status[nomor] = True
                print("Mobil berhasil dikembalikan.")
            else:
                print("Mobil tidak sedang disewa.")

        else:
            print("Nomor mobil tidak valid!")

    # ==================================================
    # 4. CARI MOBIL
    # ==================================================
    elif pilihan == "4":

        keyword = input("Masukkan Nama Mobil : ").lower()

        ditemukan = False

        for i in range(len(mobil)):

            if keyword in mobil[i].lower():

                ditemukan = True

                kondisi = "Tersedia" if status[i] else "Disewa"

                print("\nHasil Pencarian")
                print("-" * 50)
                print("Mobil  :", mobil[i])
                print("Harga  : Rp{:,.0f}".format(harga[i]))
                print("Status :", kondisi)

        if not ditemukan:
            print("Mobil tidak ditemukan.")

    # ==================================================
    # 5. MOBIL TERSEDIA
    # ==================================================
    elif pilihan == "5":

        print("\nMOBIL TERSEDIA")
        print("-" * 50)

        ada = False

        for i in range(len(mobil)):

            if status[i]:
                ada = True
                print(f"{i+1}. {mobil[i]}")

        if not ada:
            print("Tidak ada mobil yang tersedia.")

    # ==================================================
    # 6. MOBIL DISEWA
    # ==================================================
    elif pilihan == "6":

        print("\nMOBIL YANG SEDANG DISEWA")
        print("-" * 50)

        ada = False

        for i in range(len(mobil)):

            if not status[i]:
                ada = True
                print(f"{i+1}. {mobil[i]}")

        if not ada:
            print("Tidak ada mobil yang sedang disewa.")

    # ==================================================
    # 7. RIWAYAT TRANSAKSI
    # ==================================================
    elif pilihan == "7":

        print("\nRIWAYAT TRANSAKSI")
        print("-" * 70)

        if len(riwayat) == 0:
            print("Belum ada transaksi.")

        else:
            for i in range(len(riwayat)):
                print(f"{i+1}. {riwayat[i]}")

    # ==================================================
    # 8. STATISTIK RENTAL
    # ==================================================
    elif pilihan == "8":

        tersedia = 0
        disewa = 0

        for s in status:

            if s:
                tersedia += 1
            else:
                disewa += 1

        print("\nSTATISTIK RENTAL")
        print("=" * 50)
        print("Total Mobil       :", len(mobil))
        print("Mobil Tersedia    :", tersedia)
        print("Mobil Disewa      :", disewa)
        print("Total Transaksi   :", total_transaksi)
        print("Total Pendapatan  : Rp{:,.0f}".format(total_pendapatan))
        print("=" * 50)

    # ==================================================
    # 9. KELUAR
    # ==================================================
    elif pilihan == "9":

        print("\nTerima kasih telah menggunakan")
        print("RENTAL MOBIL SPORT PREMIUM INDONESIA")
        break

    else:
        print("Menu tidak tersedia!")