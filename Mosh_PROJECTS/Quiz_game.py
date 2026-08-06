
questions = [
  {
    "prompt": "What is the capital of France?",
    "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
    "answer": "A"
  },
  {
    "prompt": "Which language is primarily spoken in Brazil?",
    "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
    "answer": "B"
  },
  {
    "prompt": "What is the smallest prime number?",
    "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
    "answer": "B"
  },
  {
    "prompt": "Who wrote 'To Kill a Mockingbird'?",
    "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
    "answer": "A"
  }
]

answer_list = ['A', 'B', 'C', 'D' ]

def run_quiz(questions):
    score= 0 
    for question in questions:
      print('\n')
      print(question['prompt']) 
      for option in question['options']:
        print(option)
      while True:
        answer = input('What is your answer [A, B, C, D ]: ').upper()
        if answer == question['answer']:
          print('Correct Peahead\n')
          score += 1
          break
        elif answer not in answer_list:
          print('enter valid input dickhead')
                
        else:
          print('Wrong answr LOL, correct answer was', question['answer'], '\n') 
          break
      
    print(f'You got {score} out of {len(questions)} questions correct')
       

run_quiz(questions)


