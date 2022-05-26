#讀取檔案
products =[]
with open('products.csv','r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name,price= line.strip().split(',')
		products.append([name,price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name =='q':
		break
	price= input('請輸入商品價格:')	
	p = [name,price]
	products.append(p)
print(products)

#印出所有購買紀錄
for p in products:
	print(p)
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8' )as f:#存成csv
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' +p[1] +'\n')

#字串可以相加相乘
'abc' + '123' == 'abc123'
'abc' * 2 == 'abcabc'

#products[0][0]#等於products裡的地0格的第0格[(n,p),(n,p)]等於第一個小括號裡的第一個
