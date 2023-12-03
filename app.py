# TODO: prediction forms
# TODO: model integration

from flask import Flask, request
from flask import render_template
from pickle import load

# init app
app = Flask(__name__)

with open('models/salesvspositive.pkl', 'rb') as f:
    salesvspositive = load(f)

# routes
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

@app.route("/postive-reviews-and-total-sales", methods=['GET', 'POST'])
def postiveReviewsAndTotalSales():
    if request.method == 'POST':
        pred = salesvspositive.predict([[float(request.form.get('positive'))]])
        return (f'<h1 style="text-align: center;">Total sales</h1><dialog open><p>{pred[0]}</p></dialog>')
    
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

@app.route("/overview")
def overview():
    return render_template('overview.html')

if __name__ == '__main__':
    app.run(debug=True)