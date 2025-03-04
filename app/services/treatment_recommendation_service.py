def physicianAction(index):
    physician_action = [
        ["0 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
    ]
    return physician_action[index]

def aiRecommendation(index):
    ai_recommendations = [
        ["0 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "0 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", ">0-40 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "40-205 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", "205-635 ml dose of iv fluid"],
        ["0 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        [">0-0.110 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        ["0.110-0.225 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        ["0.225-0.450 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
        [">0.450 ug/kg/h dose of vasopressor", ">635 ml dose of iv fluid"],
    ]
    return ai_recommendations[index]
