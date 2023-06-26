from flask import Flask, render_template, request, jsonify
from db_manager import Dbquery

populate_form = {
    "countries": {
        "argentina" : "argentina",
        "china" : "china",
        "germany" : "germany",
        "great_britain" : "great britain",
        "greece" : "greece",
        "japan" : "japan",
        "south_korea" : "south korea",
        "turkey" : "turkey",
        "ukraine" : "ukraine",
        "united_states" : "united states",
        "romania": "romania",
        "russian_federation" : "russian federation",
        
    },
    "values": {
        "work_score": "Importance of work",
        "fam_score": "Importance of family",
        "religion_score": "Importance of religion",
        "gender_equality": "Importance of gender equality",
        "ethnic_rel_tolerance": "Ethnic and religious tolerance",
        "sex_minority_tolerance": "Tolerance of sexual minorities",
    },
    "demo_group": {
        "age_group": "Age Group",
        "gender": "Gender",
        "education": "Education",
        "settlement_size": "Settlement Size",
        "income": "Income",
    },
}

colors_list = ["#f48fb1", "#7986cb", "#4dd0e1", "#a5d6a7", "#e6ee9c", "#ffab91"]

legend = {
    "values": {
        "work_score": {
            "title": "Importance of work values",
            "description": "Evaluates respondents view of work ethics as a factor contributing to a successful / meaningful life.",
        },
        "fam_score": {
            "title": "Importance of family values",
            "description": "Evaluates respondents view of family relationships as a factor contributing to a successful / meaningful life.",
        },
        "religion_score": {
            "title": "Importance of religious values",
            "description": "Evaluates respondents view of religious ethics as a factor contributing to a successful / meaningful life.",
        },
        "gender_equality": {
            "title": "Gender Equality",
            "description": "Evaluates how desirable is gender equality from the point of view of the respondents.",
        },
        "ethnic_rel_tolerance": {
            "title": "Tolerance of ethnic and religious minorities",
            "description": "Evaluates respondents willingness to accept and / or interact with people of different religions and / or ethnicities.",
        },
        "sex_minority_tolerance": {
            "title": "Tolerance of sexual minorities",
            "description": "Evaluates respondents willingness to accept and / or interact with people belonging to sexual minorities.",
        },
    }
}


app = Flask(__name__)


@app.route("/api/", methods=["GET"])
def get_country_info():
    args = request.args

    if request.method == "GET":
        if args.keys() >= {"country", "social_value", "demo_group"}:
            db = Dbquery(args["country"])
            data = db.get_value_by_group(
                value=args["social_value"], group=args["demo_group"]
            )
            formatted_data = {
                "country_name": populate_form["countries"][args["country"]],
                "values": [
                    {
                        "value_name": args["social_value"],
                        "value_title": legend["values"][args["social_value"]]["title"],
                        "value_description": legend["values"][args["social_value"]]["description"],
                        "data": data
                    }
                ], 
            }

            return jsonify(formatted_data)

        elif args.keys() >= {"country", "social_value"}:
            db = Dbquery(args["country"])
            data = db.get_country_value(args["social_value"])
            formatted_data = {
                "country_name": populate_form["countries"][args["country"]],
                "values": [
                    {
                        "value_name": args["social_value"],
                        "value_title": legend["values"][args["social_value"]]["title"],
                        "value_description": legend["values"][args["social_value"]]["description"],
                        "data": [{"country_average": data}]
                    }
                ], 
            }

            return jsonify(formatted_data)

        elif args.keys() >= {"country"}:
            db = Dbquery(args["country"])


            formatted_data = {
                "country_name": populate_form["countries"][args["country"]],
                "values": [
                    {
                        "value_name": social_value,
                        "value_title": legend["values"][social_value]["title"],
                        "value_description": legend["values"][social_value]["description"],
                        "data": [{"country_average": db.get_country_value(social_value)}]
                    } for social_value in populate_form["values"].keys()
                ], 
            }
            return jsonify(formatted_data)
        
        else:
            print("Invalid Paramters")
    print(data)
    return jsonify(data)


@app.route("/", methods=["GET"])
def show_index():
    return render_template("index.html", populate_form=populate_form)


@app.route("/results", methods=["POST", "GET"])
def show_results():
    selected = request.form

    country = selected["countries"]
    value = selected["social_value"]
    demo_group = selected["demographic"]

    db = Dbquery(country)
    
    data = db.get_value_by_group(value, demo_group)

    labels = []
    values = []
    colors = []

    for index,( key, val) in enumerate(data.items()):
        labels.append(key)
        values.append(val)
        colors.append(colors_list[index])
      

    return render_template(
        "results.html",
        populate_form=populate_form,
        selected_country=country,
        selected_demo=demo_group,
        selected_value=value,
        labels=labels,
        values=values,
        colors=colors,
        title=legend["values"][value]["title"],
        description=legend["values"][value]["description"],
    )


if __name__ == "__main__":
    app.run(debug=False)
