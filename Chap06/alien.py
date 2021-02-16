#Dictionary simple
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#adding new value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Custom Dictionary
favourite_teams = {
	'michael': 'Man Utd',
	'paul':'Liverpool',
	'bruce': 'Chelsea',
	'freddie': 'Arsenal',
}
for name, team in favourite_teams.items():
	print(f"\n{name.title()}'s favorite team is {team.title()}")

