#guess
geneSet=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPKRSTUVWXYZ!."
target="Hello World!"
#generate a guess
import random
def generate_parent(length):
    genes=[]
    while len(genes)<length:
        samplesize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, samplesize))
        return''.join(genes)
#fitness  
def get_fitness(guess):
    return sum(1 for expected,actual in zip(target,guess)if(expected==actual))
#mutate
def mutate(parent):
    index=random.randrange(0,len(parent))
    childGenes=list(parent)
    newGene,alternate=random.sample(geneSet,2)
    childGenes[index]=alternate \
      if newGene==childGenes[index] \
      else newGene
    return''.join(childGenes)
#disaplay
import datetime
def display(guess):
    timeD=datetime.datetime.now()-startTime
    fitness=get_fitness(guess)
    print("{0}\{1}\{2}".format(guess, fitness, str(timeD)))
#main
random.seed()
startTime=datetime.datetime.now()
bestparent=generate_parent(len(target))
bestFitness=get_fitness(bestparent)
display(bestparent)
while True:
    child=mutate(bestparent)
    childFitness=get_fitness(child)
    if bestFitness>=childFitness:
        continue
    display(child)
    if childFitness>=len(bestparent):
        break
    bestFitness=childFitness
    bestparent=child