import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from graphics import *
from matplotlib.ticker import FuncFormatter

def LoadData():
    demographics_table = pd.read_excel('demographics.xlsx')
    humancapital_table = pd.read_excel('humancapital.xlsx')
    countrydata = pd.read_csv('world_population.csv')
    return demographics_table, humancapital_table, countrydata


def startButton(win):
    title = Text(Point(2, 3.5), "InsightGRAPHIX")
    title.setSize(30)
    title.setStyle("bold")
    title.setFace("courier")
    title.draw(win)

    title2 = Text(Point(2, 3.25), "Application")
    title2.setSize(20)
    title2.setFace("courier")
    title2.draw(win)

    start = Rectangle(Point(1,1.5), Point(3,2.5))
    start.setFill("lightgrey")
    start.draw(win)

    startText= Text(Point(2,2), "START")
    startText.setSize(30)
    startText.setStyle("bold")
    startText.setFace("courier")
    startText.draw(win)

    while True:
        pt = win.getMouse()
        if pt:
            if pt.getX() > 1 and pt.getX() < 3:
                if pt.getY() > 1 and pt.getY() < 3:
                    start.undraw()
                    startText.undraw()
                    title.undraw()
                    title2.undraw()
                    break

def create_button(win, label, p1, p2):
    button = Rectangle(p1, p2)
    button.setFill("lightgrey")
    button.draw(win)

    text_point = Point((p1.getX() + p2.getX()) / 2, (p1.getY() + p2.getY()) / 2)
    text = Text(text_point, label)
    text.setFace("courier")
    text.setSize(15)
    text.draw(win)

    return button, text

def undrawbuttons(*elements):
    for element in elements:
        element.undraw()

def DisplayMenu(win):
    title = Text(Point(2, 3.5), "SELECT AN OPTION")
    title.setSize(30)
    title.setFace("courier")
    title.setStyle("bold")
    title.draw(win)

    button_region, label_region = create_button(win, "Plots for Regions ", Point(1, 2.5), Point(3, 3))
    button_country, label_country = create_button(win, "Country Populations", Point(1, 1.5), Point(3, 2))

    while True:
        click_point = win.getMouse()
        if button_region.getP1().getX() < click_point.getX() < button_region.getP2().getX() and \
                button_region.getP1().getY() < click_point.getY() < button_region.getP2().getY():
            undrawbuttons(button_region, label_region,button_country, label_country,  title)
            return "region"

        elif button_country.getP1().getX() < click_point.getX() < button_country.getP2().getX() and \
                button_country.getP1().getY() < click_point.getY() < button_country.getP2().getY():
            undrawbuttons(button_region, label_region,button_country, label_country,  title)
            return "country"



def RegionMenu(win):
    title = Text(Point(2, 4), "PLOT OPTIONS")
    title.setSize(30)
    title.setFace("courier")
    title.setStyle("bold")
    title.draw(win)

    button_population, label_population = create_button(win, "Age Distribution /region", Point(1, 3), Point(3, 3.5))
    button_education, label_education = create_button(win, "Level of Education /region", Point(1, 2.5), Point(3, 3))
    button_life_expectancy, label_life_expectancy = create_button(win, "Life Expectancy /region", Point(1, 2), Point(3, 2.5))
    button_population_density, label_population_density = create_button(win, "Population Density /region", Point(1, 1.5), Point(3, 2))

    while True:
        click_point = win.getMouse()


        if button_population.getP1().getX() < click_point.getX() < button_population.getP2().getX() and \
                button_population.getP1().getY() < click_point.getY() < button_population.getP2().getY():
            undrawbuttons(button_population, label_population, button_education, label_education,
                          button_life_expectancy, label_life_expectancy, button_population_density,
                          label_population_density, title)
            region = select_region(win)
            return(1, region)

        elif button_education.getP1().getX() < click_point.getX() < button_education.getP2().getX() and \
                button_education.getP1().getY() < click_point.getY() < button_education.getP2().getY():
            undrawbuttons(button_population, label_population, button_education, label_education,
                          button_life_expectancy, label_life_expectancy, button_population_density,
                          label_population_density, title)
            region = select_region(win)
            return(2, region)

        elif button_life_expectancy.getP1().getX() < click_point.getX() < button_life_expectancy.getP2().getX() and \
                button_life_expectancy.getP1().getY() < click_point.getY() < button_life_expectancy.getP2().getY():
            undrawbuttons(button_population, label_population, button_education, label_education,
                          button_life_expectancy, label_life_expectancy, button_population_density,
                          label_population_density, title)
            return(3, None)

        elif button_population_density.getP1().getX() < click_point.getX() < button_population_density.getP2().getX() and \
                button_population_density.getP1().getY() < click_point.getY() < button_population_density.getP2().getY():
            undrawbuttons(button_population, label_population, button_education, label_education,
                          button_life_expectancy, label_life_expectancy, button_population_density,
                          label_population_density, title)
            return(4, None)

def select_region(win):
    title = Text(Point(2, 4), "SELECT REGION")
    title.setSize(30)
    title.setFace("courier")
    title.setStyle("bold")
    title.draw(win)

    button_Arab, label_Arab = create_button(win, "Arab States", Point(1, 3), Point(3, 3.5))
    button_Asia, label_Asia = create_button(win, "Asia and the Pacific", Point(1, 2.5), Point(3, 3))
    button_Europe, label_Europe = create_button(win, "Eastern Europe & CentralAsia", Point(1, 2), Point(3, 2.5))
    button_LatinAmerica, label_LatinAmerica = create_button(win, "Latin American & Caribbean", Point(1, 1.5),
                                                                Point(3, 2))
    button_EastAfrica, label_EastAfrica = create_button(win, "East & Southern Africa", Point(1, 1), Point(3, 1.5))
    button_WestAfrica, label_WestAfrica = create_button(win, "West & Central Africa", Point(1, 0.5), Point(3, 1))


    while True:
        click_point = win.getMouse()

        if button_Arab.getP1().getX() < click_point.getX() < button_Arab.getP2().getX() and \
                button_Arab.getP1().getY() < click_point.getY() < button_Arab.getP2().getY():
            undrawbuttons(button_Arab, label_Arab,button_Asia, label_Asia,button_Europe, label_Europe, button_LatinAmerica, label_LatinAmerica,
                            button_EastAfrica, label_EastAfrica,button_WestAfrica, label_WestAfrica , title)
            return ("Arab States")

        elif button_Asia.getP1().getX() < click_point.getX() < button_Asia.getP2().getX() and \
                    button_Asia.getP1().getY() < click_point.getY() < button_Asia.getP2().getY():
            undrawbuttons(button_Arab, label_Arab, button_Asia, label_Asia, button_Europe, label_Europe,
                              button_LatinAmerica, label_LatinAmerica,
                              button_EastAfrica, label_EastAfrica, button_WestAfrica, label_WestAfrica, title)
            return ("Asia and the Pacific")

        elif button_Europe.getP1().getX() < click_point.getX() < button_Europe.getP2().getX() and \
                    button_Europe.getP1().getY() < click_point.getY() < button_Europe.getP2().getY():
            undrawbuttons(button_Arab, label_Arab, button_Asia, label_Asia, button_Europe, label_Europe,
                              button_LatinAmerica, label_LatinAmerica,
                              button_EastAfrica, label_EastAfrica, button_WestAfrica, label_WestAfrica, title)
            return ("Eastern Europe and Central Asia")

        elif button_LatinAmerica.getP1().getX() < click_point.getX() < button_LatinAmerica.getP2().getX() and \
                    button_LatinAmerica.getP1().getY() < click_point.getY() < button_LatinAmerica.getP2().getY():
            undrawbuttons(button_Arab, label_Arab, button_Asia, label_Asia, button_Europe, label_Europe,
                              button_LatinAmerica, label_LatinAmerica,
                              button_EastAfrica, label_EastAfrica, button_WestAfrica, label_WestAfrica, title)
            return ("Latin American and Caribbean")

        elif button_EastAfrica.getP1().getX() < click_point.getX() < button_EastAfrica.getP2().getX() and \
                    button_EastAfrica.getP1().getY() < click_point.getY() < button_EastAfrica.getP2().getY():
            undrawbuttons(button_Arab, label_Arab, button_Asia, label_Asia, button_Europe, label_Europe,
                              button_LatinAmerica, label_LatinAmerica,
                              button_EastAfrica, label_EastAfrica, button_WestAfrica, label_WestAfrica, title)
            return ("East and Southern Africa")

        elif button_WestAfrica.getP1().getX() < click_point.getX() < button_WestAfrica.getP2().getX() and \
                    button_WestAfrica.getP1().getY() < click_point.getY() < button_WestAfrica.getP2().getY():
            undrawbuttons(button_Arab, label_Arab, button_Asia, label_Asia, button_Europe, label_Europe,
                              button_LatinAmerica, label_LatinAmerica,
                              button_EastAfrica, label_EastAfrica, button_WestAfrica, label_WestAfrica, title)
            return ("West and Central Africa")


def inputTitle(win):
    text = Text(Point(2, 3.5), "CHOOSE A TITLE")
    text.setSize(25)
    text.setFace("courier")
    text.setStyle("bold")
    text.draw(win)

    text2 = Text(Point(2, 1.5), "If no title provided App will set Default title.")
    text2.setSize(14)
    text2.setFace("courier")
    text2.draw(win)
    button_Done, label_Done = create_button(win, "Done", Point(1, 2.5), Point(3, 3))

    title = Entry(Point(2, 2), 50)
    title.draw(win)

    while True:
        click_point = win.getMouse()
        if button_Done.getP1().getX() < click_point.getX() < button_Done.getP2().getX():
            undrawbuttons(button_Done, label_Done, text, text2, title)
            return title.getText()

def population_piechart(df,region, title ):
    selected_region = region
    df_region = df[df['SUMMARY INDICATORS'] == selected_region]

    population_columns = ['Population aged 0-14, percent', 'Population aged 15-24, percent',
                          'Population aged 25-59, percent', 'Population aged 60+, percent']
    df_population = df_region[population_columns]

    values =  df_population.iloc[0].tolist()
    colors = ['b', 'g', 'm', 'c']
    labels = ['Population aged  0-14', 'Population aged 15-24', 'Population aged 25-59', 'Population aged 60+']

    plt.pie(values, colors=colors, labels=labels, autopct='%1.1f%%',
            counterclock=False, shadow=False)

    if title == "":
        title = 'Distribution Population per Age Group of ' + region
    plt.title(title)

    plt.show()


def education_graph(df, region, title ):
    selected_region = region
    df_region = df[df['SUMMARY INDICATORS'] == selected_region]

    education_columns = ['Total net enrolment rate, primary education, percent',
                         'Total net enrolment rate, lower secondary education, percent',
                         'Toal net enrolment rate, upper secondary education, percent']
    df_education = df_region[education_columns]
    df_education.columns = ['Primary Education', 'Lower Secondary Education', 'Upper Secondary Education']

    df_education_transposed = df_education.transpose()


    ax = df_education_transposed.plot(kind='bar', stacked=True, figsize=(10, 6))

    ax.set_xlabel('Education Level')
    ax.set_ylabel('Enrollment Rate (%)')

    if title == "" :
        title = f'Net Enrollment Rate by Education Level in {region}'

    plt.title(title)
    ax.set_title(title)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.45)

    # Show the plot
    plt.show()

def life_expectancy(data, title = ""):
    barWidth = 0.6

    plt.bar(data['SUMMARY INDICATORS'], data['life expectancy at birth rate male'], color='darkred', edgecolor='black',
            width=barWidth, label='Male')
    plt.bar(data['SUMMARY INDICATORS'], data['life expectancy at birth rate female'],
            bottom=data['life expectancy at birth rate male'], color='darkorange', edgecolor='black', width=barWidth,
            label='Female')

    plt.xlabel('Regions')
    plt.ylabel('Life Expectancy of Females and Males')

    if title  =="":
        title = f'Stacked chart bar of life expectancy by regions'

    plt.title(title)
    plt.legend()

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.45)

    plt.show()


def total_population(data, title ):

    regions = data['SUMMARY INDICATORS']
    totalpop = data['Total population in millions']

    plt.figure(facecolor='lightgrey')

    plt.bar(regions, totalpop)

    plt.xlabel('Regions')
    plt.ylabel('Total Population')

    if title == "":
        title = 'Population by Regions Bar Chart'
    plt.title(title)

    bars = plt.bar(regions, totalpop, color=['darkred'])

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.45)

    plt.show()

def CountryMenu(win):
    title = Text(Point(2, 4), "SELECT COUNTRY")
    title.setSize(30)
    title.setStyle("bold")
    title.setFace("courier")
    title.draw(win)


    button_Argentina, label_Argentina = create_button(win, "Argentina", Point(1, 3), Point(3, 3.5))
    button_Brazil, label_Brazil = create_button(win, "Brazil", Point(1, 2.5), Point(3, 3))
    button_France, label_France = create_button(win, "France", Point(1, 2), Point(3, 2.5))
    button_India, label_India = create_button(win, "India", Point(1, 1.5), Point(3, 2))
    button_Russia, label_Russia = create_button(win, "Russia", Point(1, 1), Point(3, 1.5))
    button_China, label_China = create_button(win, "China", Point(1, 0.5), Point(3, 1))

    while True:
        click_point = win.getMouse()

        if button_Argentina.getP1().getX() < click_point.getX() < button_Argentina.getP2().getX() and \
                button_Argentina.getP1().getY() < click_point.getY() < button_Argentina.getP2().getY():
            undrawbuttons(button_Argentina, label_Argentina, button_Brazil, label_Brazil, button_France, label_France,
                          button_India, label_India, button_Russia, label_Russia, button_China, label_China, title)
            return "Argentina"

        elif button_Brazil.getP1().getX() < click_point.getX() < button_Brazil.getP2().getX() and \
                button_Brazil.getP1().getY() < click_point.getY() < button_Brazil.getP2().getY():
            undrawbuttons(button_Argentina, label_Argentina, button_Brazil, label_Brazil, button_France, label_France,
                          button_India, label_India, button_Russia, label_Russia, button_China, label_China, title)
            return "Brazil"

        elif button_France.getP1().getX() < click_point.getX() < button_France.getP2().getX() and \
                button_France.getP1().getY() < click_point.getY() < button_France.getP2().getY():
            undrawbuttons(button_Argentina, label_Argentina, button_Brazil, label_Brazil, button_France, label_France,
                          button_India, label_India, button_Russia, label_Russia, button_China, label_China, title)
            return "France"

        elif button_India.getP1().getX() < click_point.getX() < button_India.getP2().getX() and \
                button_India.getP1().getY() < click_point.getY() < button_India.getP2().getY():
            undrawbuttons(button_Argentina, label_Argentina, button_Brazil, label_Brazil, button_France, label_France,
                          button_India, label_India, button_Russia, label_Russia, button_China, label_China, title)
            return "India"

        elif button_Russia.getP1().getX() < click_point.getX() < button_Russia.getP2().getX() and \
                button_Russia.getP1().getY() < click_point.getY() < button_Russia.getP2().getY():
            undrawbuttons(button_Argentina, label_Argentina, button_Brazil, label_Brazil, button_France, label_France,
                          button_India, label_India, button_Russia, label_Russia, button_China, label_China, title)
            return "Russia"

        elif button_China.getP1().getX() < click_point.getX() < button_China.getP2().getX() and \
                button_China.getP1().getY() < click_point.getY() < button_China.getP2().getY():
            undrawbuttons(button_Argentina, label_Argentina, button_Brazil, label_Brazil, button_France, label_France,
                          button_India, label_India, button_Russia, label_Russia, button_China, label_China, title)
            return "China"

def country_population(df, country, title):
    df_country = df[df['Country/Territory'] == country]

    population_columns = ['1970 Population','1980 Population','1990 Population',
                          '2000 Population','2010 Population','2015 Population','2020 Population',
                          '2022 Population',]
    df_country = df_country[population_columns]

    values = df_country.iloc[0].tolist()
    values2 = [1970,1980,1990,2000,2010,2015,2020,2022]

    plt.plot(values2, values, marker='o')

    plt.xlabel('Year')
    plt.ylabel('Population')

    if title == "":
        title = f'Population Over Time - {country}'
    plt.title(title)

    plt.title(title)

    # Define a custom formatting function to avoid scinetific notation in plots
    def custom_formatter(value, _):
        return f"{value:.0f}"
    plt.gca().xaxis.set_major_formatter(FuncFormatter(custom_formatter))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
    plt.yticks(rotation=45, ha='right')

    plt.show()

def End_or_Repeat(win):
    title = Text(Point(2, 1.5), "SELECTED PLOT HAS BEEN PLOTTED")
    title.setSize(20)
    title.setStyle("bold")
    title.setFace("courier")
    title.draw(win)
    button_start, label_start = create_button(win, "Back to Menu", Point(1, 3), Point(3, 3.5))
    button_end, label_end = create_button(win, "Quit", Point(1, 2.5), Point(3, 3))

    while True:
        click_point = win.getMouse()
        if button_start.getP1().getX() < click_point.getX() < button_start.getP2().getX() and \
                button_start.getP1().getY() < click_point.getY() < button_start.getP2().getY():
            undrawbuttons(button_start, label_start, button_end, label_end, title)
            return 1

        elif button_end.getP1().getX() < click_point.getX() < button_end.getP2().getX() and \
                button_end.getP1().getY() < click_point.getY() < button_end.getP2().getY():
            undrawbuttons(button_start, label_start, button_end, label_end, title)
            return 2

def main():
    win = GraphWin("Regions Insights", 500, 500)
    win.setCoords(0.0, 0.0, 4.0, 4.5)
    win.setBackground('white')

    demographics_table, humancapital_table, country_data = LoadData()

    startButton(win)

    while True:
        selection = DisplayMenu(win)

        if selection == "region":
            plot, region = RegionMenu(win)

            if plot == 1:
                title = inputTitle(win)
                population_piechart(demographics_table, region, title)

            if plot == 2:
                title = inputTitle(win)
                education_graph(humancapital_table , region, title)

            if plot == 3:
                title= inputTitle(win)
                life_expectancy(demographics_table, title)

            if plot == 4:
                title = inputTitle(win)
                total_population(demographics_table, title)

        elif selection == "country":
            country = CountryMenu(win)
            title = inputTitle(win)
            country_population(country_data , country, title)



        value = End_or_Repeat(win)

        if value ==1:
            continue
        elif value == 2:
            break


main()

