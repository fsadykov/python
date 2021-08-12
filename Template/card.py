from string import Template

def Main():
    card = []
    card.append(dict(item='Coke', price=8, qty=2))
    card.append(dict(item='Cake', price=12, qty=1))
    card.append(dict(item='Fish', price=32, qty=4))

    temp = Template("$qty x $item = $price")
    total = 0
    for data in card:
        print(temp.substitute(data))
        total += data['price']
    print("Total: "+str(total))

if __name__ == '__main__':
    Main()
