import pandas as pd                         # for data manipulation and analysis
from matplotlib import pyplot as mypy       # for generating visualizations
from termcolor import colored               # for beautiful text formatting
print("")
print(colored("-"*50 + "  MetroMotion  "+"-"*50, "red"))
print(colored("\nWelcome to MetroMotion - your comprehensive platform for exploring public transport trends and statistics worldwide.\nDiscover insights into global commuting patterns, city comparisons, and sustainable travel options, all at your fingertips!\n", "cyan"))


# page making function to generate a consistent page layout for each menu page

def page_maker(page_title,dict):    # page_title:string; dict:dictionary; 
    global exit
    exit = True
    print("\n","-"*25,page_title,"-"*25,"\n")
    
    for i,j in dict.items():
        print(f"{i}. {j}")   # displays a sub-menu for each menu page
    print("")

    num_max = len(dict)
    # let user choose an option from the menu
    choice = input("Please select an option: ")
    
    # check if the input is a number
    if choice.isdigit() == False:
        print(colored("Invalid input! Please enter a number from the menu options.", "red"))
        return page_maker(page_title,dict)
    # check else if the input exceeds the max length of the dictionary or if it equal to zero
    if int(choice) > num_max or int(choice) == 0:
        print(colored("Invalid input! Please enter a number from the menu options.", "red"))
        return page_maker(page_title,dict)
    else:
        choice = int(choice)
    
    # INPUT HANDLING
    if choice == 1:
        print(colored("Indian Railways", "yellow"))
        print(
            '''
            Indian Railways is the fourth largest railway network in the world by size. 
            It is also the second largest public transport provider in India.  
            The network is known for its vast reach and connectivity, 
            making it an essential mode of transport for millions of people in India.
            '''
            )
        print(colored("Showing the passenger traffic data for Indian Railways from 2010 to 2022.\n", "light_magenta"))
        data=pd.read_csv("railways.csv")
        graphs("bar", data,"Year","Passenger traffic (in billions)", "#63a6e0")
    elif choice == 2:
        print(colored("Indian Metro", "yellow"))
        print(
            '''
              The Indian Metro is a rapid transit system that operates in several major cities in India. 
              It is known for its modern infrastructure, state-of-the-art technology, and world-class facilities. 
              The Indian Metro plays a crucial role in reducing traffic congestion, air pollution, and travel time in urban areas.
              '''
        )
        print(colored("Showing the Annual Ridership for different metro systems across India.\n", "light_magenta"))
        data=pd.read_csv("metro.csv")
        graphs("bar", data,"System","Annual Ridership (in millions)", "#63e091")
    elif choice == 3:
        print(colored("Domestic Airways", "yellow"))
        print(
            '''
            Domestic air travel is an essential mode of transport for millions of people in India. 
            It offers fast, convenient, and comfortable travel options for passengers across the country. 
            The domestic aviation sector is known for its connectivity, efficiency, and safety standards.
            '''
        )
        print(colored("Showing the annual report data for Domestic Airways from 2020 to 2021.\n", "light_magenta"))
        data=pd.read_csv("airport.csv")
        graphs("stacked", data,"Year",["Number of Audits/Inspections", "Audit", "Inspection", "Total"], ["#182787", "#551887", "#d41948"])
    elif choice == 4:
        print(colored("Indian Roadways", "yellow"))
        print(
            '''
            Indian Roadways is the largest mode of transportation in India. 
            It plays a crucial role in connecting cities, towns, and villages across the country. 
            The road transport sector is known for its extensive network, affordability, and accessibility to remote areas.
            '''
        )
        print(colored("Showing the number of registered motor vehicles in India from 1951 to 2016.\n", "light_magenta"))
        data=pd.read_csv("bus.csv")
        graphs("stacked", data,"State",["Bus Tax Amount", "Bus Tax/month", "Bus Tax/Annum"], ["#249e28", "#97f250"])
    elif choice == 5:
        print(colored("Indian Waterways", "yellow"))
        print(
            '''
            Indian Waterways are an important mode of transport for cargo and passenger traffic in India. 
            They provide an eco-friendly, cost-effective, and efficient transportation alternative. 
            The water transport sector is known for its capacity to carry heavy loads, reduce road congestion, and promote inland water trade.
            '''
        )
        print(colored("Showing the cargo traffic data for Indian Waterways from 2010 to 2022.\n", "light_magenta"))
        data=pd.read_csv("ferries.csv")
        graphs("stacked", data,"Year",["Cargo Volume", "National Waterways- I", "National Waterways- II", "National Waterways-III"], ["#F72C5B", "#FF748B", "#A7D477"])
    elif choice == 6:
            print(colored("Revenue Share among Public Transport Sectors", "yellow"))
            print(
                '''
                Public transport plays a vital role in the mobility and accessibility of people in urban areas. 
                It includes various modes of transportation such as buses, metros, trains, and trams. 
                Understanding the revenue share among different public transport sectors is essential for sustainable urban planning and development.
                '''
            )
            print(colored("Showing the revenue share among different public transport sectors in India.\n", "light_magenta"))
            data=pd.read_csv("percent_share.csv")
            graphs("stacked", data,"Year",["Revenue Share (%)", "Road Transport", "Railways", "Water Transport", "Air Transport", "Services Incidental to Transport"], 
                   ["#e76f51", "#f4a261", "#e9c46a", "#2a9d8f", "#264653"])
    if choice == 7:
        exit = False
        print(colored("Thank you for using MetroMotion. Have a great day!", "light_green"))


# GRAPHING FUNCTION
def graphs(type,df,x,y, _color):
    """
        type: string, type of graph to be plotted (line/bar)
        df: required DataFrame
        x, y: column names of the DataFrame 
        _color: color of the graph
    """
    if type=="line":
        mypy.plot(df[x], df[y], color=_color)
        mypy.ylabel(y,fontsize=10)
    elif type=="bar":
        mypy.bar(df[x], df[y], color=_color)
        mypy.ylabel(y,fontsize=10)
    elif type == "stacked":
        bottom = [0] * len(df)  # Initialize the bottom array with zeros
        for i in range(1, len(y)):
            mypy.bar(
                df[x], 
                df[y[i]], 
                bottom=bottom, 
                color=_color[i-1], 
                label=y[i]
            )
            bottom += df[y[i]]  # Update the bottom for the next stack
        
        mypy.legend()
        mypy.tight_layout()

    mypy.xticks(rotation=45,ha='right',fontsize=7)
    mypy.xlabel(x,fontsize=10)
    mypy.show()

    
    
main_menu_options= {
    1:"Indian Railways",
    2:"Indian Metro",
    3:"Domestic Airways",
    4:"Indian Roadways",
    5:"Indian Waterways",
    6:"Revenue Share among Public Transport Sectors",
    7:"Exit",
}

while exit:
    page_maker("MENU", main_menu_options)