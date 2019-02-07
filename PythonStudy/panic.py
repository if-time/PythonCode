phrase = "Don`t panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove('`')
print(plist)
plist.extend([plist.pop(), plist.pop()])
print(plist)
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
