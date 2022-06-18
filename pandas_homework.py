# задание 1
import pandas as pd
a = {
    "author_id":[1, 2, 3],
    "author_name":["Тургенев", "Чехов", "Чайковский"]
}
authors = pd.DataFrame(a)
print(authors)

b = {
    "author_id":[1, 1, 1, 2, 2, 3, 3],
    "book_title":['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    "price":[450, 300, 350, 500, 450, 370, 290]
}
book = pd.DataFrame(b)
print(book)

# задание 2

authors_price = pd.merge(authors, book, on="author_id", how="outer")
print(authors_price)

# задание 3
print(authors_price.nlargest(5, "price"))

# задание 4
c = authors_price.groupby("author_name")

df_mean = pd.DataFrame(c["price"].mean())
df_min = pd.DataFrame(c["price"].min())
df_max = pd.DataFrame(c["price"].max())

# не разобрался как это объединить в один DataFrame
print("Средняя цена для каждого автора: {}".format(df_mean))
print("Минимальная цена для каждого автора: {}".format(df_min))
print("Максимальная цена для каждого автора: {}".format(df_max))
#конец

