import genanki
import os
import shutil

tests = [
    '04_15',
    '07_15',
    '08_08',
    '08_10',
    '08_12',
    '08_13',
    '08_15',
]

my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

deck = genanki.Deck(deck_id=12312312321, name="Mathmatical logic")
deck.add_model(my_model)
media_files = []

for test_number in tests:
    for question_number in range(1, 11):
        original_question_file_path = os.path.join('images', test_number, 'questions', '{}.png'.format(question_number))
        destination_question_file_path = '{}_question_{}.png'.format(test_number, question_number)
        shutil.copy(original_question_file_path, destination_question_file_path)
        media_files.append(destination_question_file_path)
        original_answer_file_path = os.path.join('images', test_number, 'answers', '{}.png'.format(question_number))
        destination_answer_file_path = '{}_answer_{}.png'.format(test_number, question_number)
        shutil.copy(original_answer_file_path, destination_answer_file_path)
        media_files.append(destination_answer_file_path)
        question = 'Test: {} Question: {} <br/> <img src="{}">'.format(
            test_number,
            question_number,
            destination_question_file_path
        )
        answer = '<img src="{}">'.format(destination_answer_file_path)
        my_note = genanki.Note(
            model=my_model,
            fields=[question, answer])
        deck.add_note(my_note)


package = genanki.Package(deck)
package.media_files = media_files
package.write_to_file('logic.apkg')
for f in media_files:
    os.remove(f)
