
import scipy.special as cs #импорт скипи, используется для вычисления гаммы

def Betapdf(a,b,x):

    return (x**(a-1)*(1-x)**(b-1))/((cs.gamma(a)*cs.gamma(b))/cs.gamma(a+b))

def Betacdf(a,b,x,l,c):

    from scipy import integrate
    def f(u):
        return (((u)**(a-1))*((c-u)**(b-1)))

    v, err = integrate.quad(f, l, x.all())

    return (((1/Betapdf(a,b,x) * (v))))/10*2
