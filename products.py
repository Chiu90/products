products = []
while True:
	name = input('請輸入商品名稱:')
	if name =='q':
		break
	price= input('請輸入商品價格:')	
	p = []
	p.append(name)
	p.append(price)#上面三行等於p = [name,price]
	products.append(p)
print(products)

products[0][0]#等於products裡的地0格的第0格[(n,p),(n,p)]等於第一個小括號裡的第一個

for p in products:
	print(p)
	print(p[0], '的價格是', p[1])