driving = input("你有沒有開車: ")
age = input("你的年齡: ")
age = int(age)

if driving == "有":
	if age >= 18:
		print("你通過測驗了")
	else:
		print("你在這幹嗎")
if driving == "沒有":
	if age >= 18:
		print("你還在這幹嗎")
	else:
		print("過幾年再去考吧")
else:
	print("只能輸入有或沒有")