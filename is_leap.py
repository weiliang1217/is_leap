print(4 / 2) # 運算結果自動float 1位數
print(int(4/2)) # 運算結果顯示integer整數
print(4 % 2) # 4/2 = 2 無餘數 answer = 0

def is_leap(year):
	if year % 4 != 0:
	 return False
	if year % 4 == 0 and year % 100 != 0:
		return True
	if year % 100 == 0 and year % 400 != 0:
		return False
	if year % 400 == 0 and year % 3200 != 0:
		return True
print(is_leap(2024))		
	 
