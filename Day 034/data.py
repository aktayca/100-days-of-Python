import requests

class QuizData:
    def get_questions(self):
        self.parameters = {
            "amount": 10,
            "type": "boolean",
        }

        self.response = requests.get(url="https://opentdb.com/api.php", params=self.parameters)
        self.response.raise_for_status()

        self.question_data =  self.response.json()