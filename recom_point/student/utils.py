def convert_diem_so_thanh_diem_chu(diem):
    if diem >= 8.5:
        return 'A'
    if diem >= 8.0:
        return 'B+'
    if diem >= 7.0:
        return 'B'
    if diem >= 6.5:
        return 'C+'
    if diem >= 5.5:
        return 'C'
    if diem >= 5.0:
        return 'D'
    if diem < 5:
        return 'F'