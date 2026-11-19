import json
import pickle

from func import *
from sklearn.model_selection import train_test_split

matplotlib.rcParams["figure.figsize"] = (20, 10)

df1 = pd.read_csv("Bengaluru_House_Data.csv")

df2 = df1.drop(["area_type", "society", "balcony", "availability"], axis="columns")

df3 = df2.dropna()

df3["bhk"] = df3["size"].apply(lambda x: int(x.split(" ")[0]))

df4 = df3.copy()

df4["total_sqft"] = df3["total_sqft"].apply(convert_sqft_to_num)


df5 = df4.copy()

df5["price_per_sqft"] = df5["price"] * 1_00_000 / df5["total_sqft"]

df5.location = df5.location.apply(lambda x: x.strip())

location_stats = (
    df5.groupby("location")["location"].agg("count").sort_values(ascending=False)
)

location_stats_less_than_10 = location_stats[location_stats <= 10]

df5.location = df5.location.apply(
    lambda x: "other" if x in location_stats_less_than_10 else x
)

df6 = df5[~(df5.total_sqft / df5.bhk < 300)]

df7 = remove_pps_outliners(df6)

df8 = remove_bhk_outliers(df7)

df9 = df8[df8.bath < df8.bhk + 2]

df10 = df9.drop(["size", "price_per_sqft"], axis="columns")

dummies = pd.get_dummies(df10.location)

df11 = pd.concat([df10, dummies.drop("other", axis="columns")], axis="columns")

df12 = df11.drop("location", axis="columns")

X = df12.drop("price", axis="columns")

y = df12.price

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10
)

lr_clf = LinearRegression()
lr_clf.fit(X_train, y_train)

with open("banglore_home_price_model.pickle", "wb") as f:
    pickle.dump(lr_clf, f)


columns = {"data_columns": [col.lower() for col in X.columns]}

with open("columns.json", "w") as f:
    f.write(json.dumps(columns))
