import streamlit as st

teksti=st.text_input("Ju lutem shenoni tekstin tuaj ")

def conv_list(teksti):
    teksti_conv=teksti.split()
    print(teksti_conv)

lista = []
lista.append(conv_list(teksti))


if st.button("Kthe listen "):
    st.write(teksti)
else:
    st.write("")


def conv_lower(lista):
    lower=[]
    for i in lista:     
        lower.append(i.lower)
    print(lower)
lista_lower = print(conv_lower(lista))

if st.button(" lower "):
    st.write(lista_lower)
else:
    st.write("")

def lista_count(lista):
    count=0
    for i in lista:
        count += 1
    print(count)
numri = lista_count(lista)

if st.button(" Nr "):
    st.write(numri)
else:
    st.write("")