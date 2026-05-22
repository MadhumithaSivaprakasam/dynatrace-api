def transform_problem(problem):

    return {
        "id": problem.get("problemId"),
        "problem_name": problem.get("title"),
        "severity": problem.get("severityLevel")
    }