import pandas as pd

# Step 1: Create dataset
data = {
    "FullName": [
        " raj patel ",
        "AMIT SHAH",
        "Neha Mehta ",
        " priya desai",
        "KARAN SHAH"
    ],
    "City": [
        "ahmedabad",
        "SURAT",
        "Vadodara",
        "AHMEDABAD",
        "surat"
    ],
    "Email": [
        " RAJ@GMAIL.COM ",
        "amit@yahoo.com",
        "NEHA@GMAIL.COM",
        "priya@gmail.com ",
        " KARAN@OUTLOOK.COM"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Remove extra spaces
df["FullName"] = df["FullName"].str.strip()
df["City"] = df["City"].str.strip()
df["Email"] = df["Email"].str.strip()

# Step 3: Standardize capitalization
df["FullName"] = df["FullName"].str.title()
df["City"] = df["City"].str.title()
df["Email"] = df["Email"].str.lower()

# Step 4: Split full name
df["FirstName"] = df["FullName"].str.split().str[0]
df["LastName"] = df["FullName"].str.split().str[-1]

# Step 5: Extract email domain
df["EmailDomain"] = df["Email"].str.split("@").str[-1]

# Step 6: Identify Gmail users
df["IsGmail"] = df["Email"].str.endswith(
    "@gmail.com",
    na=False
)

# Step 7: Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Step 8: Find customers from Ahmedabad
ahmedabad_customers = df[
    df["City"].str.contains("Ahmedabad", case=False, na=False)
]

print("\nCustomers from Ahmedabad:")
print(ahmedabad_customers)

# Step 9: Export the cleaned dataset
df.to_csv("cleaned_customers.csv", index=False)

print("\nCustomer report saved successfully!")