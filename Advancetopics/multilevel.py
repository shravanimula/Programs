class A():
    a_name="aaaa"
    a_age=66

class B(A):
    b_name="bbbb"
    b_age=22

class C(B):
    c_name="ccc"
    c_age=5


var=C()
print("class C:",var.c_name,var.c_age)
print("class B:",var.b_name,var.b_age)
print("class A:",var.a_name,var.a_age)
