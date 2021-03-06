import openpyxl
from helper import Handler

wb = Handler("C:/Users/malique/important_stuff/CSEC-Prep/CSEC Prep.xlsx")
print("The following are the sheet names:")
print(wb.get_sheet_names())

sheet = input("\nWhich sheet would you like to use?\n")
action = input("\nWould you like to get the topics(t) or questions(q)?\n")

if action == "t":
    topics = wb.get_topics(sheet)

    topics_html = list(map(lambda x: x.html(), topics))
    
    print(topics_html)
    print('\n'.join(topics_html))

    wb.insert(f"C:/Users/malique/important_stuff/CSEC-Prep/{sheet}.html", "topic", '\n'.join(topics_html))

elif action == "q":
    questions = wb.get_questions(sheet)

    questions_html = list(map(lambda x: x.html(), questions))
    print('\n'.join(questions_html))

    wb.insert(f"C:/Users/malique/important_stuff/CSEC-Prep/{sheet}.html", "question", '\n'.join(questions_html))