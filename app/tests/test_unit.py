from app.models.problem_model import transform_problem

def test_transform_problem():

    sample_problem = {
        "problemId": "123",
        "title": "CPU High",
        "severityLevel": "ERROR"
    }

    transformed = transform_problem(sample_problem)

    assert transformed["id"] == "123"
    assert transformed["problem_name"] == "CPU High"
    assert transformed["severity"] == "ERROR"