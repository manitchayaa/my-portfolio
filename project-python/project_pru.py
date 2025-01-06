from datetime import datetime
import random
tea={"ชาไทย" : 19, "ชาเขียว" : 19, "ชานมไต้หวัน" : 19, "ชาดำเย็น" : 19, "ชามะนาว" : 19}
coffee={"กาแฟโบราณ" : 24, "คาปูชิโน" : 34, "อเมริกาโน" : 34, "เอสเปรสโซ" : 34, "โกโก้" :24}
smootie={"สตอเบอรี่" : 34, "แอปเปิ้ลเขียว" : 34, "กีวี่" : 34, "ส้มยูซุ" : 34, "ลิ้นจี่" : 34}
cake={"เค้กส้ม" :40, "เค้กมะพร้าวอ่อน" : 40, "เอแคลร์" : 35, "บราวนี่" : 35}
food={"สปาเก็ตตี้คาโบนาร่า" : 55, "สปาเก็ตตี้ผัดขี้เมา" : 55, "ซุปเห็ด" : 45, "ซุปข้าวโพด" : 45, "ข้าวผัดอเมริกัน" : 55}

# dict
add_dict = {}

#list
tea_list=list(tea)
coffee_list=list(coffee)
smootie_list=list(smootie)
cake_list=list(cake)
food_list=list(food)
sweet=["ไม่หวานเลย","หวานน้อย","หวานปกติ","หวานมาก"]
sweet_addlist = []
game_list = []


# menu หลัก
def menu() :
    print("\n[เมนูหลัก]")
    print("1.สั่งเครื่องดื่ม")
    print("2.สั่งขนมเค้ก/ของทานเล่น")
    print("3.สั่งอาหารจานเดียว")
    print("4.เล่นเกมเพื่อรับคูปองส่วนลด")
    print("0.ออกจากโปรแกรม")

# menu ชา
def type_drink(code):
    while True :
        try :
            while True :
                print("\n[สั่งเครื่องดื่ม]")
                print("1.ชา")
                print("2.กาแฟ/โกโก้")
                print("3.สมูทตี้")
                print("4.กลับเมนูหลัก")
                print("0.ออกจากโปรแกรม")
                select=int(input("✿ กรุณาเลือกเครื่องดื่ม :"))
                if select == 1 :
                    menu_tea(code)
                    return
                elif select == 2 :
                    coffee_menu(code)
                    return
                elif select == 3 :
                    smootie_menu(code)
                    return
                elif select == 4 :
                    return 
                elif select == 0 :
                    while True :
                        n=input("\n✿ คุณต้องการยืนยันการออกหรือไม่ (Y/N) :").lower()
                        if n == 'y' :
                            farewell()
                            return 0
                        elif n == 'n' :
                            return 
                        else :
                            print("********** กรุณากรอก (y/n) เท่านั้ัน **********")
                else :
                    print("\n-----------------ไม่พบข้อมูล ----------------- ")
                    print("----------------- กรุณากรอกใหม่ -----------------")
        except ValueError :
            print("\n----------- กรุณากรอกตัวเลข(0-4) เท่านั้น -----------")

# ระดับความหวาน
def sweet_level():
    print("\n[ระดับความหวาน]")
    print("1.ไม่หวานเลย")
    print("2.หวานน้อย")
    print("3.หวานปกติ")
    print("4.หวานมาก")

# ชา
def menu_tea(code):
    while True:
        try :
            x=True
            while x :
                print("\n[ชา]")
                i=1
                for name in tea :
                    print(f"{i}.{name} {tea[name]} บาท")
                    i +=1
                choose_tea = int(input("✿ กรุณาเลือกเครื่องดื่มชาที่ต้องการ :"))-1
                if choose_tea > -1 :
                    x=False
                else :
                    print("\n----- ไม่มีในรายการ กรุณาเลือกสั่งชาใหม่ -----")
            tea_in=tea_list[choose_tea]
            cost=tea.get(tea_in)
            add_dict[tea_in] = cost
            while True :
                try :
                    q=True
                    while q:
                        sweet_level()
                        level=int(input("✿ กรุณาเลือกระดับความหวาน (1-4) :"))-1
                        if level > -1 :
                            q=False
                        else :
                            print("\n---- ไม่มีในรายการ กรุณากรอกระดับความหวานใหม่ ----")
                    sweet_print = sweet[level]
                    sweet_addlist.append(sweet_print)
                    print("\n---------------- สรุปรายการ ----------------")
                    a = 0 
                    for k,v in add_dict.items() :
                        a+=1
                        print(f"{a}.{k}{sweet_addlist[a-1]} ราคา {v} บาท")
                    print("--------------------------------------------")
                    print("**** หากซื้อครบ 100 บาทได้รับส่วนลด 10 บาท ****")
                    while True :
                        con = input("\n✿ คุณต้องการทำรายการต่อหรือไม่ (Y/N) : ").lower()
                        if con == "y" :
                            return
                        elif con == "n" : 
                            bill(code)  
                            farewell()
                            add_dict.clear()
                            sweet_addlist.clear()
                            return 0
                        else :
                            print("****** กรุณากรอก (y/n) เท่านั้น *******") 
                except ValueError :
                    print("\n----------- กรุณากรอกตัวเลข(1-4) เท่านั้น ----------- ")
                except IndexError :
                    print("\n----------------- ไม่พบข้อมูล ----------------- ")
                    print("----------------- กรุณากรอกใหม่ ----------------")        
        except ValueError :
            print("\n----------- กรุณากรอกตัวเลข(1-5) เท่านั้น ----------- ")
        except IndexError :
            print("\n----------------- ไม่พบข้อมูล ----------------- ")
            print("----------------- กรุณากรอกใหม่ ----------------")

               
# กาแฟ
def coffee_menu(code) :
    while True :
        try :
            c=True
            while c:
                print("\n[กาแฟ/โกโก้]")
                i=1
                for name in coffee :
                    print(f"{i}.{name} {coffee[name]} บาท")
                    i +=1
                choose_coffee=int(input("✿ กรุณาเลือกกาแฟ/โกโก้ที่ต้องการ :"))-1
                if choose_coffee > -1 :
                    c = False
                else :
                    print("\n----- ไม่มีในรายการ กรุณาเลือกสั่งกาแฟใหม่ -----")
            coffee_in=coffee_list[choose_coffee]
            cost_coffee=coffee.get(coffee_in)
            add_dict[coffee_in] = cost_coffee
            while True :
                try :
                    j=True
                    while j:
                        sweet_level()
                        level=int(input("✿ กรุณาเลือกระดับความหวาน (1-4) :"))-1
                        if level > -1 :
                            j=False
                        else :
                            print("\n----- ไม่มีในรายการ กรุณาเลือกระดับความหวานใหม่ -----")
                    sweet_print = sweet[level]
                    sweet_addlist.append(sweet_print)
                    print("\n---------------- สรุปรายการ ----------------")
                    a = 0
                    for k,v in add_dict.items() :
                        a+=1
                        print(f"{a}.{k}{sweet_addlist[a-1]} ราคา {v} บาท")
                    print("--------------------------------------------")
                    print("**** หากซื้อครบ 100 บาทได้รับส่วนลด 10 บาท ****")
                    while True :
                        con = input("\n✿ คุณต้องการทำรายการต่อหรือไม่ (Y/N) :").lower()
                        if con == "y" :
                            return
                        elif con == "n" :
                            bill(code)
                            farewell()
                            add_dict.clear()
                            sweet_addlist.clear()
                            return 0
                        else :
                            print("****** กรุณากรอก (y/n) เท่านั้น *******")
                except ValueError :
                    print("\n----------- กรุณากรอกตัวเลข(1-4) เท่านั้น -----------")
                except IndexError :
                    print("\n----------------- ไม่พบข้อมูล ----------------- ")
                    print("----------------- กรุณากรอกใหม่ ----------------")
        except ValueError :
            print("\n----------- กรุณากรอกตัวเลข(1-5) เท่านั้น ----------- ")
        except IndexError :
            print("\n----------------- ไม่พบข้อมูล ----------------- ")
            print("----------------- กรุณากรอกใหม่ ----------------")

# สมูทตี้
def smootie_menu(code) :
    while True :
        try :
            m=True
            while m :
                print("\n[สมูทตี้]")
                i=1
                for name in smootie :
                    print(f"{i}.{name} {smootie[name]} บาท")
                    i +=1
                choose_smootie=int(input("✿ กรุณาเลือกสมูทตี้ที่ต้องการ :"))-1
                if choose_smootie > -1 :
                    m=False
                else :
                    print("\n-----ไม่มีในรายการ กรุณาเลือกสั่งสมูทตี้ใหม่ -----")
            smootie_in=smootie_list[choose_smootie]
            cost_smootie=smootie.get(smootie_in)
            add_dict[smootie_in] = cost_smootie
            q = ''
            sweet_addlist.append(q)
            print("\n--------------- สรุปรายการ ----------------")
            a = 0 
            for k,v in add_dict.items() :
                a+=1
                print(f"{a}.{k}{sweet_addlist[a-1]} ราคา {v} บาท")
            print("--------------------------------------------")
            print("**** หากซื้อครบ 100 บาทได้รับส่วนลด 10 บาท ****")
            while True :
                con = input("\n✿ คุณต้องการทำรายการต่อหรือไม่ (Y/N) :").lower()
                if con == "y" :
                    return
                elif con == "n" :
                    bill(code)
                    farewell()
                    add_dict.clear()
                    sweet_addlist.clear()
                    return 0
                else :
                    print("\n****** กรุณากรอก (y/n) เท่านั้น *******")
        except ValueError :
            print("\n----------- กรุณากรอกตัวเลข(1-5) เท่านั้น ----------- ")
        except IndexError :
            print("\n----------------- ไม่พบข้อมูล ----------------- ")
            print("----------------- กรุณากรอกใหม่ ----------------")

# menu ของทานเล่น
def cake_menu(code) :
    while True :
        try :
            k=True
            while k :
                print("\n[สั่งขนมเค้ก/ของทานเล่น]")
                i=1
                for name in cake :
                    print(f"{i}.{name} {cake[name]} บาท")
                    i +=1
                choose_cake=int(input("✿ กรุณาสั่งของทานเล่นที่ต้องการ :"))-1
                if choose_cake > -1 :
                    k=False
                else:
                    print("\n----- ไม่มีในรายการ กรุณาเลือกสั่งของทานเล่นใหม่ -----")
            cake_in=cake_list[choose_cake]
            cost_cake=cake.get(cake_in)
            add_dict[cake_in] = cost_cake
            q = ''
            sweet_addlist.append(q)
            print("\n---------------- สรุปรายการ ----------------")
            a = 0 
            for k,v in add_dict.items() :
                a+=1
                print(f"{a}.{k}{sweet_addlist[a-1]} ราคา {v} บาท")
            print("--------------------------------------------")
            print("**** หากซื้อครบ 100 บาทได้รับส่วนลด 10 บาท ****")
            while True :
                con = input("\n✿ คุณต้องการทำรายการต่อหรือไม่ (Y/N) :").lower()
                if con == "y" :
                    return
                elif con == "n" :
                    bill(code)
                    farewell()
                    add_dict.clear()
                    sweet_addlist.clear()
                    return 0
                else :
                    print("****** กรุณากรอก (y/n) เท่านั้น *******")
        except ValueError :
            print("\n----------- กรุณากรอกตัวเลข(1-4) เท่านั้น ----------- ")
        except IndexError :
            print("\n----------------- ไม่พบข้อมูล ----------------- ")
            print("----------------- กรุณากรอกใหม่ ----------------")

#menu อาหาร
def food_menu (code) :
    while True :
        try :
            t=True
            while t :
                print("\n[สั่งอาหารจานเดียว]")
                i=1
                for name in food :
                    print(f"{i}.{name} {food[name]} บาท")
                    i +=1
                choose_food=int(input("✿ กรุณาเลือกอาหารที่ต้องการ :"))-1
                if choose_food > -1 :
                    t=False
                else :
                    print("\n----- ไม่มีในรายการ กรุณาเลือกสั่งอาหารใหม่ -----")
            food_in=food_list[choose_food]
            cost_food=food.get(food_in)
            add_dict[food_in] = cost_food
            q = ''
            sweet_addlist.append(q)
            print("\n--------------- สรุปรายการ ----------------")
            a = 0 
            for k,v in add_dict.items() :
                a+=1
                print(f"{a}.{k}{sweet_addlist[a-1]} ราคา {v} บาท")
            print("--------------------------------------------")
            print("**** หากซื้อครบ 100 บาทได้รับส่วนลด 10 บาท ****")
            while True :
                con = input("\n---> คุณต้องการทำรายการต่อหรือไม่ (Y/N) :").lower()
                if con == "y" :
                    return
                elif con == "n" :
                    bill(code)
                    farewell()
                    add_dict.clear()
                    sweet_addlist.clear()
                    return 0
                else : 
                    print("****** กรุณากรอก (y/n) เท่านั้น *******")
        except ValueError :
            print("\n-------- กรุณากรอกตัวเลข(1-5) เท่านั้น ---------")
        except IndexError :
            print("\n----------------- ไม่พบข้อมูล ----------------- ")
            print("----------------- กรุณากรอกใหม่ ----------------")

# bill
def bill (code):
    print("\n------- สรุปยอดรายการสั่งซื้อทั้งหมด -------")
    a = 0 
    for k,v in add_dict.items() :
        a+=1
        print(f"{a}.{k}{sweet_addlist[a-1]} ราคา {v} บาท")
    print("-------------------------------------")
    sum = 0
    for v in add_dict.values() :
        sum+=v
    if sum>=100:
        print(f"ยอดชำระทั้งหมด : {sum} บาท ")
        print("-------------------------------------")
    elif sum<100 and code != 15:
        print("ราคาทั้งสิ้น :",sum,"บาท")
        print("-------------------------------------")
    if sum >= 100 and code == 15:
        print ("******** คุณได้รับส่วนลด 10 บาท *******")
        print("******** คุณได้รับส่วนลดจากคูปอง 15 บาท *******")
        dis = discount(sum)
        sum = dis - code
        print("-------------------------------------")
        print("ราคาทั้งสิ้น :",sum,"บาท")
    elif sum >= 100 and code != 15 :
        print ("******** คุณได้รับส่วนลด 10 บาท *******")
        dis = discount(sum)
        print("\nราคาทั้งสิ้น :",dis,"บาท")
        print("-------------------------------------")
    elif sum <100 and code == 15:
        sum -= code
        print("คุณได้รับส่วนลดคูปอง จากการเล่นเกมชนะ 15 บาท ")
        print("\nราคาทั้งสิ้น :",sum,"บาท")
        print("-------------------------------------")
    while True :
            yuenyan = input("\nยืนยันการชำระ (Y) :").lower()
            if yuenyan == 'y' :
                game_list.clear()
                return
            else :
                print("\n****** กรุณากรอก (y) เท่านั้น *******")

# ส่วนลด
def discount(sum) :
    if sum >= 100 :
        dis = sum-10
        return dis
    elif sum < 100 :
        return
#kupong
def kupong():
    print("\n[เดาตัวเลข]")
    ran_num = random.randint(1,10)
    a = 0
    while True :
        try :
            a += 1
            if a == 4 :
                break
            print(f"-- รอบที่ :{a} ")
            ans_num=int(input(f"เดาตัวเลข :"))
            if ran_num > ans_num :
                print (f"++ มากกว่า {ans_num} ++\n")
            elif ran_num < ans_num :
                print (f"-- น้อยกว่า {ans_num} --\n")
            else :
                print ("-----> ถูกต้อง!!!")
                break
        except ValueError :
            print("-----------------กำหนดข้อมูลเป็นตัวเลข -----------------\n")
            a -= 1
             
    if ans_num == ran_num:
        print("----- คุณชนะได้รับส่วนลด 15 บาท -----")
        game_list.append(15)
        return 15
    else:
        print("----- คุณไม่ได้รับส่วนลดคูปองจาการเล่นเกม -----")
        return 0
# end
def farewell() :
    print("\n-------------------------------------")
    print("🙏ขอบคุณที่ใช้บริการ ^_____^")
    print("-------------------------------------")

# main program
print("♥_PunchPraew cafe_♥")
print("ยินดีต้อนรับ")
myname= input("ชื่อ:")
print("")
now = datetime.today()
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print("-----------------------------------")
code = 0
while True :
    try :
        menu()
        work=int(input("✿ เลือกหัวข้อเพื่อทำงาน :"))
        if work == 1 :
            type_drink(code)
        elif work == 2 :
            cake_menu(code)
        elif work == 3 :
            food_menu(code)
        elif work == 4:
            if 15 not in game_list:
                code = kupong()
            else:
                print("\n----------- คุณได้ทำการเล่นไปแล้ว -----------")
        elif work == 0 :
            farewell()
            break
        else :
            print("\n-----------------ไม่พบข้อมูล ----------------- ")
            print("----------------- กรุณากรอกใหม่ ---------------")
    except ValueError :
        print("\n-----------กรุณากรอกตัวเลข(0-4) เท่านั้น ----------- ")