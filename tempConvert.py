# make Celcius
def f_to_c(f):
 c = (5/9*(f-32))
 return c

def k_to_c(k):
 c = k - 273.15
 return c


# make Fahrenheit
def c_to_f(c):
 f = (c * 1.8)+32
 return f

def k_to_f(k):
 c = k_to_c(k)
 f = c_to_f(c)
 return f


# make Kelvin
def c_to_k(c):
 k = c + 273.15
 return k

def f_to_k(f):
 c = f_to_c(f)
 k = c+ 273.15
 return k
 
# Debug
def debug(f):
 return f
