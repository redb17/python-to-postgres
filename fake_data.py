from faker import Faker
import random
import time


fake = Faker()


def get_students(cnt):
    students = []

    for i in range(cnt):
        student_name = fake.name()
        gender = fake.random_element(elements=('M', 'F'))
        phone = fake.phone_number()
        
        place = fake.random_element(elements=('Jammu', 
            'Kashmir', 'Punjab', 'Himachal', 'Haryana', 'Delhi',
            'UP', 'Kolkata', 'Mumbai', 'Chennai', 'Bangalore',
            'Kerala'))
        
        addr = fake.address()

        row = [student_name, gender, phone, place, addr]
        students.append(row)
    
    return students # [[student_name, gender, phone, place, addr]]


def get_exams():
    exam_names = [
        "Joint Entrance Examination (JEE) Main",
        "Joint Entrance Examination (JEE) Advanced",
        "National Eligibility cum Entrance Test (NEET)",
        "Common Admission Test (CAT)",
        "Graduate Aptitude Test in Engineering (GATE)",
        "National Institute of Fashion Technology (NIFT) Entrance Exam",
        "Common Law Admission Test (CLAT)",
        "National Institute of Design (NID) Entrance Exam",
        "All India Institute of Medical Sciences (AIIMS) Entrance Exam",
        "Xavier Aptitude Test (XAT)",
        "National Entrance Examination for Design (NID DAT)",
        "Indian Statistical Institute (ISI) Admission Test",
        "National Institute of Technology (NIT) Entrance Exam",
        "Indian Institutes of Management Admission Test (IIM CAT)",
        "All India Pre-Medical Test (AIPMT)",
        "Indian Institute of Technology Joint Admission Test for M.Sc. (IIT JAM)",
        "National Entrance Screening Test (NEST)",
        "National Aptitude Test in Architecture (NATA)",
        "National Institute of Hotel Management Joint Entrance Examination (NCHM JEE)",
        "Symbiosis National Aptitude Test (SNAP)",
        "Common Management Admission Test (CMAT)",
        "Engineering, Agriculture and Medical Common Entrance Test (EAMCET)",
        "Karnataka Common Entrance Test (KCET)",
        "West Bengal Joint Entrance Examination (WBJEE)",
        "Vellore Institute of Technology Engineering Entrance Exam (VITEEE)",
        "National Board of Examinations Post Graduate Medical Entrance Exam (NEET PG)",
        "Indian Council of Agricultural Research All India Entrance Examination (ICAR AIEEA)",
        "National Law University Delhi All India Law Entrance Test (AILET)",
        "Joint Entrance Examination for Polytechnics (JEEP)",
        "Andhra Pradesh Law Common Entrance Test (AP LAWCET)",
        "National Institute of Technology Master of Computer Applications Common Entrance Test (NIMCET)",
        "Delhi University Entrance Test (DUET)"
    ]

    exams = []
    for exam_name in exam_names:
        row = [exam_name]
        exams.append(row)
    
    return exams # [[exam_name]]


def get_subjects(cnt):
    subjects = []

    for i in range(cnt):
        subject_name = fake.word().title()
        row = [subject_name]
        subjects.append(row)
    
    return subjects # [[subject_name]]


def get_chapters(cnt, subjects):
    chapters = []
    chapter_id = 1

    for i in range(len(subjects)):
        subject_id = i + 1
        for j in range(cnt):
            chapter_name = fake.word().title()
            row = [chapter_id, chapter_name, subject_id]
            chapters.append(row)
            chapter_id += 1

    return chapters


def get_answers(cnt):
    answers = []

    for i in range(cnt):
        answer = fake.sentence(nb_words=10)
        row = [answer]
        answers.append(row)
    
    return answers


def get_questions(cnt, answers, chapters):
    questions = []
    answers_count = len(answers)
    question_id = 1
    qna = {}

    for chapter in chapters:
        chapter_id = chapter[0]
        for i in range(cnt):
            question = fake.sentence(nb_words=10)
            answer_option_1 = random.randint(1, answers_count)
            answer_option_2 = random.randint(1, answers_count)
            answer_option_3 = random.randint(1, answers_count)
            answer_option_correct = random.randint(1, answers_count)

            row = [question_id, question, answer_option_1, answer_option_2, answer_option_3, answer_option_correct, chapter_id]
            questions.append(row)

            qna[question_id] = answer_option_correct
            question_id += 1

    return questions, qna


def get_events(cnt):
    events = []

    for i in range(cnt):
        event_code = f'{i}_{fake.word().upper()}'
        event_code = event_code[:10]
        
        event = fake.sentence(nb_words=10)
        total_questions = random.randint(10, 50)
        min_corrects = random.randint(4, total_questions)
        row = [event_code, event, total_questions, min_corrects]
        events.append(row)

    return events


def get_random_ts(last_n_days):
    current_timestamp = int(time.time())
    max_timestamp = current_timestamp - last_n_days * 24 * 60 * 60
    
    random_timestamp = random.randint(max_timestamp, current_timestamp)
    random_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(random_timestamp))
    random_date = time.strftime("%Y-%m-%d", time.localtime(random_timestamp))
    
    return random_datetime, random_date


def get_attempts(cnt, students, questions, exams, answers, events, qna):
    attempts = []
    
    for i in range(cnt):
        attempt_ts, attempt_dt = get_random_ts(30)
        student_id = random.randint(1, len(students))
        question_id = random.randint(1, len(questions))
        exam_id = random.randint(1, len(exams))
        
        # this will lead to very less correct attempts
        selected_answer_id = random.randint(1, len(answers))
        # increasing the chances of correct attempts to 50%
        selected_answer_id = fake.random_element(elements=(selected_answer_id, qna[question_id]))

        event_code = events[random.randint(0, len(events)-1)][0]

        row = [attempt_ts, attempt_dt, student_id, question_id, exam_id, selected_answer_id, event_code]
        attempts.append(row)
    
    return attempts
