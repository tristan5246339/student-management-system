# 学生信息字典初始化
students = []


# 函数：添加学生信息
def add_student():
    name = input("请输入学生姓名：")
    dormitory = input("请输入宿舍号+床位号（如313-3）：")
    className = input("请输入班级：")
    status = input("请输入入住情况（在校/请假）：")
    student = {
        'name': name,
        'dormitory': dormitory,
        'class': className,
        'status': status
    }
    students.append(student)
    print("已成功添加学生信息！")


# 函数：删除学生信息
def delete_student():
    name = input("请输入要删除的学生姓名：")
    found = False
    for student in students:
        if student['name'] == name:
            students.remove(student)
            found = True
            print("已成功删除学生信息！")
            break
    if not found:
        print("系统不存在该学生的信息。")


# 函数：修改学生信息
def modify_student():
    name = input("请输入要修改的学生姓名：")
    found = False
    for student in students:
        if student['name'] == name:
            student['dormitory'] = input("请输入新的宿舍号+床位号：")
            student['class'] = input("请输入新的班级：")
            student['status'] = input("请输入新的入住情况（在校/请假）：")
            found = True
            print("已成功修改学生信息！")
            break
    if not found:
        print("系统不存在该学生的信息。")


# 函数：查询学生信息
def query_student():
    name = input("请输入要查询的学生姓名：")
    found = False
    for student in students:
        if student['name'] == name:
            print("学生姓名：", student['name'])
            print("宿舍号+床位号：", student['dormitory'])
            print("班级：", student['class'])
            print("入住情况：", student['status'])
            found = True
            break
    if not found:
        print("系统不存在该学生的信息。")


# 函数：显示所有学生信息
def show_all_students():
    print("所有学生的住宿信息：")
    for student in students:
        print("学生姓名：", student['name'])
        print("宿舍号+床位号：", student['dormitory'])
        print("班级：", student['class'])
        print("入住情况：", student['status'])
        print("-----------------------")


# 函数：显示请假学生信息
def show_leave_students():
    print("请假学生的住宿信息：")
    for student in students:
        if student['status'] == '请假':
            print("学生姓名：", student['name'])
            print("宿舍号+床位号：", student['dormitory'])
            print("班级：", student['class'])
            print("入住情况：", student['status'])
            print("-----------------------")


# 主函数：宿舍管理系统操作指引
def main():
    while True:
        print("欢迎使用宿舍管理系统")
        print("1. 添加学生信息")
        print("2. 删除学生信息")
        print("3. 修改学生信息")
        print("4. 查询学生信息")
        print("5. 显示所有学生信息")
        print("6. 显示请假学生信息")
        print("7. 退出系统")
        choice = input("请输入操作编号(1-7)：")

        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            modify_student()
        elif choice == '4':
            query_student()
        elif choice == '5':
            show_all_students()
        elif choice == '6':
            show_leave_students()
        elif choice == '7':
            print("感谢使用宿舍管理系统，再见！")
            break
        else:
            print("无效的操作编号，请重新输入。")


# 调用主函数开始运行宿舍管理系统
fp=open("students.txt",mode="r",encoding="utf-8")
for i in fp:
    j=i.split(",")
    students.append({
        'name': j[0],
        'dormitory': j[1],
        'class': j[2],
        'status': j[3][:-1]
    })
fp.close()
main()
fp=open("students.txt",mode="w",encoding="utf-8")
for i in students:
    j=i["name"]+","+i["dormitory"]+","+i["class"]+","+i["status"]+"\n"
    fp.write(j)
fp.close()
