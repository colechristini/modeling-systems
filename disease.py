import csv
import plotly.express as px

initial_pop = [1, 2000]
infected = [initial_pop[0]]
susceptible = [initial_pop[1]]
recovered = [0]
total = [susceptible + recovered + infected]
deltaT = 0.001
alpha = 0.6
beta = 0.01
simulation_length = 6000

with open('./disease_spread.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for x in range(simulation_length):
        infected += [( infected[-1] + (beta * susceptible[-1] - alpha) * infected[-1] * deltaT)]
        susceptible += [(susceptible[-1] + (-beta * susceptible[-1] * infected[-1] ) * deltaT)]
        recovered += [alpha * infected[-1] * deltaT]
        total += [susceptible + recovered + infected]
        writer.writerow([infected, susceptible, recovered])
    fig = px.scatter_3d(x=susceptible, y=infected, z=recovered)
    fig.show()
    fig.write_image("./graphs/disease_spread.png")
