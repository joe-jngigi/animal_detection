# Setting up Kaggle APIs

To setup Kaggle to get the dataset you require using the following steps.

First install the kaggle using `pip install kaggle`. Kaggle requires that you have the data that you require in a specific folder, **.kaggle**. In order to create, use `mkdir .kaggle`. Then visit the kaggle profile and create an API token. Once you click the create API the **kaggle.json** file is going to download automatically.

- You can now use `kaggle datasets list -s 'animal-detection'`
- You can download datasets from like this `kaggle datasets download -d 'https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009/download'`
