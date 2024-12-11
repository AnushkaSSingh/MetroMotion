import pandas as pd
from matplotlib import pyplot as mypy
from termcolor import colored

def print_header():
    """Prints the header for the application."""
    print("")
    print(colored("-" * 50 + "  MetroMotion  " + "-" * 50, "red"))
    print(colored(
        "\nWelcome to MetroMotion - your comprehensive platform for exploring public transport trends and statistics worldwide.\n"
        "Discover insights into global commuting patterns, city comparisons, and sustainable travel options, all at your fingertips!\n",
        "cyan"
    ))


def page_maker(page_title, options):
    """Generates a consistent page layout for each menu."""
    print("\n", "-" * 25, page_title, "-" * 25, "\n")
    for key, value in options.items():
        print(f"{key}. {value}")
    print("")


def get_user_choice(num_max):
    """Validates user input for menu selection."""
    while True:
        choice = input("Please select an option: ")
        if not choice.isdigit():
            print(colored("Invalid input! Please enter a number.", "red"))
        elif int(choice) < 1 or int(choice) > num_max:
            print(colored("Invalid input! Please enter a valid menu option.", "red"))
        else:
            return int(choice)


def display_info(title, description, data_file, graph_type, x, y, color):
    """Displays information and generates the graph."""
    print(colored(title, "yellow"))
    print("-" * 130)
    print(description)
    print("-" * 130)
    print(pd.read_csv(data_file))

    showData = input("Would you like to see graphical representation of the data? (y/n): ").lower()
    if showData != "y":
        return
    print(colored("\nShowing a graph of this data...\n", "light_magenta"))

    try:
        data = pd.read_csv(data_file)
        graphs(graph_type, data, x, y, color)
    except FileNotFoundError:
        print(colored("Error: Data file not found!", "red"))
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))


def graphs(graph_type, df, x, y, color):
    """Plots graphs based on the provided data."""
    try:
        if graph_type == "line":
            mypy.plot(df[x], df[y], color=color)
            mypy.ylabel(y, fontsize=10)
        elif graph_type == "bar":
            mypy.bar(df[x], df[y], color=color)
            mypy.ylabel(y, fontsize=10)
        elif graph_type == "stacked":
            bottom = [0] * len(df)
            for i in range(1, len(y)):
                mypy.bar(df[x], df[y[i]], bottom=bottom, color=color[i - 1], label=y[i])
                bottom = [a + b for a, b in zip(bottom, df[y[i]])]
            mypy.legend()
            mypy.tight_layout()

        mypy.xticks(rotation=45, ha='right', fontsize=7)
        mypy.xlabel(x, fontsize=10)
        mypy.show()
    except KeyError:
        print(colored("Error: Invalid column names for graphing!", "red"))


def main():
    print_header()
    menu_options = {
        1: "Indian Railways",
        2: "Indian Metro",
        3: "Domestic Airways",
        4: "Indian Roadways",
        5: "Indian Waterways",
        6: "Revenue Share among Public Transport Sectors",
        7: "Exit"
    }

    while True:
        page_maker("MENU", menu_options)
        choice = get_user_choice(len(menu_options))

        if choice == 1:
            display_info(
                "Indian Railways",
                '''
                Indian Railways is the fourth largest railway network in the world by size. 
                It is also the second largest public transport provider in India.  
                The network is known for its vast reach and connectivity, 
                making it an essential mode of transport for millions of people in India.
                ''',
                "railways.csv",
                "bar",
                "Year",
                "Passenger traffic (in billions)",
                "#63a6e0"
            )
        elif choice == 2:
            display_info(
                "Indian Metro",
                '''
                The Indian Metro is a rapid transit system that operates in several major cities in India. 
                It is known for its modern infrastructure, state-of-the-art technology, and world-class facilities. 
                The Indian Metro plays a crucial role in reducing traffic congestion, air pollution, and travel time in urban areas.
                ''',
                "metro.csv",
                "bar",
                "System",
                "Annual Ridership (in millions)",
                "#63e091"
            )
        elif choice == 3:
            display_info(
                "Domestic Airways",
                '''
                Domestic air travel is an essential mode of transport for millions of people in India. 
                It offers fast, convenient, and comfortable travel options for passengers across the country. 
                The domestic aviation sector is known for its connectivity, efficiency, and safety standards.
                ''',
                "airport.csv",
                "stacked",
                "Year",
                ["Number of Audits/Inspections", "Audit", "Inspection", "Total"],
                ["#182787", "#551887", "#d41948"]
            )
        elif choice == 4:
            display_info(
                "Indian Roadways",
                '''
                Indian Roadways is the largest mode of transportation in India. 
                It plays a crucial role in connecting cities, towns, and villages across the country. 
                The road transport sector is known for its extensive network, affordability, and accessibility to remote areas.
                ''',
                "bus.csv",
                "stacked",
                "State",
                ["Bus Tax Amount", "Bus Tax/month", "Bus Tax/Annum"],
                ["#249e28", "#97f250"]
            )
        elif choice == 5:
            display_info(
                "Indian Waterways",
                '''
                Indian Waterways are an important mode of transport for cargo and passenger traffic in India. 
                They provide an eco-friendly, cost-effective, and efficient transportation alternative. 
                The water transport sector is known for its capacity to carry heavy loads, reduce road congestion, and promote inland water trade.
                ''',
                "ferries.csv",
                "stacked",
                "Year",
                ["Cargo Volume", "National Waterways- I", "National Waterways- II", "National Waterways-III"],
                ["#F72C5B", "#FF748B", "#A7D477"]
            )
        elif choice == 6:
            display_info(
                "Revenue Share among Public Transport Sectors",
                '''
                Public transport plays a vital role in the mobility and accessibility of people in urban areas. 
                It includes various modes of transportation such as buses, metros, trains, and trams. 
                Understanding the revenue share among different public transport sectors is essential for sustainable urban planning and development.
                ''',
                "percent_share.csv",
                "stacked",
                "Year",
                ["Revenue Share (%)", "Road Transport", "Railways", "Water Transport", "Air Transport", "Services Incidental to Transport"],
                ["#e76f51", "#f4a261", "#e9c46a", "#2a9d8f", "#264653"]
            )
        elif choice == 7:
            print(colored("Thank you for using MetroMotion. Have a great day!", "light_green"))
            break

if __name__ == "__main__":
    main()