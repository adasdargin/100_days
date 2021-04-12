from prettytable import PrettyTable

table = PrettyTable()   #defing an object
table.add_column("Pokemon Table", ["Pikachu", "Squirtle", "Chamander"])     #modifying method
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"   #changing attribute

print(table)
