# Logic for BJSS Pair Programming Exercise "Land and Buildings Transaction Tax "

def calculate_lbtt(value):
    lbtt_cost = 0
    if 0 < value < 145000:
        lbtt_cost = 0
    elif 145000 < value <= 250000:
        lbtt_cost = value * 0.02
    elif 250000 < value <= 325000:
        lbtt_cost = value * 0.05
    elif 325000 < value <= 750000:
        lbtt_cost = value * 0.1
    elif 750000 < value:
        lbtt_cost = value * 0.12
    else: raise ValueError
    return round(lbtt_cost, 2)


def interface():
    try:
        price_of_property = round(float(input("\nPlease enter property value to calculate LBTT: £")), 2)
        lbtt = calculate_lbtt(price_of_property)
        print(f"The price of the property is £{price_of_property}")
        print(f"The value of LBTT to be paid is £{lbtt}")
        interface()
    except ValueError:
        print("Please enter a numerical input that is greater than 0.")
        interface()


if __name__ == "__main__":
    interface()
