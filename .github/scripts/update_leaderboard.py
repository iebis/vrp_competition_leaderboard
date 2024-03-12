import pandas as pd

# Load the CSV file
df = pd.read_csv('output/central_results.csv')

# Process the DataFrame to find the best score per group
# This is a placeholder - adapt the logic based on your scoring rules
best_scores = df.sort_values(by=['Score', 'Date Time'], ascending=[True, False]).drop_duplicates('Group')

# Clear the leaderboard section in README.md and prepare new content
with open('README.md', 'r+') as file:
    content = file.read()
    start = content.find('<!-- LEADERBOARD_START -->')
    end = content.find('<!-- LEADERBOARD_END -->') + len('<!-- LEADERBOARD_END -->')
    new_leaderboard = "\n".join([
        "| Rank | Date | GroupNumber | Feasible | Score | Runtime |",
        "| ------ | ------------ | ------------------- |-------------| ------- | ------- |",
    ] + [
        f"| {i+1} | {row['Date Time']} | {row['Group']} | {'✅' if row['Overall Feasible'] == 'Yes' else '❌'} | {row['Score']} | {row['Total Runtime (seconds)']}s |"
        for i, row in best_scores.iterrows()
    ])
    new_content = content[:start] + '<!-- LEADERBOARD_START -->\n' + new_leaderboard + '\n' + content[end:]
    file.seek(0)
    file.write(new_content)
    file.truncate()
