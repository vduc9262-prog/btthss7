
choice = 0
raw_input = 'nGuyen vaN aN ; 2004'
while choice != 4:
    print()
    choice = input("""===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
    1. Hiển thị chuỗi dữ liệu gốc
    2. Chuẩn hóa Họ tên và tính Tuổi
    3. Tạo Mã ID và Email tự động
    4. Thoát chương trình
    =====================================
    Nhập lựa chọn của bạn (1-4):""")
    print()
        
    data_revert = raw_input.strip().split(";")
   
    full_name = data_revert[0].strip().title()
    birth_date = data_revert[1].strip()
    age = 2026 - int(birth_date)

        
    if choice == "1":
            print('chuỗi dữ liệu hiện tại :')
            print(raw_input)
    elif choice == "2":
            

            print("KET QUA CHUAN HOA DU LIEU: ")
            print("ho va ten: ", full_name)
            print("nam sinh: ", birth_date)
            print("tuổi: ", age)
    elif choice == "3":
            handle_str = full_name.split()
            first_name= handle_str[0]
            middle_name = handle_str[1]
            last_name = handle_str[2]
            
            email = first_name[0:1].lower() + middle_name[0].lower() + last_name.lower() + "@company.com"

            Code = last_name.upper() + birth_date[2:]
            
            print("THE THANH VIEN MOI")
            print("Ho va ten: ", full_name)
            print(f"Ma ID: {Code}")
            print(f"Email: {email}")
        
    elif choice == "4":
        print('thoats chuongw trinhf ')
        break
    else:
        print('luaw chonj ko hop le ! ')

