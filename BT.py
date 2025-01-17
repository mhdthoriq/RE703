import py_trees
import time

# Definisi Aksi
class HindariRintangan(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(HindariRintangan, self).__init__(name)

    def update(self):
        print("[Aksi] Menghindari rintangan...")
        # Simulasi menghindari rintangan
        time.sleep(1)  # Simulasi waktu proses
        return py_trees.common.Status.SUCCESS

class MenujuTujuan(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(MenujuTujuan, self).__init__(name)

    def update(self):
        print("[Aksi] Menuju tujuan...")
        # Simulasi menuju tujuan
        time.sleep(1)  # Simulasi waktu proses
        return py_trees.common.Status.SUCCESS

class IsiUlang(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(IsiUlang, self).__init__(name)

    def update(self):
        print("[Aksi] Mengisi ulang baterai...")
        # Simulasi pengisian ulang
        time.sleep(1)  # Simulasi waktu proses
        return py_trees.common.Status.SUCCESS

# Definisi Kondisi
class ApakahAdaRintangan(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(ApakahAdaRintangan, self).__init__(name)

    def update(self):
        print("[Kondisi] Memeriksa rintangan...")
        # Simulasi deteksi rintangan
        time.sleep(0.5)  # Simulasi waktu proses
        ada_rintangan = True  # Ubah ke False untuk simulasi tanpa rintangan
        return py_trees.common.Status.SUCCESS if ada_rintangan else py_trees.common.Status.FAILURE

class ApakahBateraiLemah(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(ApakahBateraiLemah, self).__init__(name)

    def update(self):
        print("[Kondisi] Memeriksa level baterai...")
        # Simulasi status baterai
        time.sleep(0.5)  # Simulasi waktu proses
        baterai_lemah = False  # Ubah ke True untuk simulasi baterai lemah
        return py_trees.common.Status.SUCCESS if baterai_lemah else py_trees.common.Status.FAILURE

# Membangun Pohon Perilaku
def buat_pohon_perilaku():
    root = py_trees.composites.Selector("Akar", memory=False)

    # Urutan pengisian ulang
    urutan_isi_ulang = py_trees.composites.Sequence("Urutan Isi Ulang", memory=False)
    urutan_isi_ulang.add_child(ApakahBateraiLemah("Baterai Lemah?"))
    urutan_isi_ulang.add_child(IsiUlang("Isi Ulang"))

    # Urutan menghindari rintangan
    urutan_hindari_rintangan = py_trees.composites.Sequence("Urutan Hindari Rintangan", memory=False)
    urutan_hindari_rintangan.add_child(ApakahAdaRintangan("Ada Rintangan?"))
    urutan_hindari_rintangan.add_child(HindariRintangan("Hindari Rintangan"))

    # Urutan tujuan utama
    menuju_tujuan = MenujuTujuan("Menuju Tujuan")

    # Menambahkan urutan ke akar
    root.add_child(urutan_isi_ulang)
    root.add_child(urutan_hindari_rintangan)
    root.add_child(menuju_tujuan)

    return root

# Eksekusi Utama
if __name__ == "__main__":
    pohon_perilaku = buat_pohon_perilaku()
    print(py_trees.display.ascii_tree(pohon_perilaku))

    # Tick pohon
    for i in range(3):
        print(f"\nTick {i + 1}")
        pohon_perilaku.tick_once()
        time.sleep(2)  # Memberikan jeda antara tiap tick
