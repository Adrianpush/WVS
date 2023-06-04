from flask import Flask, render_template, request, json
from db_manager import Dbquery


manager = Dbquery()
manager.load_file("romania_2018.csv")
manager.calculate_scores()

values_dict = {
    "work_importance": "work_score",
    "family_importance": "fam_score",
    "religious_importance": "religion_score",
    "gender_equality": "gender_equality",
    "rel_n_ethnic_tolerance": "ethnic_rel_tolerance",
    "sex_minority_tolerance": "sex_minority_tolerance"
}

demographic_dict = {
    "age_group": "age_group",
    "gender": "Q260",
    "settlement_size": "settlement_size",
    "education": "education",
    "income": "Q288R"

}

colors_list = ["#f48fb1", "#7986cb",  "#4dd0e1",  "#a5d6a7", "#e6ee9c", "#ffab91"]

legend = {
    "values" :{
        "work_importance": {
            "title": "Importance of work values",
            "description": "Evaluates respondents view of work ethics as a factor contributing to a successful / meaningful life."
        },
        "family_importance": {
            "title": "Importance of family values",
            "description": "Evaluates respondents view of family relationships as a factor contributing to a successful / meaningful life."
            
        },
        "religious_importance": {
            "title": "Importance of religious values",
            "description": "Evaluates respondents view of religious ethics as a factor contributing to a successful / meaningful life."
        },
        "gender_equality": {
            "title": "Gender Equality",
            "description": "Evaluates how desirable is gender equality from the point of view of the respondents."
        },
        "rel_n_ethnic_tolerance": {
            "title": "Tolerance of ethnic and religious minorities",
            "description": "Evaluates respondents willingness to accept and / or interact with people of different religions and / or ethnicities."

        },
        "sex_minority_tolerance": {
            "title": "Tolerance of sexual minorities",
            "description": "Evaluates respondents willingness to accept and / or interact with people belonging to sexual minorities."
        }

    }

}


app = Flask(__name__)


@app.route("/", methods=['GET'])
def show_index():
    return render_template("index.html")

@app.route("/results", methods = ['POST', 'GET'])
def show_results():


        
    selected = request.form
    value = selected["social_value"]
    demo_group = selected["demographic"]

    data = manager.get_value_by_group(values_dict[value], demographic_dict[demo_group])

    labels = []
    values = []
    colors = []

    for i,key in enumerate(data):
        labels.append(key)
        values.append(data[key])
        colors.append(colors_list[i])

    labels = json.dumps(labels)
    values = json.dumps(values)
    colors = json.dumps(colors)


    return render_template("results.html", labels = labels, values = values, colors = colors, \
                            title = legend["values"][value]["title"], description = legend["values"][value]["description"])
    


if __name__ == "__main__":
    app.run()