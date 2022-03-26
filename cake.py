


def get_recipe_price(prices,optional=[],**ingredients):
    """
    the function calculate the price of cake products
    :param prices: dictionary of products prices for 100 gr
    :param optional: list of products that should be ignored
    :param ingredients: the products and the amounts to the cake
    :return:
    """
    total_price=[prices[product]*ingredients[product] for product in ingredients if product not in optional]
    # go over the product and calculate the price of each one
    return sum(total_price)


# print(get_recipe_price(prices={'c':5,'a':3,'b':8,'d':9},c=10,a=1,b=2,d=1,optional=['a']))
