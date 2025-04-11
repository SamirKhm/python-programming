
questions=[
  ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
  ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
  ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
  ["Who invented the light bulb?", "Nikola Tesla", "Albert Einstein", "Thomas Edison", "Isaac Newton", 3],
  ["What is H2O commonly known as?", "Salt", "Hydrogen", "Water", "Oxygen", 3],
  ["Which animal is known as the king of the jungle?", "Elephant", "Lion", "Tiger", "Bear", 2],
  ["Who wrote 'Romeo and Juliet'?", "William Wordsworth", "William Shakespeare", "Charles Dickens", "Jane Austen", 2],
  ["Which country is famous for the Great Wall?", "India", "Japan", "China", "Korea", 3],
  ["What gas do humans breathe in?", "Carbon Dioxide", "Nitrogen", "Hydrogen", "Oxygen", 4],
  ["Which is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2]
]

prizes=[100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
idx=0

for question in questions:
    print(question[0]) 
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    
    # Check wether he answer is correct or not
    a=int(input("Enter your answer. 1 for a , 2 for b , 3 for c , 4 for d : " ))

    if(question[5] == a):
        print("Well done!\n")
        print(f"You have won {prizes[idx]} Rs.\n")
        
        idx+=1
        
    else:
        print("Wrong answer!\n")
        
        break