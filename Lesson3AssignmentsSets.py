# Lesson 3: Assignments | Sets
# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!
# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!
# ________________________________________
# 1. Python Sets Adventure
# Objective: The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:
# 1.	Destinations that both airlines fly to.
# 2.	Destinations unique to your airline.
# 3.	Whether there are any destinations that neither airline shares.
# Example Code:
# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
# all_possible_routes = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "SYD", "HND"}

"""
To solve this problem, we use the set function
Use the intersection operator & to find elements that are common to both sets.
Use the difference set operator - to find elements that exist only in the our_routes collection.
Use the complementary set operator - subtract all destinations of both airlines from all possible destinations (concatenation operator |).

"""
def d():
   print("="*75)

d()
def compare_flight_routes(our_routes, competitor_routes, all_possible_routes):
    # Destinations that both airlines fly to
    common_routes = our_routes & competitor_routes
    # Destinations unique to your airline
    unique_our_routes = our_routes - competitor_routes
    # Destinations neither airline shares
    neither_routes = all_possible_routes - (our_routes | competitor_routes)
    return common_routes, unique_our_routes, neither_routes

# Example usage
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
all_possible_routes = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "SYD", "HND"}

# Compare flight paths
common_routes, unique_our_routes, neither_routes = compare_flight_routes(our_routes, competitor_routes, all_possible_routes)

# Print results
print(f"Destinations both airlines fly to: {common_routes}")
print(f"Destinations unique to our airline: {unique_our_routes}")
print(f"Destinations neither airline shares: {neither_routes}")


# ________________________________________
# 2. Set Operations in Data Analysis
# Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.
# Example Code:
# customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
# Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.
d()
def remove_duplicates(customer_ids):
  """
  Removes duplicate customer IDs from a list and returns a set of unique IDs.
  """
  # Convert the list to a set to automatically remove duplicates
  unique_customer_ids = set(customer_ids)
  return unique_customer_ids

# Example usage
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_ids = remove_duplicates(customer_ids)

print("Unique Customer IDs:", unique_ids)
