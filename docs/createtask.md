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
