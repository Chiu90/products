import os #operating system

#讀取檔案
def read_file(filename ):
    products =[]
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price= line.strip().split(',')
            products.append([name, price])
    return products           


#讓使用者輸入
def input_file(products):
    while True:
        name = input('請輸入商品名稱:')
        if name =='q':
            break
        price = input('請輸入商品價格:')	
        price = int(price) 
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_file(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8' )as f:#存成csv
        f.write('商品,價格\n')
        for p in products:
            f.write(str(p[0]) + ',' +str(p[1]) +'\n')


#檢查檔案室否在
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查products.csv在裡面嗎
        print('yeah')   
        products = read_file(filename) 
    else:
        print('can not found the file') 
    
    products = input_file(products)
    print_file(products)
    write_file('products.csv', products)

main()



#字串可以相加相乘
'abc' + '123' == 'abc123'
'abc' * 2 == 'abcabc'

#products[0][0]#等於products裡的地0格的第0格[(n,p),(n,p)]等於第一個小括號裡的第一個
