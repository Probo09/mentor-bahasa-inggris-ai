if True:
    # logika program, proses yang lain
    print("contoh penggunaan if True, maka blok kode ini akan selalu dijalankan")

# 10 > 9 -> True / False
# 10 == 9 -> True / False
# 10 < 9 -> True / False


# if else statement
model_name:str = "gemini-3.5-flash"
if model_name == "gemini-3.5-flash":
    print("Sistem Agentic: Mengaktifkan mode Gemini 3.5 Flash...")
else:
    print("Sistem Agentic: Model tidak dikenali.")  

# if elif  elif else statement
price:int = 3000
service_tier:str = ""


# price diantara 1000 dan 2000 -> service tier itu adalah basic
# price diantara 2000 dan 5000 -> service tier itu adalah premium
# apabila price diatas 5000 -> service tier itu adalah platinum
# apabila diluar ini -> service tier itu adalah free

if price >= 1000 and price <= 2000:
    service_tier = "basic"
elif price >= 2000 and price <= 5000:
    service_tier = "premium"
elif price > 5000:
    service_tier = "platinum"
else:
    service_tier = "free"   

print(service_tier)

service_label:str = ""
match service_tier:
    case "basic":
        service_label = "Basic"
    case "premium": 
        service_label = "Premium"
    case "platinum":            
        service_label = "Platinum"
    case "free":
        service_label = "Free"

print(service_label)
