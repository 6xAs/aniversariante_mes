import pandas as pd

# Lista de nomes fictícios e suas datas de nascimento
names = [
    "Mario", "Lara Croft", "Sonic", "Samus Aran", "Link",
    "Donkey Kong", "Master Chief", "Kirby", "Kratos", "Pac-Man",
    "Mega Man", "Street Fighter Ryu", "Nathan Drake", "Ash Ketchum", "Zelda",
    "Aloy", "Geralt of Rivia", "Cloud Strife", "Pikachu", "Rayman"
]

birthdates = [
    "1981-09-13", "1996-10-25", "1991-06-23", "1986-08-15", "1986-02-21",
    "1994-11-01", "2001-11-15", "1992-04-01", "2005-03-02", "1980-11-29",
    "1987-09-09", "1987-08-12", "2007-10-22", "1997-04-01", "1992-11-21",
    "2017-02-28", "2009-10-06", "1997-03-06", "1996-08-16", "1995-12-12"
]

# URLs de imagens de alta qualidade de personagens
image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/8/83/Mario_%28character%29.png",
    "https://upload.wikimedia.org/wikipedia/commons/a/a3/Lara_Croft_%28character%29.png",
    "https://upload.wikimedia.org/wikipedia/commons/a/a1/Sonic_the_Hedgehog.png",
    "https://upload.wikimedia.org/wikipedia/commons/7/74/Samus_Aran.png",
    "https://upload.wikimedia.org/wikipedia/commons/a/a9/Link_%28The_Legend_of_Zelda%29.png",
    "https://upload.wikimedia.org/wikipedia/commons/7/7b/Donkey_Kong_character.png",
    "https://upload.wikimedia.org/wikipedia/commons/2/2a/Master_Chief.png",
    "https://upload.wikimedia.org/wikipedia/commons/f/f8/Kirby_Character_Artwork.png",
    "https://upload.wikimedia.org/wikipedia/commons/9/97/Kratos_from_God_of_War.png",
    "https://upload.wikimedia.org/wikipedia/commons/6/6e/Pac-Man.png",
    "https://upload.wikimedia.org/wikipedia/commons/e/e0/Mega_Man_Character_Artwork.png",
    "https://upload.wikimedia.org/wikipedia/commons/4/4a/Ryu_%28Street_Fighter%29.png",
    "https://upload.wikimedia.org/wikipedia/commons/c/c9/Nathan_Drake.png",
    "https://upload.wikimedia.org/wikipedia/commons/a/a4/Ash_Ketchum.png",
    "https://upload.wikimedia.org/wikipedia/commons/4/43/Princess_Zelda_-_The_Legend_of_Zelda.png",
    "https://upload.wikimedia.org/wikipedia/commons/6/6c/Aloy_from_Horizon_Zero_Dawn.png",
    "https://upload.wikimedia.org/wikipedia/commons/4/47/Geralt_of_Rivia.png",
    "https://upload.wikimedia.org/wikipedia/commons/9/97/Cloud_Strife_character_art.png",
    "https://upload.wikimedia.org/wikipedia/commons/9/9c/Pikachu.png",
    "https://upload.wikimedia.org/wikipedia/commons/0/0d/Rayman_character.png"
]

# Criar DataFrame
data = {
    "Name": names,
    "Date_of_Birth": birthdates,
    "Image_URL": image_urls
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvar em CSV
df.to_csv("Character_Images.csv", index=False)

# Exibindo o DataFrame
print(df)
