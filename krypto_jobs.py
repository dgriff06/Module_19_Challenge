import streamlit as st 
from ethereum import generate_accounts, get_balance, send_transaction
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))

account = generate_accounts(web3)

st.markdown("# KryptoJobs2Go")
st.text("\n")
st.sidebar.markdown("## Account Address")
st.sidebar.write(account.address)

st.text("\n")
st.sidebar.markdown("## Balance")
ether_balance = get_balance(web3, account.address)
st.sidebar.write(ether_balance)

candidate_database = {
    "ash":["Ash","0xFFAF907686C1Efa931C634ec80D16BFDE839EA43","4.3", .20, "Images/ash.jpeg"],
    "jo":["Jo","0x428c6Ca3AA3887803220f4A211b62bF00499622e","5.0", .33, "Images/jo.jpeg"],
    "kendall":["Kendall","0x9bf62517a6077b1B2f32aA4d6d56977B53399368", "4.7", .19, "Images/kendall.jpeg"],
    "lane":["Lane","0x129ab4d8A87c6c6E3c3107EbB83789879eA403e4","4.1", .17, "Images/lane.jpeg"]
}

people = ["ash","jo","kendall","lane"]


def get_person():
    db_list = list(candidate_database.values())
    
    for x in range(len(people)):
        st.image( db_list[x][4], width = 200)
        
        st.write("Name: ", db_list[x][0])
        st.write("Address: ", db_list[x][1])
        st.write("Rating: ", db_list[x][2])
        st.write("Hourly Rate per ETH: ", db_list[x][3])
        st.write("\n")
        

st.markdown("# Candidate Database")
st.markdown("## Hire A Fintech Professional!")
st.text("\n")
st.text("\n")

person = st.sidebar.selectbox("Select a Person", people)
st.sidebar.markdown("## Person Name and Price")
name_of_person = candidate_database[person][0]
address_of_person = candidate_database[person][1]
rating_of_person = candidate_database[person][2]
rate_of_person = candidate_database[person][3]


hours = st.sidebar.number_input("How man hours would you like to hire for?")
wage = hours * rate_of_person
st.sidebar.write(wage)



if wage <= ether_balance:
    new_balance = float(ether_balance) - float(wage)
    st.sidebar.write(f"You can hire {name_of_person} for {wage} ether")
    get_person()
else:
    st.sidebar.write(f"You cannot hire {name_of_person} for {wage} ether")
    get_person()
    
    
st.text("\n")


if st.button("Hire a Person"):
    transaction_hash = send_transaction(web3, account, address_of_person, wage)
    st.text("\n")
    st.text("\n")
    st.markdown("## Transaction Hash")
    st.write(transaction_hash)

