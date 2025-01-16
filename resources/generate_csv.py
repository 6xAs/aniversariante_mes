import pandas as pd

# Listas com dados de pessoas fictícias
names = [
    "Alice Johnson", "Bob Smith", "Carlos Pereira", "Diana Silva", 
    "Eva Richards", "Frank Martin", "Grace Brown", "Henry Wilson", 
    "Ivy Clark", "Jack Moore", "Kathy Lee", "Louis Adams", 
    "Mona Parker", "Nick Turner", "Olivia Evans", "Paul Mitchell", 
    "Quincy Harris", "Rita Scott", "Steve Lewis", "Tina Green"
]

birthdates = [
    "1990-02-15", "1985-05-22", "1978-12-11", "1992-07-30",
    "1988-01-25", "1983-03-09", "1995-09-13", "1975-11-04",
    "1990-04-18", "1980-06-20", "1993-03-25", "1986-08-12",
    "1991-10-09", "1982-05-14", "1994-12-22", "1987-06-07",
    "1979-02-11", "1984-09-19", "1996-01-30", "1981-10-02"
]

# Links públicos para imagens aleatórias de pessoas
image_urls = [
    "https://randomuser.me/api/portraits/men/1.jpg",
    "https://randomuser.me/api/portraits/men/2.jpg",
    "https://randomuser.me/api/portraits/men/3.jpg",
    "https://randomuser.me/api/portraits/men/4.jpg",
    "https://randomuser.me/api/portraits/women/5.jpg",
    "https://randomuser.me/api/portraits/men/6.jpg",
    "https://randomuser.me/api/portraits/men/7.jpg",
    "https://randomuser.me/api/portraits/men/8.jpg",
    "https://randomuser.me/api/portraits/women/9.jpg",
    "https://randomuser.me/api/portraits/men/10.jpg",
    "https://randomuser.me/api/portraits/women/11.jpg",
    "https://randomuser.me/api/portraits/men/12.jpg",
    "https://randomuser.me/api/portraits/men/13.jpg",
    "https://randomuser.me/api/portraits/men/14.jpg",
    "https://randomuser.me/api/portraits/women/15.jpg",
    "https://randomuser.me/api/portraits/men/16.jpg",
    "https://randomuser.me/api/portraits/women/17.jpg",
    "https://randomuser.me/api/portraits/men/18.jpg",
    "https://randomuser.me/api/portraits/women/19.jpg",
    "https://randomuser.me/api/portraits/men/20.jpg"
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
df.to_csv("Random_People_Dataset.csv", index=False)

# Exibindo o DataFrame
print(df)
