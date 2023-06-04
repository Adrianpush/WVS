import pandas


class Dbquery:
    def __init__(self) -> None:
        self.df = None

    def load_file(self, file_name):
        with open("data/romania_2018.csv", "r") as file:

            self.df = pandas.read_csv(file, sep=";")


    def _compute_religion_score(self, row):
        religion_score = 0
        valid_answers = 0

        if row["Q6"] > 0:
            valid_answers += 1

        if row["Q6"] == 1:
            religion_score += 10
        elif row["Q6"] == 2:
            religion_score += 7
        elif row["Q6"] == 3:
            religion_score += 3

        if row["Q64"] > 0:
            valid_answers += 1

        if row["Q64"] == 1:
            religion_score += 10
        elif row["Q64"] == 2:
            religion_score += 7
        elif row["Q64"] == 3:
            religion_score += 3

        if row["Q160"] > 0:
            valid_answers += 1
            religion_score += row["Q160"]

        if row["Q171"] > 0:
            valid_answers += 1

        if row["Q171"] == 1:
            religion_score += 10
        elif row["Q171"] == 2:
            religion_score += 9
        elif row["Q171"] == 3:
            religion_score += 8
        elif row["Q171"] == 4:
            religion_score += 6
        elif row["Q171"] == 5:
            religion_score += 4
        elif row["Q171"] == 6:
            religion_score += 2

        if valid_answers:
            return religion_score / valid_answers

    def _compute_family_score(self, row):
        family_score = 0
        valid_answers = 0

        if row["Q1"] > 0:
            valid_answers += 1

        if row["Q1"] == 1:
            family_score += 10
        elif row["Q1"] == 2:
            family_score += 7
        elif row["Q1"] == 3:
            family_score += 3

        if row["Q58"] > 0:
            valid_answers += 1

        if row["Q58"] == 1:
            family_score += 10
        elif row["Q58"] == 2:
            family_score += 7
        elif row["Q58"] == 3:
            family_score += 3

        if row["Q185"] > 0:
            valid_answers += 1
            family_score += abs(row["Q185"] - 11)

        if valid_answers:
            return family_score / valid_answers

    def _compute_work_score(self, row):
        work_score = 0
        valid_answers = 0

        if row["Q5"] > 0:
            valid_answers += 1

        if row["Q1"] == 1:
            work_score += 10
        elif row["Q5"] == 2:
            work_score += 7
        elif row["Q5"] == 3:
            work_score += 3

        if row["Q41"] > 0:
            valid_answers += 1

        if row["Q41"] == 1:
            work_score += 10
        elif row["Q41"] == 2:
            work_score += 7.5
        elif row["Q41"] == 3:
            work_score += 5
        elif row["Q41"] == 4:
            work_score += 2.5

        if valid_answers:
            return work_score / valid_answers

    def _compute_gender_equality_score(self, row):
        valid_answers = 0
        g_discrimination_score = 0

        if row["Q28"] > 0:
            valid_answers += 1

        if row["Q28"] == 1:
            g_discrimination_score += 10
        elif row["Q28"] == 2:
            g_discrimination_score += 7
        elif row["Q28"] == 3:
            g_discrimination_score += 3

        if row["Q29"] > 0:
            valid_answers += 1

        if row["Q29"] == 1:
            g_discrimination_score += 10
        elif row["Q29"] == 2:
            g_discrimination_score += 7
        elif row["Q29"] == 3:
            g_discrimination_score += 3

        if row["Q30"] > 0:
            valid_answers += 1

        if row["Q30"] == 1:
            g_discrimination_score += 10
        elif row["Q30"] == 2:
            g_discrimination_score += 7
        elif row["Q30"] == 3:
            g_discrimination_score += 3

        if row["Q31"] > 0:
            valid_answers += 1

        if row["Q31"] == 1:
            g_discrimination_score += 10
        elif row["Q31"] == 2:
            g_discrimination_score += 7
        elif row["Q31"] == 3:
            g_discrimination_score += 3

        if valid_answers:
            return abs(10 - (g_discrimination_score / valid_answers))

    def _compute_tolerance_ethnic_religious(self, row):
        tolerance_score = 0
        valid_answers = 0

        if row["Q19"] > 0:
            valid_answers += 1

        if row["Q19"] == 2:
            tolerance_score += 10

        if row["Q21"] > 0:
            valid_answers += 1

        if row["Q21"] == 2:
            tolerance_score += 10

        if row["Q23"] > 0:
            valid_answers += 1

        if row["Q23"] == 2:
            tolerance_score += 10

        if row["Q34"] > 0:
            valid_answers += 1

        if row["Q34"] == 2:
            tolerance_score += 2.5
        elif row["Q34"] == 3:
            tolerance_score += 5
        elif row["Q34"] == 4:
            tolerance_score += 7.5
        elif row["Q34"] == 5:
            tolerance_score += 10

        if row["Q121"] > 0:
            valid_answers += 1

        if row["Q121"] == 2:
            tolerance_score += 2.5
        elif row["Q121"] == 3:
            tolerance_score += 5
        elif row["Q121"] == 4:
            tolerance_score += 7.5
        elif row["Q121"] == 5:
            tolerance_score += 10

        if row["Q170"] > 0:
            valid_answers += 1

        if row["Q170"] == 2:
            tolerance_score += 3
        elif row["Q170"] == 3:
            tolerance_score += 7
        elif row["Q170"] == 4:
            tolerance_score += 10

        if valid_answers:
            return tolerance_score / valid_answers

    def _compute_tolerance_sex_minorities(self, row):
        valid_answers = 0
        tolerance_score = 0

        if row["Q22"] > 0:
            valid_answers += 1

        if row["Q22"] == 2:
            tolerance_score += 10

        if row["Q36"] > 0:
            valid_answers += 1

        if row["Q36"] == 1:
            tolerance_score += 10
        elif row["Q36"] == 2:
            tolerance_score += 7.5
        elif row["Q36"] == 3:
            tolerance_score += 5
        elif row["Q36"] == 4:
            tolerance_score += 2.5

        if row["Q182"] > 0:
            valid_answers += 1
            tolerance_score += row["Q182"]

        if valid_answers:
            return tolerance_score / valid_answers

    def _compute_age_group(self, row):
        if row["Q262"] > 84:
            return "84+"
        if row["Q262"] > 64:
            return "64 - 84"
        if row["Q262"] > 52:
            return "52 - 64"
        if row["Q262"] > 40:
            return "40 - 52"
        if row["Q262"] > 28:
            return "28 - 40"
        if row["Q262"] > 18:
            return "18 - 28"

    def _compute_settlement_size(self, row):
        if row["G_TOWNSIZE"] in range(1, 5):
            return "Small Settlement"
        elif row["G_TOWNSIZE"] in range(5, 8):
            return "Medium Settlement"
        elif row["G_TOWNSIZE"] == 8:
            return "Large Settlement"

    def _compute_education_level(self, row):

        if row["Q275"] in range(1, 3):
            return "Base Education - Up to ISCED 2"
        elif row["Q275"] in range(3, 5):
            return "Medium Education - Up to ISCED 4"
        elif row["Q275"] in range(5,10):
            return "Higher Education - ISCED 6 and above"

    def calculate_scores(self):
        self.df["religion_score"] = self.df.apply(
            lambda row: self._compute_religion_score(row), axis=1
        )
        self.df["fam_score"] = self.df.apply(
            lambda row: self._compute_family_score(row), axis=1
        )
        self.df["work_score"] = self.df.apply(
            lambda row: self._compute_work_score(row), axis=1
        )
        self.df["gender_equality"] = self.df.apply(
            lambda row: self._compute_gender_equality_score(row), axis=1
        )
        self.df["ethnic_rel_tolerance"] = self.df.apply(
            lambda row: self._compute_tolerance_ethnic_religious(row), axis=1
        )
        self.df["sex_minority_tolerance"] = self.df.apply(
            lambda row: self._compute_tolerance_sex_minorities(row), axis=1
        )
        self.df["age_group"] = self.df.apply(
            lambda row: self._compute_age_group(row), axis=1
        )
        self.df["settlement_size"] = self.df.apply(
            lambda row: self._compute_settlement_size(row), axis=1
        )
        self.df["education"] = self.df.apply(
            lambda row: self._compute_education_level(row), axis=1
        )

    def _format_dict(self, dict, group):
        
        new_dict = {}

        if group == "age_group":

            keys = ["Ages between 18 and 28", "Ages between 28 and 40", "Ages between 40 and 52", "Ages between 52 and 64", "Ages between 64 and 84", "Ages over 84"]
            new_dict = {key: key for key in keys}
            for key in dict:
                if key == "18 - 28":
                    new_dict["Ages between 18 and 28"] = format(dict[key], '.2f')
                elif key == "28 - 40":
                    new_dict["Ages between 28 and 40"] = format(dict[key], '.2f')
                elif key == "40 - 52":
                    new_dict["Ages between 40 and 52"] = format(dict[key], '.2f')
                elif key == "52 - 64":
                    new_dict["Ages between 52 and 64"] = format(dict[key], '.2f')
                elif key == "64 - 84":
                    new_dict["Ages between 64 and 84"] = format(dict[key], '.2f')
                elif key == "84+":
                    new_dict["Ages over 84"] = format(dict[key], '.2f')

        elif group == "Q260":

            keys = ["Men", "Women"]
            new_dict = {key: key for key in keys}
            for key in dict:
                if key == 1:
                    new_dict["Men"] = format(dict[key], '.2f')
                elif key == 2:
                    new_dict["Women"] = format(dict[key], '.2f')
        
        elif group == "education":

            keys = ["Base Education - Up to ISCED 2", "Medium Education - Up to ISCED 4", "Higher Education - ISCED 6 and above"]
            new_dict = {key: key for key in keys}

            for k in dict:
                new_dict[k] = format(dict[k], '.2f')

        elif group == "settlement_size":

            keys = ["Small Settlement", "Medium Settlement", "Large Settlement"]
            new_dict = {key: key for key in keys}
            for key in dict:
                new_dict[key] = format(dict[key], '.2f')

        elif group == "Q288R":
                        
            keys = ["Low Income", "Medium Income", "High Income"]
            new_dict = {key: key for key in keys}

            for key in dict:
                if key == 1:
                    new_dict["Low Income"] = format(dict[key], '.2f')
                elif key == 2:
                    new_dict["Medium Income"] = format(dict[key], '.2f')
                elif key == 3:
                    new_dict["High Income"] = format(dict[key], '.2f')

        return new_dict
    
    def get_value_by_group(self, value, group):

        data = self.df.groupby([group])[value].mean()
        data_dict = self._format_dict(data.to_dict(), group)   

        return data_dict
