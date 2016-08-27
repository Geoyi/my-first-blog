print("Hello Django")
if 3>4:
    print("correct")
else:
    print("not correct")
    
name = "Lala"
if name == "Kiya":
    print("hello Lala")
elif name == "Lala":
    print("hello Lala")
else:
    print("hello there")
volume = 80
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

if volume >=80:
    volume=81
    print("Too loud")
    
# def hi():
#     print("Hi there!")
#     print("What do you want for breakfast?")
# hi()


# def hi(name):
#     if name=="Ana":
#         print("Hi Ana")
#     elif name =="Ali":
#         print("Hi Ali")
#     else:
#         print("Hi anonymous")
# hi('Ana')

# Girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You','Ana', 'Lala']
# for name in Girls:
#     # def hi(name):
#         print('Hi'+name+'!')

Girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You','Ana', 'Lala']
for name in Girls:
    print(name)
    print("Next girl")

for i in range(1,10):
    print(i)
    