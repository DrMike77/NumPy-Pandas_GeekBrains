import pandas as pd
authors_dict = {"author_id": [1, 2, 3],
    "author_name": ["Тургенев", "Чехов", "Островский"]}
authors = pd.DataFrame(authors_dict)
books_dict = {"author_id": [1, 1, 1, 2, 2, 3, 3],
    "book_title": ["Отцы и дети", "Рудин", "Дворянское гнездо", "Толстый и тонкий", "Дама с собачкой", "Гроза", "Таланты и поклонники" ],
    "price": [450, 300, 350, 500, 450, 370, 290]}
books = pd.DataFrame(books_dict)
print(authors)
print(books)
authors_price = pd.merge(authors, books, on='author_id', how='inner')
print(authors_price)
top5 = authors_price.sort_values(by="price", ascending = False).head(5)
print(top5)
groupby = authors_price.groupby("author_name")
column_min = groupby.agg({"price": "min"})
column_max = groupby.agg({"price": "max"})
column_mean = groupby["price"].mean()
authors_stat = pd.concat([column_min, column_max, column_mean], axis=1)
authors_stat.columns = ["min_price","max_price","mean_price"]
print(authors_stat)