guest_names = ['Elon Musk', 'Warren Buffett', 'Queen Elizabeth']
print("Hello, {}, please come to my dinner party".format(guest_names[0]))
print("Hello, {}, please come to my dinner party".format(guest_names[1]))
print("Hello, {}, please come to my dinner party".format(guest_names[2]))
print("Hello Santi, I can't make it, Sorry! - Queen Elizabeth")
guest_names = ['Elon Musk', 'Warren Buffett', 'Bryan Cranston']
print("Hello, {}, please come to my dinner party".format(guest_names[0]))
print("Hello, {}, please come to my dinner party".format(guest_names[1]))
print("Hello, {}, please come to my dinner party".format(guest_names[2]))
print("Hello, {}, we found a bigger dinner table!".format(guest_names[0]))
print("Hello, {}, we found a bigger dinner table!".format(guest_names[1]))
print("Hello, {}, we found a bigger dinner table!".format(guest_names[2]))
guest_names.insert(0, 'Tom Cruise')
guest_names.insert(3, 'Tyler the Creator')
guest_names.append('Drake')
print("Hello, {}, please come to my dinner party".format(guest_names[0]))
print("Hello, {}, please come to my dinner party".format(guest_names[1]))
print("Hello, {}, please come to my dinner party".format(guest_names[2]))
print("Hello, {}, please come to my dinner party".format(guest_names[3]))
print("Hello, {}, please come to my dinner party".format(guest_names[4]))
print("Hello, {}, please come to my dinner party".format(guest_names[5]))
print("Hello, {}, I can only invite two people, sorry!".format(guest_names[0]))
print("Hello, {}, I can only invite two people, sorry!".format(guest_names[1]))
print("Hello, {}, I can only invite two people, sorry!".format(guest_names[2]))
print("Hello, {}, I can only invite two people, sorry!".format(guest_names[3]))
print("Hello, {}, I can only invite two people, sorry!".format(guest_names[4]))
print("Hello, {}, I can only invite two people, sorry!".format(guest_names[5]))
guest_names.pop(0)
print("Hello, {}, sorry but your un-invited".format(guest_names[0]))
guest_names.pop(1)
print("Hello, {}, sorry but your un-invited".format(guest_names[1]))
guest_names.pop(2)
print("Hello, {}, sorry but your un-invited".format(guest_names[2]))
guest_names.pop(-1)
del guest_names[0]
del guest_names[0]
print(guest_names)

print(len(guest_names))
