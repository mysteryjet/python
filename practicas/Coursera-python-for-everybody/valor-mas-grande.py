grande = None
print("Antes", grande)
for num in [9, 41, 12, 3, 74, 15]:
    if grande is None:
        grande = num
    elif num > grande:
        grande = num
    print(grande, num)
print("Después", grande)

#valor mas pequeño
peque = None
print("Antes", grande)
for num in [9, 41, 12, 3, 74, 15]:
    if peque is None:
        peque = num
    elif num < peque:
        peque = num
    print(peque, num)
print("Después", peque)