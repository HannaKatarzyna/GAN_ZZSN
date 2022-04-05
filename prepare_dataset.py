#%% IMPORTS
import re
import os

#%% lista plikow
# na razie sciezka lokalna, trzeba zmienic data_path
data_path = r'D:\studia mgr EIM\ZZSN\thecarconnectionpicturedataset'
listOfFiles = os.listdir(data_path)

#%% opcja 1 - rozdzielenie na typy np. SUV

car_types= ['Van','Pickup','Station Wagon','4dr','3dr','2dr','SUV','Convertible']
# reszta to 'nan'
car_dictionary = dict.fromkeys(car_types)
for type_of_car in car_types:
    str_match = [s for s in listOfFiles if type_of_car in s]
    car_dictionary[type_of_car] = len(str_match)

print(car_dictionary)
print(sum(car_dictionary.values()))

#missing_car=[s for s in listOfFiles if not type_of_car in s]

#%% opcja 2 - rozdzielenie na konkretne modele samochodow, nie tylko marki

list_index = [re.search(r"[0-9]{4}",x).span() for x in listOfFiles]  # nazwy modeli koncza sie w momencie wystepowania liczby o 4 cyfrach co odpowiada rocznikowi samochodu
car_types= [listOfFiles[i][:list_index[i][0]-1] for i in range(len(listOfFiles)) ] #znajdz pozycje, gdzie wystepuja 4 cyfry (i odejmij znak _)
car_types=list(set(car_types)) # modele nie moga sie powtarzac
car_types.sort() # i niech beda posegregowane alfabytycznie
print("ile modeli samochodow: ", len(car_types))
print(car_types)

car_dictionary = dict.fromkeys(car_types)
for type_of_car in car_types:
    str_match = [s for s in listOfFiles if type_of_car in s]
    car_dictionary[type_of_car] = len(str_match)

#%% test
print(car_dictionary['smart_fortwo'])
print(max(car_dictionary.values()))

fin_max = max(car_dictionary, key=car_dictionary.get)
print("Maximum value is for:",fin_max)

ready_list= []
for car, number in car_dictionary.items():
    if number >=400:
        ready_list.append(car)

print(ready_list)
print(len(ready_list))

#%% opcja 3 - rozdzielenie tylko na marki samochodow

list_index = [x.find("_") for x in listOfFiles]
car_brands= [listOfFiles[i][:list_index[i]] for i in range(len(listOfFiles)) ]

car_brands=list(set(car_brands)) # modele nie moga sie powtarzac
car_brands.sort() # i niech beda posegregowane alfabytycznie
print("ile marek samochodow: ", len(car_brands))
print(car_brands)

ready_list= []
for brand_of_car in car_brands:
    str_match = [s for s in listOfFiles if brand_of_car in s]
    ready_list.append(str_match)
    print(brand_of_car, " : ", len(str_match))

# %%
