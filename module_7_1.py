class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'test.txt'
        self.__products = None

    def get_products(self):
        if self.__products is None:
            print('Что бы получить список продуктов для начала добавьте их')
            return 'Is Empty'
        else:
            str_products = ''
            for i in self.__products:
                str_products = str_products + f'{i.name}, {i.weight}, {i.category}\n'
            return str_products


    def add(self, *products):
        self.__products = products
        with open(self.__file_name, 'r+', encoding='utf-8') as file:
            is_product = False
            words_in_file = file.read()
            words_in_file = words_in_file.split()
            for i in products:
                for j in words_in_file:
                    if j == i.name:
                        is_product = True
                        break
                    else:
                        is_product = False

                if is_product:
                    print(f'Продукт {i.name} уже есть в магазине')
                else:
                    file.seek(0, 2)
                    file.write(i.name + ' ')
                is_product = False




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

