def main():
    fatg=float(input("Enter the number of fat grams consumed in a day:"))
    carbg=float(input("Enter the number of carbohydrate grams consumed in a day:"))
    caf=fat(fatg)
    cac=carbo(carbg)
    print(f'The number of calories that result from the fat are {caf:,.2f}')
    print(f'The number of calories that result from the carbohydrates are {cac:,.2f}')
def fat(fat_grams):
    calories_fat=fat_grams*9
    return calories_fat
def carbo(carb_grams):
    calories_carbs=carb_grams*4
    return calories_carbs
main()