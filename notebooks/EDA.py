# notebooks/EDA.py
import pandas as pd
import matplotlib.pyplot as plt

CLEAN_PATH = "output/cleaned_products.csv"

def run_eda():
    df = pd.read_csv(CLEAN_PATH)
    print("Total rows:", len(df))
    print(df[['min_price','max_price']].describe())

    # histogram of min_price
    df['min_price'].dropna().plot(kind='hist', bins=30)
    plt.title("Distribution of min_price")
    plt.xlabel("Price (INR)")
    plt.tight_layout()
    plt.savefig("plots/min_price_hist.png")
    plt.clf()

    # top seller cities
    top_cities = df['seller_city'].fillna("Unknown").value_counts().nlargest(10)
    top_cities.plot(kind='bar')
    plt.title("Top seller cities")
    plt.tight_layout()
    plt.savefig("plots/top_seller_cities.png")
    plt.clf()

    # price boxplot (if category present; fallback to title words)
    if 'category' in df.columns and not df['category'].isna().all():
        df.boxplot(column='min_price', by='category', rot=45)
        plt.title("Price by Category")
        plt.suptitle("")
        plt.savefig("plots/price_by_category.png")
        plt.clf()

    print("Saved plots to /plots")

if __name__ == "__main__":
    run_eda()
