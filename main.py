from database import DataBase
from messages import Message
from programe import Programe

if __name__ == '__main__':
    config_filename = 'config.json'
    db = DataBase()
    message = Message()

    program = Programe(config_filename, db)
    config = db.load(config_filename)

    while True:
        name = input(message.ent_name).capitalize()
        surname = input(message.ent_surname).capitalize()
        try:
            program.add_name_surname(name, surname)
            break
        except ValueError:
            print(message.fail)
            continue

    start = config['start']
    end = config['end']

    while start <= end:
        ind = str(start)
        f_question = program.get_question(ind)
        question = f_question["question"]
        a = f_question["a"]
        b = f_question["b"]
        c = f_question["c"]
        d = f_question["d"]

        print(message.question_mess.format(question=question, a=a, b=b, c=c, d=d))
        answ = input(message.ent_answ).lower()

        if answ in ('a', 'b', 'c', 'd'):
            answer = f_question[answ]
            program.set_question(ind, question, answer)
        else:
            continue

        print(30 * '___')

        start += 1

