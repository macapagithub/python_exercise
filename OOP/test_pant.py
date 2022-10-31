def check_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12
    
    pants.change_price(10) == 10
    assert pants.price == 10 
    
    assert pants.discount(.1) == 9
    
    print('You made it to the end of the check. Nice job!')

check_results()


# Check display_sales() method

# pants_one = Pants('red', 35, 36, 15.12)
# pants_two = Pants('blue', 40, 38, 24.12)
# pants_three = Pants('tan', 28, 30, 8.12)

# salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

# salesperson.sell_pants(pants_one)    
# salesperson.sell_pants(pants_two)
# salesperson.sell_pants(pants_three)

# salesperson.display_sales()