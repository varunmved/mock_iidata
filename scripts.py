import pandas as pd

conn = "injuries.db"

a = pd.read_sql("SELECT * FROM Injury",conn)

print(a)
