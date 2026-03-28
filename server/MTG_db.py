import sqlite3

#Connecting / creating a database and the coursor is editing the actions
connection = sqlite3.connect("MTG.db")
coursor = connection.cursor()


sql_command = """CREATE TABLE Users (User_id int primary key, 
					Email varchar(50), 
                    Username varchar(50), 
                    Phone_number varchar(20), 
                    Password varchar(24))"""
sql_command_Deck = """CREATE TABLE Deck (Inventory_ID INT PRIMARY KEY)"""
sql_command_Cards = """create table Cards (Card_ID varchar(10) primary key, 
					Rarity char,
                    Set_Release varchar(50),
                    Count int, 
                    Price decimal (8,2))"""


sql_command_Deck_Cards = """create table Deck_cards(Inventory_ID int,
 					Card_ID varchar(10), 
                     primary key(Inventory_ID, Card_ID))"""
sql_command_Bidder = """create table Bidder(Bidder_ID varchar(50) primary key, 
					User_id int, 
                    Inventory_ID int, 
                    Card_ID varchar(10), 
                    constraint user_num foreign key(User_id) references Users(User_id),
                    constraint inventory_num foreign key(Inventory_ID) references Deck(Inventory_ID),
                    constraint cardType foreign key(Card_ID) references Cards (Card_ID))"""
sql_command_Transactions = """create table Transactions(Transaction_ID int primary key, 
					User_id int, 
                    Price decimal (8,2), 
                    Card_ID varchar(10), 
					constraint user_num_2 foreign key(User_id) references Users(User_id),
					constraint cardType_2 foreign key(Card_ID) references Cards (Card_ID));"""
# running SQL code 
coursor.execute(sql_command_Transactions)
connection.close()