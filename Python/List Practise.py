#  1
colors = list(["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"])

#  2
pColors = colors[4:7]  
nColors = colors[-6:-3]  
myColors = pColors + nColors

#  3
middle_index = len(colors) // 2
for i in range(len(colors)):
    if i == middle_index:
        print(f"{i} is the middle element: {colors[i]}")
    else:
        print(f"{i} is not in the mid place")


#  4
colors.append("magenta")
colors.append("lime")

#  5
removed_color = colors[3]
colors = colors[:3] + colors[4:]

#  6
eColors = colors[::-2]
print(eColors)
#  7
colors.insert(6, "aqua")
print(colors)
#  8
print(colors[5:-6])

#  9
print(colors[-5:-2])

#  10
del eColors