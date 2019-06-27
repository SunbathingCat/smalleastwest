items = []
Tile = 'Furnaces'#Altar
price = 20

f = open('CopyMachChange.txt')
str = f.readlines()
for tem in str:
    s = tem.replace('\n','')
    a = s.split(' ')
    name = a[0]
    if len(a)==2:
        price = int(a[1])
    l = [name, price]
    items.append(l)
f.close()

f = open('CopyMachData.txt', 'a+')
for index, item in enumerate(items):
    f.write('ModRecipe CR%d_%s = new ModRecipe(this);\n'%(index, item[0]))
    f.write('CR%d_%s.AddIngredient(ItemID.%s, 1);\n'%(index, item[0], item[0]))
    f.write('CR%d_%s.AddIngredient(ItemID.GoldCoin, %d);\n' %(index, item[0], item[1]))

    f.write('CR%d_%s.AddTile(null, "%s");\n' % (index, item[0], Tile))
    # f.write('CR%d_%s.AddTile(TileID.%s);\n'%(index, item, Tile))

    f.write('CR%d_%s.SetResult(ItemID.%s, 2);\n'%(index, item[0], item[0]))
    f.write('CR%d_%s.AddRecipe();\n\n'%(index, item[0]))
f.close()