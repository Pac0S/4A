import numpy as np
import random


def generate_genome(size):
	genome = []
	for i in range(size):
		gene = random.choice([-1,1])
		genome.append(gene)
	return genome
	
def calculate_cost(genome, r0):
	total = 0
	cost = 0
	for gene in genome:
		total += gene
		if abs(total) > abs(r0):
			cost += 1		
	return cost


def generate_population(number, size):
	population = np.zeros((number,size))
	#dim 1 : stocke la population
	#dim 2 : stocke les genomes
	for n in range(number):
		genome = generate_genome(size)
		population[n] = genome
	return population
	
		
		
def sort_genomes(population, r0):
	costs = []
	for i in range(len(population)):
		cost = calculate_cost(population[i], r0)
		costs.append(cost)
	order = np.argsort(costs)
	#print(costs) #Couts associes aux genomes de population, dans le meme ordre
	#print(order) #Indice des couts tries par ordre croissants, donc des genomes
	shape = np.shape(population)
	number = shape[0]
	size = shape[1]
	sorted_pop = np.zeros((number,size))
	for i in range(number):
		indice = order[i]
		genome = population[indice]
		sorted_pop[i] = genome
	#print(population)
	#print(sorted_pop)
	return sorted_pop
	
	
def to_mute(sor_pop, Ns):
	size_to_mute = Ns
	mutating = np.zeros((size_to_mute, np.shape(sor_pop)[1]))
	for i in range(len(mutating)):
		mutating[len(mutating)-i-1] = sor_pop[len(sor_pop)-i-1]
	return mutating
	
def mutation(mut_pop, Tm):
	for genome in mut_pop:
		for gene in genome:
			flip_coin = random.random()
			if(flip_coin <=Tm):
				if(gene == -1):
					gene = 1
					print("-1 became 1")
				else:
					gene = -1
					print("1 became -1")
			else:
				print("nothing happened")
		print("Next genome\n")

			


if __name__ == '__main__':
	
	'''
	genome1 = generate_genome(10)
	print ("genome 1: " + str(genome1))
	cost1 = calculate_cost(genome1,1)
	print("genome 1 costs : " + str(cost1))
	print("")
	'''
	
	
	pop1 = generate_population(5,10)
	print(pop1)
	
	print("")
	
	sorted_pop1 = sort_genomes(pop1, 1)
	print(sorted_pop1)
	
	print("")
	
	mut_pop1 = to_mute(sorted_pop1, int(len(sorted_pop1)/2))
	print(mut_pop1)
	
	print("")
	
	mutation(mut_pop1,0.5)
	print(mut_pop1)
	
	
	
	
