import os
from dotenv import load_dotenv

load_dotenv()

# tester_key = 'VAR_1'
# tester_value = os.getenv(tester_key)

# print("Value of 'VAR_1' environment variable is: " + str(tester_value))



tester_value_2 = os.getenv('VAR_1')

print(tester_value_2) 