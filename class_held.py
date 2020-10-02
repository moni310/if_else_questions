class_held=int(input("enter the held"))
class_attende=int(input("enter the attende"))
attendence_pracentage=class_attende/class_held*100
if attendence_pracentage>=75:
    print("allow in this exam")
else:
    print("not allow")