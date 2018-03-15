import gdax

# GDAX Params
passphrase = "vniohy1goai"
key = "38983fb513dd8b9c75a723ff80cc2be2"
b64secret = "9ogGMrNdE8i8WRz49CDJdvno+YsHTCHM7b6K+Us3vkmDhjApo9QDG2nLXBwBkMrY9Leul23lk3w1/KrFl5VstQ=="

# Auth Client
auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase)

# Use the sandbox API (requires a different set of API access credentials)
auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase,
                                  api_url="https://api-public.sandbox.gdax.com")

