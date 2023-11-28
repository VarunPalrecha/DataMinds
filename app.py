from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/products")
def products():
    return render_template('list.html')

@app.route("/general-analysis")
def generalAnalysis():
    return render_template('catagory.html')

@app.route("/price-vs-rating")
def priceVsRating():
    return render_template('price_VS_rating.html')

@app.route("/reviews")
def reviews():
    return render_template('review_graph.html')

@app.route("/add-json")
def addJson():
    return render_template('genOwnChart2.html')

@app.route("/postive-reviews-and-total-sales")
def postiveReviewsAndTotalSales():
    return render_template('predictive2.html')

@app.route("/negative-reviews-and-total-sales")
def negativeReviewsAndTotalSales():
    return render_template('predictive3.html')

@app.route("/sales-analysis-by-seller")
def salesAnalysisBySeller():
    return render_template('predictive4.html')

@app.route("/average-total-reviews-by-category")
def averageTotalReviewsByCategory():
    return render_template('predictive5.html')

@app.route("/predicted-distribution-of-prices-by-category")
def predictedDistributionOfPricesByCategory():
    return render_template('predictive6.html')


if __name__ == '__main__':
    app.run(debug=True)