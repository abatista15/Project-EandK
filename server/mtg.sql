Create DATABASE MTG;

CREATE TABLE IF NOT EXISTS public."Users"
(
    "User_Id" uuid NOT NULL,
    "Username" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "Phone_number" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "Password" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Users_pkey" PRIMARY KEY ("User_Id")
)
CREATE TABLE IF NOT EXISTS public."User_deck"
(
    "Group_ID" uuid NOT NULL,
    "User_ID" uuid NOT NULL,
    "Inventory_ID" uuid NOT NULL,
    CONSTRAINT "User_deck_pkey" PRIMARY KEY ("Group_ID"),
    CONSTRAINT "FK_Inventory_ID" FOREIGN KEY ("Inventory_ID")
        REFERENCES public."Deck" ("Inventory_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_User_ID" FOREIGN KEY ("User_ID")
        REFERENCES public."Users" ("User_Id") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
CREATE TABLE IF NOT EXISTS public."Deck"
(
    "Inventory_ID" uuid NOT NULL,
    "Deck_Owner" uuid NOT NULL,
    CONSTRAINT "Deck_pkey" PRIMARY KEY ("Inventory_ID"),
    CONSTRAINT "Deck_Owner_FK" FOREIGN KEY ("Deck_Owner")
        REFERENCES public."Users" ("User_Id") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
CREATE TABLE IF NOT EXISTS public."Deck_Cards"
(
    "Unique_ID" uuid NOT NULL,
    "Inventory_ID" uuid NOT NULL,
    "Card_ID" uuid NOT NULL,
    CONSTRAINT "Deck_Cards_pkey" PRIMARY KEY ("Unique_ID"),
    CONSTRAINT "FK_Card_ID" FOREIGN KEY ("Card_ID")
        REFERENCES public."Cards" ("Card_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_Inventory_ID" FOREIGN KEY ("Inventory_ID")
        REFERENCES public."Deck" ("Inventory_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

CREATE TABLE IF NOT EXISTS public."Cards"
(
    "Card_ID" uuid NOT NULL,
    "Rarity" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "Set_Release" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "Count" integer NOT NULL,
    "Commanders" character varying(50) COLLATE pg_catalog."default",
    "Price" numeric(1000,2),
    CONSTRAINT "Cards_pkey" PRIMARY KEY ("Card_ID")
)
CREATE TABLE IF NOT EXISTS public."Bidding_Session"
(
    "Bidding_ID" uuid NOT NULL,
    "User_ID" uuid NOT NULL,
    "Unique_ID" uuid NOT NULL,
    "Bidding_Price" numeric(1000,2) NOT NULL,
    CONSTRAINT "Bidding_Session_pkey" PRIMARY KEY ("Bidding_ID"),
    CONSTRAINT "FK_User_ID" FOREIGN KEY ("User_ID")
        REFERENCES public."Users" ("User_Id") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "Unique_ID_FK" FOREIGN KEY ("Unique_ID")
        REFERENCES public."Deck_Cards" ("Unique_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
CREATE TABLE IF NOT EXISTS public."Transactions"
(
    "Transaction_ID" uuid NOT NULL,
    "Bidder_ID" uuid NOT NULL,
    "Bidding_Price" numeric(1000,2) NOT NULL,
    CONSTRAINT "Transactions_pkey" PRIMARY KEY ("Transaction_ID"),
    CONSTRAINT "FK_Bidder_ID" FOREIGN KEY ("Bidder_ID")
        REFERENCES public."Bidding_Session" ("Bidding_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)