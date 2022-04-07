{% include navigation.html %}

# Create Task Plan
Description:
We have a class, with objects as trivia, and the attributes are questions, answers, and point values. A user is prompted with a question of how many questions they want, and then on input, loads one question with an input box to give the correct answer. A point count is kept, and correct answers add to the total. 

Outline:
Class has Trivia(Question, Answer, Point Value)

Check answer function
checkanswer =
if guess is equal to the answer, 
return true 
else false

score is set to 0
score = 0

objects are made using the attributes from the class
q1 = (question, answer, integer points)
q2 =("", "", #)
...

list is made using the objects
newlist = [q1, q2, ... ]

Function is created to take inputs and print responses based on correct or incorrect and the updated score
if run main
input = input("How many questions do you want)
take a random question in the list 
randomvalue =(for i in range int(input)...)
guess = input(randomvalue)

then use the check answer function given the guess as a parameter
if randomvalue.checkanswer(guess)
-update score
-print score
-print correct
else 
- print incorrect 
- print correct answer

finally remove that question as a possible question to come again



Requirements:
- [x] takes user input
- [x] uses a list
- [x] has a procedure with parameters
- [x] algorithm within procedure
- [x] calls to the procedure
- [x] instructions to use it  

# Code
```<script>
    let score = 0
    class Trivia {
        constructor(question, answer, point) {
            this.question = question;
            this.answer = answer;
            this.point = point;
        }

        CheckAnswer(guess) {
            return guess === this.answer
        }
    }
    let question1 = new Trivia('Chile?', 'Santiago', 1);
    let question2 = new Trivia('France?', 'Paris', 1);
    let question3 = new Trivia('Czech Republic?', 'Prague', 1);
    let question4 = new Trivia('Portugal?', 'Lisbon', 1);
    let question5 = new Trivia('Ethiopia?', 'Addis Ababa', 1);


    const qarray = [question1, question2, question3, question4, question5]

    function test() {
        window.alert(qarray[1])
    }
    function QNA() {
        let questions = parseInt(document.getElementById('number').value);
        for (let i = 0; i < questions; i++) {
            const randomValue = qarray[Math.floor(Math.random() * qarray.length)];
            let guess = prompt("What is the capital of " + randomValue.question);
            if (randomValue.CheckAnswer(guess)) {
                score = score + 1;
                document.getElementById('answer').innerHTML = "Well Done";
                document.getElementById('score').innerHTML = "Your score is " + score;
            }
            else {
                document.getElementById('score').innerHTML = "Your score is " + score;

            }

            }
    }
</script>
{#    <button onclick="test()">LFG</button>#}
    <div class="container"></div>
    <label for="number">How many questions do you want?</label>
    <input id="number" type="number"/>
    <button onclick="QNA()">Submit</button>
    <p id="answer"></p>
    <p id="score"></p>
```
# Write Up  
3a. The overall purpose of this program was to cycle a random question based on how many questions a user wants and then display them on screen with a text box to answer. If you get the questions correct, then it updates your score based on how many you get correct. In the video, I demonstrated the runtime of a user giving an input in the form of the number of questions they want, and then the prompt showed up, with a question and answer box. When I put in the correct answer, it kept iterating for how many questions the user wanted, and then stopped once the desired amount was finished. After, it gave a prompt saying "well done" if they scored any points, and nothing if they were wrong. Also updated with a score counter.
3bi. 
``` let question1 = new Trivia('Chile?', 'Santiago', 1); let question2 = new Trivia('France?', 'Paris', 1); let question3 = new Trivia('Czech Republic?', 'Prague', 1); let question4 = new Trivia('Portugal?', 'Lisbon', 1); let question5 = new Trivia('Ethiopia?', 'Addis Ababa', 1);

const qarray = [question1, question2, question3, question4, question5] 
``` 

3bii. 
``` for (let i = 0; i < questions; i++) { const randomValue = qarray[Math.floor(Math.random() * qarray.length)]; let guess = prompt("What is the capital of " + randomValue.question);
```
3b. The name of the array was qarray, and a specific value within the array was called using randomValue. The data contained in the list are questions in a random question bank. The selected list manages complexity because I defined different questions as objects using a class and constructor method. The array's elements were the objects, and if I did not use the array, I wouldn't have been able to get a random question from the bank, and the concept of the program would be lost.
3c.
```function QNA() { let questions = parseInt(document.getElementById('number').value); for (let i = 0; i < questions; i++) { const randomValue = qarray[Math.floor(Math.random() * qarray.length)]; let guess = prompt("What is the capital of " + randomValue.question); if (randomValue.CheckAnswer(guess)) { score = score + 1; document.getElementById('answer').innerHTML = "Well Done"; document.getElementById('score').innerHTML = "Your score is " + score; } else { document.getElementById('score').innerHTML = "Your score is " + score;

        }

        }
}
<div class="container"></div>
<label for="number">How many questions do you want?</label>
<input id="number" type="number"/>
<button onclick="QNA()">Submit</button>
```
3ciii. The procedure generates a certain number of questions based on user input and displays them on screen, as well as checks each answer that a user puts in, to keep track of score for all the trials. 3civ. The procedure first creates a variable called user questions that is an integer based on what a user puts in a text box. Then, it iterates for as long as whatever number is stored in the variable in the beginning. For that for loop, it takes a random object from the array, then stores it in a variable. It then demonstrates a window prompt with the variable being used to call the question, and then a user's response is stored in a variable that is put through a CheckAnswer method from the class above. Then, it is put through an if statement where if you get the right answer, it adds a point and displays a score, otherwise it says incorrect. 3di. The answer prompt is "What is the capital of Chile?" First call is Santiago. This is the correct answer, and it will add to the score and update it. The second call is Washington D.C. This is the incorrect answer, and it will not give any points, and display incorrect when the iteration is over. 3dii. The condition is if guess = answer in the constructor. First call would pass through a boolean and return true. Second call would pass through the boolean and return false. 
3diii. Result of first call is + 1 score and well done. Result of second call is + 0 and incorrect.
