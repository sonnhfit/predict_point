from .models import ChuongTrinhDaoTao, Diem, KeHoachHocTapPerson, HocPhan
import pickle
from django.conf import settings



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

def predict_score(user_id):
    with open(settings.BASE_DIR + '/student/objs.pkl', 'rb') as f:
        try:
            rs = pickle.load(f)
            data = rs.pred_for_user(user_id)
        except:
            pass

    diem = Diem.objects.filter(sinhvien_id=user_id).first()
    data = diem.diem


    return convert_diem_so_thanh_diem_chu(data)




def get_diem_from_user_and_mhp(user, mahp):
    try:
        diem = Diem.objects.get(sinhvien=user, hocphan=mahp)
        return convert_diem_so_thanh_diem_chu(diem.diem)
    except:
        return '_'
