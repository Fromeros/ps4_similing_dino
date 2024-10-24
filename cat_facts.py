import requests
import matplotlib.pyplot as plt

# Function to retrieve a random cat fact from Cat Facts API
def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['fact']
    else:
        raise Exception(f"Error {response.status_code}: Could not retrieve data")

# Function to retrieve multiple cat facts
def get_multiple_cat_facts(num_facts):
    facts = []
    for _ in range(num_facts):
        fact = get_cat_fact()
        facts.append(fact)
    return facts

# Function to display cat facts and visualize the length of each fact
def display_and_plot_facts(num_facts):
    facts = get_multiple_cat_facts(num_facts)
    
    print("Here are some interesting cat facts:")
    for i, fact in enumerate(facts, 1):
        print(f"{i}. {fact}")
    
    # Analyze the length of each fact
    fact_lengths = [len(fact) for fact in facts]
    
    # Plot the length of each fact
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, num_facts+1), fact_lengths, color='purple')
    plt.title("Length of Cat Facts")
    plt.xlabel("Fact Number")
    plt.ylabel("Number of Characters")
    plt.xticks(range(1, num_facts+1))
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Main script logic
if __name__ == "__main__":
    NUM_FACTS = 5  # You can change this to any number of facts you want to retrieve
    display_and_plot_facts(NUM_FACTS)
