# amer_price=2000
# cafe_price=3000
# capu_price=3500

menu=int(input("1: 아메리카노, 2: 카페라떼, 3: 카푸치노=>원하는 메뉴 선택"))
if menu == 1:
    coun=americanos=int(input("아메리카노 판매 개수: "))
    price=2000

elif menu == 2:
    conu=cafelattes=int(input("카페라떼 판매 개수: "))
    price=3000

else:
    conu=capucinos=int(input("카푸치노 판매 개수: "))
    price=3500

# sales=americanos*amer_price
# sales=sales+cafelattes*cafe_price
sales=conu*price
print("총 매출은", sales, "입니다.")


