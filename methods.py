from sympy import integrate, init_printing, exp, oo
from sympy.abc import x
from math import e, factorial
from numpy import random, zeros, linspace
import matplotlib.pyplot as plt
from scipy.stats import beta, gaussian_kde

def UniformInstance():
    u = random.uniform(0, 1)
    return u

def T(alpha):
    return factorial(alpha-1)

def f_gamma(x, alpha, beta):
    f = ((beta**alpha)*(x**(alpha-1))*(e**(-1*beta*x)))/(T(alpha))
    return f

def lambd(alpha):
    if alpha > 1:
        return (2*alpha - 1)**(0.5)
    return "alpha must be higher than 1"

def u(alpha, lambd):
    return alpha**(lambd)

def r(x, alpha):
    if x == 0:
        return 0
    elif x > 0:
        lamb = lambd(alpha)
        u_ = u(alpha, lamb)
        r = (lamb*u_*(x**(lamb-1)))/((u_ + (x**lamb))**(2))
        return r

def c(alpha):
    c = ((4*(alpha**alpha))*(e**(-1*alpha)))/((lambd(alpha))*T(alpha))
    return c

def t (x, alpha):
    r_ = r(x, alpha)
    c_ = c(alpha)
    t_ = r_*c_
    return t_

def R_inv (z, alpha):
    if 0 <= z < 1:
        lamb = lambd(alpha)
        u_ = u(alpha, lamb)
        R_inv_ = ((z*u_)/(1-z))**(1/lamb)
        return R_inv_
    return "z must be in [0,1)"

def R(x, alpha):
    l = lambd(alpha)
    u_ = u(alpha, l)
    r = x**(l)/(u_+ x**(l))
    return r

def match_gamma(alpha):
    match = 0
    y = 0
    while match == 0:
         U_ = UniformInstance()
         x = R_inv(U_, alpha)
         f = f_gamma(x, alpha, 1)
         t_ = t(x, alpha)
         U_2 = UniformInstance()
         if U_2 <= (f/t_):
             y = x
             match += 1
    return y

def Acceptance_rejection_method_Beta(n_instances, alpha, beta):
    instances = []
    graph = []
    match = 0

    while match < n_instances:
        instance = []
        g_1 = match_gamma(alpha)
        g_2 = match_gamma(beta)
        inst = g_1/(g_1+g_2)
        instance.append(g_1)
        instance.append(g_2)
        instance.append(inst)
        instances.append(instance)
        graph.append(inst)
        match += 1
    print(['instance', 'number', 'g_1', 'g_2', 'g_1/(g_1+g_2)'])
    for i in range(len(instances)):
        print("instance ",i+1, instances[i])    
    return graph

def Beta(x, alpha, beta):
    Beta_ = (x**(alpha-1)*(1-x)**(beta-1))*30
    return Beta_

def G_Beta(alpha, beta):
    beta_numbers = []
    while len(beta_numbers) < 100:
        U_ = UniformInstance()
        val = Beta(U_, alpha, beta)
        beta_numbers.append(val)
    return beta_numbers


def show(n_instances, alpha, beta, betas):
    dist_space = (min(betas), max(betas), n_instances)
    density = gaussian_kde(betas)
    plt.title('Density Beta(2,5)')
    plt.xlabel('Values')
    plt.ylabel('Density')
    xs = linspace(min(betas), 1, n_instances)
    plt.plot(xs, density(xs))
    plt.show()


    x = zeros(n_instances)
    for i in range(len(betas)):
        x[i] = betas[i]
    n, bins, patches = plt.hist(x, 10, facecolor='g', alpha=0.75)

    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram Beta(2,5)')
    plt.axis([0, 1, 0, 40])
    plt.grid(True)
    plt.show()
