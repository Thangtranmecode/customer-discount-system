def tinh_tien(tong_mua, gia_tri_don_hang):
    tong_sau_mua = tong_mua + gia_tri_don_hang

    if tong_mua >= 50000000 or tong_sau_mua >= 50000000:
        giam_gia = gia_tri_don_hang * 0.10
        thanh_tien = gia_tri_don_hang - giam_gia
        la_khach_hang_than_thiet = True
    else:
        giam_gia = 0
        thanh_tien = gia_tri_don_hang
        la_khach_hang_than_thiet = False

    return la_khach_hang_than_thiet, giam_gia, thanh_tien


tong_mua = float(input("Nhap tong gia tri da mua trong nam: "))
gia_tri_don_hang = float(input("Nhap gia tri don hang moi: "))

kh_than_thiet, giam, thanh_tien = tinh_tien(
    tong_mua,
    gia_tri_don_hang
)
print("\nKET QUA")
print("Khach hang than thiet:", kh_than_thiet)
print("So tien giam:", format(giam, ",.0f"), "VND")
print("Thanh tien:", format(thanh_tien, ",.0f"), "VND")