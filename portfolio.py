import pandas as pd
import chromadb
import os

class Portfolio:
    def __init__(self, asset_path: str = os.path.join("assets", "portfolio.csv")):
        self.asset_path = asset_path
        self.data = pd.read_csv(self.asset_path)
        self.client = chromadb.PersistentClient(os.path.join(os.path.dirname(os.path.abspath(__file__)),"vector_store"))
        self.collection = self.client.get_or_create_collection("portfolio")
    
    def load_portfolio(self):
        if self.collection.count() == 0:
            for index, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],
                    metadatas={"links": row["Links"]},
                    ids=[str(index)],
                )

    def query_for_links(self, skills):
        return self.collection.query(
            query_texts=skills,
            n_results=2).get("metadatas",[])