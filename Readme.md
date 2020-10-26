# Random variable generation: Acceptance-Rejection method of Beta distribution.

This method is a way to generates differents instances of a distribution. In this case is Beta. The acceptance-rejection method has three steps:
- First, generate a Y instance with r distribution. But what is r? r is the density of a distribution R that is used for generate Y instances. So, if we have r, we need to integrate between 0 and inf and get R. Now with R we need the inverse, so we calculate R^{-1}. With the inverse we need to generate a U instances, this is a uniform distribution between 0 and 1. After generate we evaluated U in R^{-1} and we get a Y instance.

- Second, generate another Uniform instances independent of Y, so we generate a u ~ U(0,1).

- Third, a comparison is necessary, we need to compare the u of the second step with f(Y)/t(Y). 
the comparison is:
```
u <= f(Y)/t(Y)
```
and if it is true, we are gonna do X = Y and return X and if it doesn't we need to repeat all the process.

# But what is X? and f? and t?

- X is an instance of a distribution F that we are generating, for this repo is te Beta distribution. 
- f is a density of F.
- t is a function that majorizes f.

It was a summary about this technique, if you want learn more about it you can search for information on the internet.
# This code is for Beta distribution with alpha > 1.

Now for generate instances of Beta we can use this method, but is just a step, because we need to do more for calculate. If we have a Beta(alpha, beta) is necessary separete this in two Betas: 
```
B1 = Beta(alpha,1)
B2 = Beta(beta,1)
```
and generate an intance Y_i for each one with the acceptation-rejection technique. And finally if you get both we can do:
```
 Y_1/(Y_1+Y_2) ~  Beta(alpha, beta) 
```
And with this you got a instance of Beta(alpha,beta), but if you want more? it would be very difficult to repeat this process many times. But here is the solution.

In the main file you have the variables:
- n_instances
- alpha
- beta

## n_instances
Is the number of instances that you want.
## alpha
Is the alpha value of the Beta parameters.
## beta
Is the beta value of the Beta parameters.

so you just need to set this variables with the values that you want and run the code. This gonna give you the instances with the values of Y_1, Y_2 and  Y_1/(Y_1+Y_2). Addiionally give you the histogram and the density.

## But remind, this technique sometimes does not give such good approximations, but it is because the procedure that the method has but if you want another approximation you can run the code again.
