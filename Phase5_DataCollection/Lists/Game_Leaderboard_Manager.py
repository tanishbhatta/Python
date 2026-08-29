"""
Requirements:

Create an initial leaderboard with at least 5 players.
Add one new player to the end.
Add one player into the middle rankings.
Merge another leaderboard containing at least 3 players.
Display the leaderboard after every operation.
"""
leaderboard = ['Magnus', 'Gotham', 'Hikaru', 'Elon', 'Steve']
leaderboard.append('Pragg')
print(leaderboard)

leaderboard.insert(3, 'Hitesh')
print(leaderboard)

leadersecond = ['Aarush', 'Ronaldo', 'Messi']

leaderboard.extend(leadersecond)
print(leaderboard)

