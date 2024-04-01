# Arbitary argument: *args

# def sum(*args):  #args is used for multiple values
#     total= 0
#     for n in args:
#         total+=n
#     return total  #return  gives result of function and stopes execution of function
# result = sum(2,5,3)
# print(result)

#arbitrary argument: **kwargs which contain data in key and value pairs
def hello(**kwargs):   #parameter
    print("Hello",kwargs["name"], "Welcome to Web development Training")
    print(kwargs["course_name"])
hello(name="Pema",course_name="python with django",another_course="Python with Data Science")

