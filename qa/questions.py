def get_questions(interview_type):
    if interview_type == "Technical":
        return [
            "Hello Rozy, Tell me about yourself and your experience in machine learning.",
            # "Tell me about a machine learning project you worked on.",
            # "How do you evaluate model performance?",
            # "Explain your experience with NLP or Computer Vision."
        ]
    elif interview_type == "Managerial":
        return [
            "Describe a time you managed a project under tight deadlines.",
            "How do you handle conflicts within a team?",
            "How do you prioritize tasks as a leader?"
        ]
    elif interview_type == "HR":
        return [
            "Tell me about yourself.",
            "What are your strengths and weaknesses?",
            "Why should we hire you?"
        ]
