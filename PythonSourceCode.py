# Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset – Let's load the data and see what the world of remote work has to reveal!
df = pd.read_csv('Impact_of_Remote_Work_on_Mental_Health.csv')

# Displaying the first few rows – Gotta know what we're dealing with, right?
df.head()

# Insight 1: Average Work-Life Balance Rating by Gender – Who's balancing work and life like a pro?
print("\nInsight 1: Average Work-Life Balance Rating by Gender")
avg_work_life_by_gender = df.groupby('Gender')['Work_Life_Balance_Rating'].mean().sort_values(ascending=False)
print(avg_work_life_by_gender)

# Bar plot for Insight 1
plt.figure(figsize=(8, 6))
avg_work_life_by_gender.plot(kind='bar', color=['skyblue', 'orange'])
plt.title('Average Work-Life Balance Rating by Gender')
plt.ylabel('Work Life Balance Rating')
plt.show()

# Insight 2: Hours Worked Per Week vs Stress Level – More hours, more stress? Let's find out!
print("\nInsight 2: Hours Worked Per Week vs Stress Level (Categorical)")
avg_hours_by_stress = df.groupby('Stress_Level')['Hours_Worked_Per_Week'].mean()
print(avg_hours_by_stress)

# Line plot for Insight 2
plt.figure(figsize=(8, 6))
avg_hours_by_stress.plot(kind='line', marker='o', color='purple')
plt.title('Stress Level vs Hours Worked Per Week')
plt.ylabel('Hours Worked Per Week')
plt.show()

# Insight 3: Access to Mental Health Resources and its Impact on Productivity – Spoiler alert: Mental health matters!
print("\nInsight 3: Access to Mental Health Resources and its Impact on Productivity")
access_impact_productivity = df.groupby('Access_to_Mental_Health_Resources')['Productivity_Change'].value_counts(normalize=True)
print(access_impact_productivity)

# Pie chart for Insight 3
plt.figure(figsize=(8, 6))
df['Access_to_Mental_Health_Resources'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightgreen'], startangle=90)
plt.title('Access to Mental Health Resources – Pie chart')
plt.ylabel('')  # Hide the y-label for pie chart
plt.show()

# Insight 4: Number of Virtual Meetings and Social Isolation – Too many Zoom calls? Let’s see if you're feeling lonelier.
print("\nInsight 4: Number of Virtual Meetings and Social Isolation Rating")

# Grouping by the number of virtual meetings and calculating the average social isolation rating for each group
avg_isolation_by_meetings = df.groupby('Number_of_Virtual_Meetings')['Social_Isolation_Rating'].mean()

# Plotting a bar chart to show how the number of virtual meetings impacts social isolation ratings
plt.figure(figsize=(10, 6))
avg_isolation_by_meetings.plot(kind='bar', color='lightseagreen')
plt.title('Average Social Isolation Rating by Number of Virtual Meetings')
plt.xlabel('Number of Virtual Meetings')
plt.ylabel('Average Social Isolation Rating')
plt.xticks(rotation=45)
plt.show()

# Insight 5: Impact of Years of Experience on Stress Level – Does experience make you zen or just stressed in a different way?
print("\nInsight 5: Impact of Years of Experience on Stress Level")
avg_stress_by_experience = df.groupby('Years_of_Experience')['Stress_Level'].value_counts(normalize=True)
print(avg_stress_by_experience)

# Area plot for Insight 5
plt.figure(figsize=(8, 6))
df.groupby('Years_of_Experience')['Stress_Level'].value_counts().unstack().plot(kind='area', stacked=False)
plt.title('Years of Experience vs Stress Level – Area Plot')
plt.ylabel('Stress Level')
plt.show()

# Insight 6: Relationship Between Company Support and Satisfaction with Remote Work – Are companies making remote life sweet or salty?
print("\nInsight 6: Relationship Between Company Support and Satisfaction with Remote Work")
avg_satisfaction_by_support = df.groupby('Company_Support_for_Remote_Work')['Satisfaction_with_Remote_Work'].value_counts(normalize=True)
print(avg_satisfaction_by_support)

# Bar plot for Insight 6
plt.figure(figsize=(8, 6))
df['Company_Support_for_Remote_Work'].value_counts().plot(kind='bar', color='salmon')
plt.title('Company Support for Remote Work')
plt.ylabel('Count')
plt.show()

# Insight 7: Physical Activity and Sleep Quality Correlation – Because you can’t Netflix all day and expect to sleep like a baby.
print("\nInsight 7: Physical Activity and Sleep Quality Correlation")
plt.figure(figsize=(8, 6))
df.groupby('Physical_Activity')['Sleep_Quality'].value_counts().unstack().plot(kind='bar', stacked=True)
plt.title('Physical Activity vs Sleep Quality – Stacked Bar')
plt.ylabel('Count')
plt.show()

# Insight 8: Work-Life Balance Rating by Industry – Which industry is the work-life balance MVP?
print("\nInsight 8: Work-Life Balance Rating by Industry")
avg_work_life_by_industry = df.groupby('Industry')['Work_Life_Balance_Rating'].mean().sort_values(ascending=False)
print(avg_work_life_by_industry)

# Bar plot for Insight 8
plt.figure(figsize=(10, 6))
avg_work_life_by_industry.plot(kind='bar', color='lightblue')
plt.title('Average Work-Life Balance Rating by Industry')
plt.ylabel('Work-Life Balance Rating')
plt.show()

# Insight 9: Gender and Mental Health Conditions – Do mental health struggles play favorites? Let’s see.
print("\nInsight 9: Gender and Mental Health Conditions")
gender_mental_health = df.groupby('Gender')['Mental_Health_Condition'].value_counts(normalize=True)
print(gender_mental_health)

# Pie chart for Insight 9
plt.figure(figsize=(8, 6))
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightpink'], startangle=90)
plt.title('Gender Distribution – Pie Chart')
plt.ylabel('')  # Hide the y-label for pie chart
plt.show()

# Insight 10: Impact of Job Role on Productivity Change – Some roles are productivity black holes... but which ones?
print("\nInsight 10: Impact of Job Role on Productivity Change")
job_productivity = df.groupby('Job_Role')['Productivity_Change'].value_counts(normalize=True)
print(job_productivity)

# Funnel plot for Insight 10 (Funnel plot is a bit tricky in matplotlib, so we'll use a bar as an alternative)
plt.figure(figsize=(10, 6))
df['Job_Role'].value_counts().plot(kind='bar', color='gold')
plt.title('Job Role Distribution – (Funnel-like Bar)')
plt.ylabel('Count')
plt.show()

# You can replicate the pattern for the remaining insights using these chart types.
