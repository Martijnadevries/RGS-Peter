import streamlit as st
import numpy as np
import pandas as pd
import random
from PIL import Image
import os.path

#Latest update 3.0 | 10/05/2021

st.set_page_config(layout = 'wide')

filename = './gods_owned.csv'
file_exists = os.path.isfile(filename)

if file_exists:
    pass
else:
    base_gods = ['Ares', 'Artemis', 'Bellona', 'Guan Yu', 'Kukulkan', 'Neith', 'Nemesis', 'Ra', 'Thor', 'Ymir']
    base_file = pd.Series(base_gods, index = None)
    base_file.to_csv('./gods_owned.csv', index = False)

gods_owned = pd.read_csv('./gods_owned.csv').squeeze().to_list()

def main():
    god_list = ['Arachne', 'Awilix', 'Bakasura', 'Bastet', 'Camazotz', 'Da Ji', 'Fenrir', 'Hun Batz', 'Kali', 'Loki', 'Mercury', 'Ne Zha', 'Pele', 'Ratatoskr', 'Ravana', 'Serqet', 'Set', 'Susano', 'Thanatos', 'Tsukuyomi', 'Artio', 'Athena', 'Bacchus', 'Cabrakan', 'Cerberus', 'Cthulhu', 'Fafnir', 'Ganesha', 'Geb', 'Jormungandr', 'Khepri', 'Kumbhakarna', 'Kuzenbo', 'Sobek', 'Sylvanus', 'Terra', 'Xing Tian', 'Yemoja', 'Ah Muzen Cab', 'Anhur', 'Apollo', 'Cernunnos', 'Chernobog', 'Chiron', 'Cupid', 'Danzaburou', 'Hachiman', 'Heimdallr', 'Hou Yi', 'Izanami', 'Jing Wei', 'Medusa', 'Rama', 'Skadi', 'Ullr', 'Xbalanque', 'Agni', 'Ah Puch', 'Anubis', 'Ao Kuang', 'Aphrodite', 'Baba Yaga', 'Baron Samedi', "Change", 'Chronos', 'Discordia', 'Eset', 'Freya', 'Hades', 'He Bo', 'Hel', 'Hera', 'Janus', 'Merlin', 'Nox', 'Nu Wa', 'Olorun', 'Persephone', 'Poseidon', 'Raijin', 'Scylla', 'Sol', 'The Morrigan', 'Thoth', 'Tiamat', 'Vulcan', 'Zeus', 'Zhong Kui', 'Achilles', 'Amaterasu', 'Chaac', 'Cu Chulainn', 'Erlang Shen', 'Gilgamesh', 'Hercules', 'Horus', 'King Arthur', 'Mulan', 'Nike', 'Odin', 'Osiris', 'Sun Wukong', 'Tyr', 'Vamana']
    smite_gods = pd.Series(god_list)
    smite_gods = smite_gods.sort_values(ignore_index = True)
    global gods_owned

    st.sidebar.title('Smite Random Generator')
    navigation_menu = st.sidebar.selectbox('Kies je optie', ['Select Gods', 'God List', 'Random Generator'])

    if navigation_menu == 'Select Gods':

        for god_name in smite_gods:
            columns_god_checkbox(god_name)

        gods_pool = pd.Series(data = gods_owned)
        gods_pool = gods_pool.sort_values(ignore_index = True)
        gods_pool.to_csv('./gods_owned.csv', index = False)
        
    elif navigation_menu == 'Random Generator':
        random_god_pick()

    elif navigation_menu == 'God List':
        god_list_show()
    
def columns_god_checkbox(god_name):
    columns1, columns2, columns3 = st.beta_columns((4, 2, 4))
    if god_name in gods_owned:
        checkbox_owned_gods = columns2.checkbox(god_name, key = god_name, value = True)
        if checkbox_owned_gods == False and god_name in gods_owned:
            gods_owned.remove(god_name)

    else:
        checkbox_unowned_gods = columns2.checkbox(god_name, key = god_name)
        if checkbox_unowned_gods == True and god_name not in gods_owned:
            gods_owned.append(god_name)

def random_god_pick():
    gods_amount = len(gods_owned)

    random_number = random.randint(0, (gods_amount - 1))
    random_selected_god = gods_owned[random_number]

    column1, column2, column3 = st.beta_columns(3)
    file_name = ('./' + random_selected_god + ".jpg")
    column3 = column2.image(Image.open(file_name), width = 350)

def god_list_show():
    columns1, columns2, columns3, columns4, columns5, columns6 = st.beta_columns(6)
    show_order_list = [0]

    n = 0
    while n < (len(gods_owned)-6):
        n += 6
        show_order_list.append(n)

    n = 1
    show_order_list.append(n)
    while n < (len(gods_owned)-6):
        n += 6
        show_order_list.append(n)

    n = 2
    show_order_list.append(n)
    while n < (len(gods_owned)-6):
        n += 6
        show_order_list.append(n)

    n = 3
    show_order_list.append(n)
    while n < (len(gods_owned)-6):
        n += 6
        show_order_list.append(n)

    n = 4
    show_order_list.append(n)
    while n < (len(gods_owned)-6):
        n += 6
        show_order_list.append(n)

    n = 5
    show_order_list.append(n)
    while n < (len(gods_owned)-6):
        n += 6
        show_order_list.append(n)
 
    gods_owned_ordered = []
    for i in show_order_list:
        gods_owned_ordered.append(gods_owned[i])

    index_1 = int(len(gods_owned) / 6 + 1)
    index_2 = int((len(gods_owned) / 6) * 2 + 1)
    index_3 = int((len(gods_owned) / 6 ) * 3 + 1)
    index_4 = int((len(gods_owned) / 6 ) * 4 + 1)
    index_5 = int((len(gods_owned) / 6 ) * 5 + 1)
    index_6 = len(gods_owned)

    if len(gods_owned) % 6 == 0:
        index_1 = index_1 - 1
        index_2 = index_2 - 1
        index_3 = index_3 - 1
        index_4 = index_4 - 1
        index_5 = index_5 - 1

    elif len(gods_owned) % 6 == 2:
        index_2 = index_2 + 2

    elif len(gods_owned) % 6 == 3:
        index_3 = index_3 + 2
   
    elif len(gods_owned) % 6 == 4:
        index_4 = index_4 + 1

    for god in gods_owned_ordered[0:index_1]:
        file_name_owned = ('./' + god + ".jpg")
        columns1.image(Image.open(file_name_owned), width = 115)

    for god in gods_owned_ordered[index_1: index_2]:
        file_name_owned2 = ('./' + god + ".jpg")
        columns2.image(Image.open(file_name_owned2), width = 115)

    for god in gods_owned_ordered[index_2: index_3]:
        file_name_owned3 = ('./' + god + ".jpg")
        columns3.image(Image.open(file_name_owned3), width = 115)

    for god in gods_owned_ordered[index_3: index_4]:
        file_name_owned4 = ('./' + god + ".jpg")
        columns4.image(Image.open(file_name_owned4), width = 115)

    for god in gods_owned_ordered[index_4: index_5]:
        file_name_owned5 = ('./' + god + ".jpg")
        columns5.image(Image.open(file_name_owned5), width = 115)

    for god in gods_owned_ordered[index_5: index_6]:
        file_name_owned6 = ('./' + god + ".jpg")
        columns6.image(Image.open(file_name_owned6), width = 115) 

if __name__ == '__main__':
    main()
