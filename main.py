from methods import Acceptance_rejection_method_Beta, show


alpha = 2
beta = 5
n_instances = 100

betas = Acceptance_rejection_method_Beta(n_instances, alpha, beta)
show(n_instances, alpha, beta, betas)



