class Programe:
    def __init__(self, configfile, database):
        self.db = database
        self.config = self.db.load(configfile)
        self.question_filename = self.config['questions_filename']
        self.answer_filename = self.config['answers_filename']

        self.exam = self.db.load(self.question_filename)

        self.questions = self.exam["exam_content"]
        self.answers = {}

    def add_name_surname(self, name: str, surname: str):
        if name.isalpha() and surname.isalpha():
            n = {"student_name": name}
            self.answers.update(n)

            s = {"student_surname": surname}
            self.answers.update(s)
            self.db.save(self.answers, self.answer_filename)
        else:
            raise ValueError

    def get_question(self, q_id):
        res_question = self.questions[q_id]
        return res_question

    def set_question(self, q_id, ques, answ):
        self.answers[q_id] = {ques: answ}
        self.db.save(self.answers, self.answer_filename)
