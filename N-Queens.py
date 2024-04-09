import random

def tao_ca_nhan(N):
    return [random.randint(0, N-1) for _ in range(N)]

def tinh_fitness(ca_nhan):
    xung_dot = 0
    N = len(ca_nhan)
    for i in range(N):
        for j in range(i+1, N):
            if ca_nhan[i] == ca_nhan[j] or abs(ca_nhan[i] - ca_nhan[j]) == abs(i - j):
                xung_dot += 1
    return xung_dot

def lai_gen(cha1, cha2):
    diem_lai = random.randint(1, len(cha1)-1)
    con1 = cha1[:diem_lai] + cha2[diem_lai:]
    con2 = cha2[:diem_lai] + cha1[diem_lai:]
    return con1, con2

def dot_bien(ca_nhan):
    index = random.randint(0, len(ca_nhan)-1)
    ca_nhan[index] = random.randint(0, len(ca_nhan)-1)
    return ca_nhan

def giai_thuat_di_truyen(N, kich_thuoc_quan_the, so_the_he):
    quan_the = [tao_ca_nhan(N) for _ in range(kich_thuoc_quan_the)]

    for the_he in range(so_the_he):
        quan_the = sorted(quan_the, key=lambda x: tinh_fitness(x))
        quan_the_moi = quan_the[:2]  # Chọn elitism: chỉ lấy hai cá thể tốt nhất

        while len(quan_the_moi) < kich_thuoc_quan_the:
            cha1, cha2 = random.choices(quan_the[:10], k=2)  # Chọn 2 cá thể từ quần thể hiện tại
            con1, con2 = lai_gen(cha1, cha2)
            con1 = dot_bien(con1)
            con2 = dot_bien(con2)
            quan_the_moi.extend([con1, con2])

        quan_the = quan_the_moi

    giai_phap_tot_nhat = quan_the[0]
    return giai_phap_tot_nhat

def in_giai_phap(giai_phap):
    N = len(giai_phap)
    for i in range(N):
        hang = ['.'] * N
        hang[giai_phap[i]] = 'H'
        print(' '.join(hang))

if __name__ == "__main__":
    N = int(input("Nhập kích thước bàn cờ N: "))  # Nhập kích thước bàn cờ từ người dùng
    kich_thuoc_quan_the = 20
    so_the_he = 1000
    giai_phap = giai_thuat_di_truyen(N, kich_thuoc_quan_the, so_the_he)
    print("Giải pháp:")
    in_giai_phap(giai_phap)
    