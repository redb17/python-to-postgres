from fake_data import *
from postgres_connect import ingest


tables_cols = {
    'students': ['student_name', 'gender', 'phone', 'place', 'addr'],
    'exams': ['exam_name'],
    'subjects': ['subject_name'],
    'chapters': ['chapter_id', 'chapter_name', 'subject_id'],
    'answers': ['text_description'],
    'questions': ['question_id', 'text_description', 'answer_option_1', 'answer_option_2', 'answer_option_3', 'answer_option_correct', 'chapter_id'],
    'events': ['event_code', 'text_description', 'total_questions', 'min_corrects'],
    'attempts': ['attempt_ts', 'attempt_dt', 'student_id', 'question_id', 'exam_id', 'selected_answer_id', 'event_code']
}


def start_ingestion():
    students = get_students(10_000)
    exams = get_exams()
    subjects = get_subjects(20)
    chapters = get_chapters(10, subjects)
    answers = get_answers(10_000)
    questions, qna = get_questions(20, answers, chapters)
    events = get_events(50)
    attempts = get_attempts(100_000, students, questions, exams, answers, events, qna)

    ingest('students', students, tables_cols)
    ingest('exams', exams, tables_cols)
    ingest('subjects', subjects, tables_cols)
    ingest('chapters', chapters, tables_cols)
    ingest('answers', answers, tables_cols)
    ingest('questions', questions, tables_cols)
    ingest('events', events, tables_cols)
    ingest('attempts', attempts, tables_cols)



if __name__ == '__main__':
    print('Starting main().')
    start_ingestion()
