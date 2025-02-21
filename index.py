import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns  


df = pd.read_csv("ipl2024.csv")

# Check the Total Number of Matches in the Dataset
print("Total matches in the dataset:", df.shape[0])

# Find the Top 5 Teams with the Most Wins
team_wins = df['winner'].value_counts().head(5)
print(team_wins)

# Calculate Win Percentage of Each Team
total_matches = df['team1'].value_counts() + df['team2'].value_counts()
win_percentage = (team_wins / total_matches) * 100
print(win_percentage)

# Most Successful Player (Man of the Match Awards)
mvp = df['player_of_the_match'].value_counts().head(10)
print(mvp)

# Set Figure Size
plt.figure(figsize=(10, 5))  

# Create the Bar Chart
sns.barplot(x=team_wins.index, y=team_wins.values, hue=team_wins.index, palette="coolwarm", legend=False)

# Set Titles and Labels
plt.title("Top 5 IPL Teams with Most Wins")  
plt.xlabel("Team")  
plt.ylabel("Number of Wins")  

# Rotate X-Axis Labels for Better Readability
plt.xticks(rotation=45)
plt.show()  

# Toss Decision Trends
toss_decision = df['toss_winner'].value_counts()
plt.pie(toss_decision, labels=toss_decision.index, autopct="%1.1f%%", colors=['#FF9999', '#66B2FF'])
plt.title("Toss Decision: Bat or Bowl?")
plt.show()


# plt.show(block=True)