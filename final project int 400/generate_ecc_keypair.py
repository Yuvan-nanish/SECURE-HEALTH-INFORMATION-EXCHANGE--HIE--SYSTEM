import json

# Assuming private_key and public_key are generated and stored in variables
private_key = 31593919573514085932370866723620508161421357103475599255908288591746784690644

public_key = {
    "x": 21306267299943488838229917687483860271965272823504237776293761710765041128368,
    "y": 66354118438501932162927582552887512470578084757507302811270413143839033738974
}

# Save private key to file
with open('keys/private_key.pem', 'w') as private_file:
    private_file.write(str(private_key))

# Save public key to file
with open('keys/public_key.pem', 'w') as public_file:
    json.dump(public_key, public_file)

print("Keys saved successfully.")
