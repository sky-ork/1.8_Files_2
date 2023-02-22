class CookBook:
    """"""
    def __init__(self, recipes: str):
        self.cook_book_dict = {}
        self.recipes = recipes
        self.get_all_recipes_in_book()

    def get_all_recipes_in_book(self):
        with open(self.recipes, encoding='UTF-8') as f:
            while True:
                ingr_list = []
                dish_name = f.readline().strip()
                if not dish_name:
                    break
                count_ingr = int(f.readline())
                for _ in range(count_ingr):
                    ingr_dict = {}
                    splited_ingr = f.readline().strip().split(' | ')
                    ingr_dict['ingredient_name'] = splited_ingr[0]
                    ingr_dict['quantity'] = int(splited_ingr[1])
                    ingr_dict['measure'] = splited_ingr[2]
                    ingr_list.append(ingr_dict)
                f.readline()
                self.cook_book_dict[dish_name] = ingr_list

    def get_shop_list_by_dishes(self, dishes: list, person_count=1):
        name_and_count_ingr = {}
        for dish in dishes:
            if not dish in self.cook_book_dict:
                return str(f'Блюдо {dish} в кулинарной книге отсутствует!')
            for item in self.cook_book_dict[dish]:
                key = item['ingredient_name']
                if key in name_and_count_ingr:
                    count_ingr = {'measure': item['measure'],
                                  'quantity': name_and_count_ingr[key]['quantity'] + item['quantity'] * person_count}
                    name_and_count_ingr[key] = count_ingr
                else:
                    count_ingr = {'measure': item['measure'], 'quantity': item['quantity'] * person_count}
                    name_and_count_ingr[key] = count_ingr
        return name_and_count_ingr


def main():
    cb1 = CookBook('recipes.txt')
    print(cb1.cook_book_dict)
    print(cb1.get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))


if __name__ == "__main__":
    main()
