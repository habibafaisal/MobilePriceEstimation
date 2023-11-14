import re
import time
import requests
from bs4 import BeautifulSoup
import csv

# url = 'https://www.olx.com.pk/karachi_g4060695/mobile-phones_c1453'
# url = 'https://www.olx.com.pk/items/q-samsung-s20-gb?page=1'
# url = "https://www.olx.com.pk/items/q-samsung-s20-gb"
# url = "https://www.olx.com.pk/items/q-samsung-note-8-gb"
# url = "https://www.olx.com.pk/items/q-samsung-note-8-gb?page=1"

headers = {

    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

import os.path

filename ='olx_data.csv'
file_exists = os.path.isfile(filename)

# columns = ['Brand', 'Model', 'Condition', 'Location', 'Price', 'Description', 'RAM', 'ROM']
with open(filename, 'a+', newline='', encoding="utf-8") as csvfile:
    columns = ['Brand', 'Model', 'Condition', 'Location', 'Price', 'Description', 'RAM', 'ROM']
    writer = csv.writer(csvfile, delimiter=',')
    if not file_exists:
        writer.writerow(columns)
    # zipped_list = zip(brandsList, titlesList, conditionsList, locationsList, pricesList, finalDescription)
    # writer.writerow(columns)
    #writer.writerows(zipped_list)

# listOfMobiles = ["samsung-a-30",
#                         "samsung-a-52",
#                         "samsung-a-72",
#                         "samsung-j-6",
#                         "samsung-a-53",
#                         "samsung-note-10",
#                         "samsung-s-10",
#                         "samsung-note-8",
#                         "samsung-a-23",
#                         "samsung-a-13",
#                         "samsung-note-9",
#                         "samsung-note-5",
#                         "samsung-note-3",
#                         "samsung-note-7",
#                         "samsung-note-4",
#                         "samsung-s-9",
#                         "samsung-s-8",
#                         ]
#
# brand = "Samsung"

listOfMobiles = ["infinix-hot-12",
                        "infinix-note-11",
                        "infinix-zero-8",
                        "infinix-note-10",
                        "infinix-note-7",
                        "infinix-note-8",
                        "infinix-hot-10",
                        "infinix-hot-11",
                        "infinix-hot-9",
                        "infinix-hot-10-play",
                        "infinix-note-12",
                        "infinix-smart-6",
                        "infinix-zero-5",
                        "infinix-s-5",
                        ]

brand = "Infinix"

for mobile in range(len(listOfMobiles)):

    for i in range(0, 5):
        model = listOfMobiles[mobile]
        url = "https://www.olx.com.pk/items/q-" + model + "-gb?page=" + str(i)


        r = requests.get(url, headers=headers)

        extractedLinkList = []

        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')

            for link in soup.find_all('a',attrs={'href': re.compile("^/item/")}):

                linkExtracted = "https://www.olx.com.pk"+link.get('href')
                extractedLinkList.append(linkExtracted)
                print(linkExtracted)
                print("--------------------------------------------------------")

        print("Length of the list is : ", len(extractedLinkList))
        extractedLinkList = list(dict.fromkeys(extractedLinkList))

        titlesList = []
        locationsList = []
        timesList = []
        brandsList = []
        pricesList = []
        conditionsList = []
        descriptionsList = []
        rows = []

        for i in range(len(extractedLinkList)):
            print(extractedLinkList[i])
            req = requests.get(extractedLinkList[i], headers=headers)
            print(i)
            if req.status_code == 200:
                html = req.text
                soup = BeautifulSoup(html, 'lxml')
                title = soup.find('h1')
                if title is not None:
                    title_text = title.text.strip()
                    print("**")
                    print('title')

                    print(model)
                    titlesList.append(model)
                    print("**")
                    print("--------------------------------------------------------")

                location = soup.find("span", {"aria-label": "Location"})
                if location is not None:
                    location_text = location.text.strip()
                    print("**")
                    print('Location')

                    print(location_text)
                    locationsList.append(location_text)
                    print("**")
                    print("--------------------------------------------------------")

                time = soup.find("span", {"aria-label": "Creation date"})
                if time is not None:
                    time_text = time.text.strip()
                    print("**")
                    print('Time')

                    print(time_text)
                    timesList.append(time_text)
                    print("**")
                    print("--------------------------------------------------------")

                div = soup.find_all('div', attrs={'class': '_241b3b1e'})

                for my_tag in soup.find_all(class_="_241b3b1e"):
                    print(my_tag.text)
                    start = 'Brand'
                    end = 'Price'
                    s = my_tag.text
                    print("**")
                    print("BRAND")
                    print(brand)
                    brandsList.append(brand)


                    # print(s[s.find(start) + len(start):s.rfind(end)])
                    # brandsList.append(s[s.find(start) + len(start):s.rfind(end)])
                    print("**")
                    print("--------------------------------------------------------")

                    start = 'Price'
                    end = 'Condition'
                    s = my_tag.text
                    print("**")
                    print("Price")

                    print(s[s.find(start) + len(start):s.rfind(end)])
                    pricesList.append(s[s.find(start) + len(start):s.rfind(end)])
                    print("**")
                    print("--------------------------------------------------------")

                    print("**")
                    print("Condition")

                    try:

                        if(my_tag.text.split("Condition", 1)[1] != "Used"):
                            print("Condition is : 9")
                            conditionsList.append("9")
                        else:
                            print("Condition is : 10")
                            conditionsList.append("10")
                    except:
                        conditionsList.append("9")

                    # print(my_tag.text.split("Condition", 1)[1])
                    # conditionsList.append(my_tag.text.split("Condition", 1)[1])
                    print("**")
                    print("--------------------------------------------------------")

                description = soup.find("div", {"class": "_0f86855a"})
                if description is not None:
                    description_text = description.text.strip()
                    print("**")
                    print('Description')

                    print(description_text)
                    descriptionsList.append(description_text)
                    print("**")
                    print("--------------------------------------------------------")
                    print([titlesList[i]],[brandsList[i]])


        for i in range(len(extractedLinkList)):
            print("Titles")
            print(titlesList[i])
            print("")
            print("Location")
            print(locationsList[i])
            print("")
            print("Time")
            print(timesList[i])
            print("")
            print("Brand")
            print(brandsList[i])
            print("")
            print("Price")
            print(pricesList[i])
            print("")
            print("Condition")
            print(conditionsList[i])
            print("")
            print("Description")
            print(descriptionsList[i])
            print("")

            print("__")
            print("__")
            print("__")
            print("__")
            print("__")
            print("__")

        testingList = []
        anotherTestingList = []
        print("77777777777777777777777777777777777777777777777777")

        # for i in range(len(descriptionsList)):
        #     x = descriptionsList[i].split()
        #     testingList.append(x)
        #     print(x)

        for i in range(len(descriptionsList)):
            if "gb" in descriptionsList[i] or "Gb" in descriptionsList[i] or "GB" in descriptionsList[i]:
                anotherTestingList.append(descriptionsList[i])

            else:
                anotherTestingList.append("0")


        print("99999999999999999999999999999999999999999")
        for i in range(len(anotherTestingList)):
            print(" post is : ", i)

            print(anotherTestingList[i])
            print("99999999999999999999999999999999999999999")

        print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
        for i in range(len(anotherTestingList)):
            x = anotherTestingList[i].split()
            testingList.append(x)
            print(x)

        finalDescription = []
        for i in range(len(testingList)):
            desc = ""
            for j in range(len(testingList[i])):
                # print(len(testingList[i]))

                if "gb" in testingList[i][j] or "Gb" in testingList[i][j] or "GB" in testingList[i][j]:
                    print("Description no ", i)
                    # print(testingList[i][j - 1])
                    #
                    # print(testingList[i][j])
                    #
                    # # print(testingList[i][j + 1])
                    desc = desc + testingList[i][j - 1] + " " + testingList[i][j] + " "
                    print(desc)



                    # finalDescription[i].append(testingList[i][j - 1])
                    # finalDescription[i].append(testingList[i][j])
                    # finalDescription[i].append(testingList[i][j + 1])
            finalDescription.append(desc)
            # counter = counter + 1

        # for i in range(len(descriptionsList)):
        #     print(descriptionsList[i])
        #     print("----------------------------------------------------")
        #     descriptionsList[i] = [int(i) for i in descriptionsList[i].split() if i.isdigit()]
        #
        # print("-------------------------------------")
        # print("GENUINE!!!!!!")
        # print("----------------------------------")
        #
        # for i in range(len(finalDescription)):
        #     print("FINAL DESC : ", i)
        #     print(finalDescription[i])
        #     print("----------------------------------------------------")

        for i in range(len(finalDescription)):
            print(type(finalDescription[i]))
            # val = finalDescription[i]
            import re as regex

            num = regex.findall(r'\d+', finalDescription[i])

            # Remove duplicate values

            num = list(dict.fromkeys(num))
            print(finalDescription[i])
            print("----------------------------------------------------")
            finalDescription[i] = num

        # Remove duplicate values
        # finalDescription = list(dict.fromkeys(finalDescription))

        for i in range(len(finalDescription)):
            print("FINAL DESC : ", i)
            print(finalDescription[i])
            print("----------------------------------------------------")

        # using loop
        for i in range(0, len(finalDescription)):

            for j in range(len(finalDescription[i])):
                finalDescription[i][j] = int(finalDescription[i][j])

            # Printing modified list
            # print("Modified list is : " + str(finalDescription))

        for i in range(len(finalDescription)):

            x = sorted(finalDescription[i])
            print("SORTING SCENEZZZZZZ")
            print(x)
            finalDescription[i] = x

        ram = []
        rom = []

        for i in range(len(finalDescription)):

            if(len(finalDescription[i]) >= 2):
                rom.append(max(finalDescription[i]))

                # ram.append(min(finalDescription[i]))

                secondLastIndex = finalDescription[i].index(max(finalDescription[i])) - 1

                value = finalDescription[i][secondLastIndex]

                if(finalDescription[i][secondLastIndex] % 2 != 0 ):

                    value = 0

                ram.append(value)


            else:
                rom.append(0)
                ram.append(0)




        # Working on location

        newLocationList = []

        for i in range(len(locationsList)):
            x = locationsList[i].split(",")
            newLocationList.append(x)
            print("x printing")
            print(x)

        locationsList = []

        for i in range(len(newLocationList)):

            locationsList.append(newLocationList[i][len(newLocationList[i])-1])

        for i in range(len(locationsList)):
            locationsList[i] = locationsList[i][:-1]






        columns = ['Brand', 'Model', 'Condition', 'Location', 'Price', 'Description']
        with open('olx_data.csv', 'a+', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            zipped_list = zip(brandsList, titlesList, conditionsList, locationsList, pricesList, finalDescription, ram, rom)
            # writer.writerow(columns)
            writer.writerows(zipped_list)