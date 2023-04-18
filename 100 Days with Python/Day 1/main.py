# text formatting in f strings
text = "Hello World"
# _<20 to right
# _>20 to left
# ·^20 between
print(f'{text:_<20}')
print(f'{text:_>20}')
print(f'{text:·^20}')