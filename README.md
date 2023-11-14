# MobilePriceEstimation
This project aims to estimate the optimum prices of used mobile phones by employing the Linear Regression algorithm. The dataset comprises specifications of over two thousand mobile phones, with a focus on three main brands: Samsung, Apple, and Infinix. The project follows the CRISP-DM methodology:

**Technical aspects of the project:**

**Data Collection:**
Data is scraped from OLX using Beautifulsoup in Python. This involves web scraping techniques to extract relevant information from the OLX website.
Facebook data is obtained using Facebook-scraper in Python, focusing on the Applewala.pk page.

**Data Cleaning and Preparation:**
Missing values in RAM and ROM are handled differently for OLX and Facebook data, involving database searches and value assignment.
Inconsistencies in data are addressed through scripting in Python, utilizing the Pandas library.
Location data inconsistencies are resolved.

**Data Merging:**
OLX and Facebook datasets are merged into one, resulting in a consolidated dataset for analysis.

**Data Encoding:**
LabelEncoder from the scikit-learn library is employed for encoding categorical features like Brand, Model, and Location, converting them into numerical values suitable for machine learning models.

**Data Modeling:**
Linear Regression is chosen as the algorithm for price estimation. This involves training the model on the prepared dataset and assessing its predictive capabilities.

**Data Analysis and Visualization:**
PowerBI is used for data analysis and visualization, allowing for interactive and insightful representations of the relationships between different features.

**Key Influencer Analysis:**
Segmentation is performed on Apple, Samsung, and Infinix datasets to identify key influencers affecting the average price within each brand.

**Deployment**:
The model is deployed to predict prices for specific scenarios, such as estimating the value for an Apple iPhone-12-Pro-Max with specific specifications and location.
Conclusion and Future Applications:

The project highlights the significance of cost estimation in marketing and suggests that similar techniques can be applied to various products.
The project lays the groundwork for potential future applications in predicting prices for different types of goods, leveraging data mining and analysis techniques.
In summary, the technical aspects encompass web scraping, data cleaning, encoding, regression modeling, and advanced analytics using tools like PowerBI, with the aim of providing a comprehensive understanding of used mobile phone pricing.
