import csv
import plotly.express as px
initial_pop = [1, 2]
shark_pop = initial_pop[0]
tuna_pop = initial_pop[1]
deltaT = 0.6
simulation_length = 600
shark_data = []
tuna_data = []
shark_data.append(1)
tuna_data.append(2)
with open('./shark_tuna_py.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='', quoting=csv.QUOTE_MINIMAL)
    for x in range(simulation_length):
        shark_pop += ((tuna_pop * shark_pop) - shark_pop) * deltaT
        tuna_pop += (tuna_pop - (shark_pop * tuna_pop)) * deltaT
        shark_data.append(shark_pop)
        tuna_data.append(tuna_pop)
        print(shark_pop, tuna_pop)
        writer.writerow([shark_pop,', ', tuna_pop])
    fig = px.line(x=shark_data, y=tuna_data)
    fig.show()
    fig.write_image("./graphs/shark_tuna.png")
