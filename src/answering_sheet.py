
def is_the_answeer_correct(user_answer, csv):
    correct_answer = csv['correct_answer'].iloc(0)
    if user_answer == correct_answer:
        return True
    else:
        return False
    