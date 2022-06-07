row1 = ['_','_','_']
row2 = ['_','_','_']
row3 = ['_','_','_']
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

pos =input("Where you want to place the tressure ? First column then row --- ")
horizontal = int(pos[0])
vertical = int(pos[1])

# selected_row = map[vertical-1]
# selected_row[horizontal-1] = 'X'
map[vertical-1][horizontal-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")



