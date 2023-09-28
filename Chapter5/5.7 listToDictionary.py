def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():      #k = key, v = value
        print(str(v) + ' ' + k)
        item_total += v
    print('Total Items: ' + str(item_total))

def add_to_inventory(inventory, added_items):
    for loot in dragon_loot:
        if loot not in inv:
            inv[loot] = 1
        else:
            inv[loot] += 1

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inv, dragon_loot)
display_inventory(inv)
