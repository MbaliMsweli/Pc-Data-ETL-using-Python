import pandas as pd
import re

df=pd.read_csv("pc_data.csv", sep=";")
print(df)

print(df.columns)


##create function called clean_phone_number, to clean the phone number and if theres no country code exists use a default one +1
def clean_phone_number(phone, default_country_code="+1"):
   
   ##check if phone number is empty and return None
    if pd.isna(phone):
        return None
## convert phone number to a string,bacause cleaning only works on text
    phone = str(phone)

    # Remove extensions (x123, ext123)
    phone = re.split(r"[xX]|ext", phone)[0]

    # Removes brackets,dashes,dots,spaces and Keep only digits
    digits = re.sub(r"\D", "", phone)

    # checks if the number starts with 2 zeros  and removes them
    if digits.startswith("00"):
        digits = digits[2:]

    # checks if the number has more than 10 digits that means it already has country code so add a + infront
    if len(digits) > 10:
        return f"+{digits}"

    # checks if number is local and has 10 digits then add default country code(+10)
    if len(digits) == 10:
        return f"{default_country_code}{digits}"

## Take each phone number in the column (Customer Contact Number) and apply cleaning 
df["Customer Contact Number"] = df["Customer Contact Number"].apply(clean_phone_number)

## now print the first 10 rows of the column we were cleaning
print(df["Customer Contact Number"].head(5))


##Define date  in the dataset
date_columns = ["Purchase Date", "Ship Date"]

## Converts Date Columns into Date type
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors = "coerce")

print(df[date_columns].dtypes)

df.to_csv("silver_pc_data.csv", index=False)

print("silver layer created")