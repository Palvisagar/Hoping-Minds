#Program of distribution of probability
#Author Palvi Sagar
import matplotlib.pyplot as plt

# Ask the user to input the number of balls
num_balls = int(input("Enter the number of balls: "))

# Create an empty dictionary to store the number of balls of each color
ball_counts = {}

# Loop through each ball and ask the user to input its color
for i in range(num_balls):
    ball_color = input(f"Enter the color of ball {i+1}: ")
    
    # If the color is not already in the dictionary, add it with a count of 1
    if ball_color not in ball_counts:
        ball_counts[ball_color] = 1
    # If the color is already in the dictionary, increment its count by 1
    else:
        ball_counts[ball_color] += 1

# Calculate the probability of drawing each color of ball
colors = []
probabilities = []
for color, count in ball_counts.items():
    probability = count / num_balls
    colors.append(color)
    probabilities.append(probability)

# Create a bar chart of the probability distribution
plt.bar(colors, probabilities)
plt.xlabel('Ball Color')
plt.ylabel('Probability')
plt.title('Probability Distribution of Ball Colors')
plt.show()
