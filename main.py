def calculate_weighted_score(project_scores, criteria_weights):
    """
    Calculates the total weighted score for a project.
    project_scores: A dictionary where keys are criteria names and values are lists of scores from judges.
    criteria_weights: A dictionary where keys are criteria names and values are their weights.
    """
    total_score = 0
    for criterion, scores_list in project_scores.items():
        if criterion in criteria_weights:
            # Calculate the average score for this criterion across all judges.
            # This helps reduce individual judge bias and the "luck factor" by aggregating opinions.
            avg_criterion_score = sum(scores_list) / len(scores_list) if scores_list else 0
            weight = criteria_weights[criterion]
            total_score += avg_criterion_score * weight
    return total_score

def main():
    # Define judging criteria and their relative weights.
    # These weights help prioritize certain aspects, making evaluation more objective and less random.
    criteria_weights = {
        "Innovation": 0.3,
        "Technical_Implementation": 0.25,
        "Impact_Potential": 0.2,
        "Presentation": 0.15,
        "Completeness": 0.1
    }

    # Simulate hackathon projects with scores from multiple judges for each criterion.
    # Scores are lists, representing different judges' evaluations for that criterion (e.g., out of 10).
    projects_data = [
        {
            "name": "EcoTracker App",
            "scores": {
                "Innovation": [8, 9, 7],
                "Technical_Implementation": [7, 8, 7],
                "Impact_Potential": [9, 8, 9],
                "Presentation": [8, 8, 9],
                "Completeness": [7, 7, 8]
            }
        },
        {
            "name": "AI Chef Assistant",
            "scores": {
                "Innovation": [9, 9, 8],
                "Technical_Implementation": [9, 8, 9],
                "Impact_Potential": [7, 7, 8],
                "Presentation": [7, 8, 7],
                "Completeness": [8, 8, 7]
            }
        },
        {
            "name": "Community Garden Network",
            "scores": {
                "Innovation": [7, 8, 7],
                "Technical_Implementation": [6, 7, 6],
                "Impact_Potential": [8, 9, 8],
                "Presentation": [9, 9, 8],
                "Completeness": [7, 6, 7]
            }
        },
        {
            "name": "Smart Waste Bin",
            "scores": {
                "Innovation": [8, 7, 8],
                "Technical_Implementation": [8, 9, 8],
                "Impact_Potential": [8, 7, 8],
                "Presentation": [7, 7, 7],
                "Completeness": [9, 9, 9]
            }
        }
    ]

    # Calculate weighted scores for all projects.
    evaluated_projects = []
    print("--- Hackathon Project Evaluation ---")
    print("Criteria Weights:", criteria_weights)
    print("\nCalculating scores...")

    for project in projects_data:
        project_name = project["name"]
        project_scores = project["scores"]
        weighted_score = calculate_weighted_score(project_scores, criteria_weights)
        evaluated_projects.append({"name": project_name, "final_score": weighted_score})
        print(f"  Project '{project_name}': Raw Scores: {project_scores}, Weighted Score: {weighted_score:.2f}")

    # Rank projects by their final weighted score.
    # Sorting by a calculated, objective score helps overcome the "luck factor"
    # and ensures fairness based on predefined criteria, making the process transparent.
    ranked_projects = sorted(evaluated_projects, key=lambda x: x["final_score"], reverse=True)

    print("\n--- Final Rankings ---")
    for i, project in enumerate(ranked_projects):
        print(f"{i + 1}. {project['name']} (Score: {project['final_score']:.2f})")

if __name__ == "__main__":
    main()
