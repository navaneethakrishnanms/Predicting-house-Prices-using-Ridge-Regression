from flask import Flask, request, render_template
import pickle
import numpy as np

application = Flask(__name__)
app = application

# Load your model
ridge_model1 = pickle.load(open('model/ridge_model.pkl', 'rb'))

@app.route("/", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        # collect form inputs
        size_m2 = float(request.form.get('size_m2'))
        bedrooms = int(request.form.get('bedrooms'))
        bathrooms = int(request.form.get('bathrooms'))
        distance_city = float(request.form.get('distance_city'))
        age_years = float(request.form.get('age_years'))

        # prepare input
        input_query = np.array([[size_m2, bedrooms, bathrooms, distance_city, age_years]])

        # make prediction
        prediction = ridge_model1.predict(input_query)[0]

        # render template with result
        return render_template("home.html", results=prediction)

    # GET request → just show the form (empty)
    return render_template("home.html", results=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

