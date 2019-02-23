dct = {
	"city" : "Москва",
	"temperature" : "20"
}

dct["temperature"] = str(int(dct["temperature"]) - 5)

t = dct.get("country", "Россия")

dct["date"] = '23.02.2019'

print(dct)
print(dct.get("country", "Россия"))