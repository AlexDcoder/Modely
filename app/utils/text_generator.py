'''
    Code explainer using GROQ API
'''
import os
from pprint import pprint

from groq import Groq
from dotenv import load_dotenv


def define_data(context: str, qtd_questions: int = 10) -> str | None:
    '''
        Create text and answers for the questions
    '''

    # Load the API KEY from .env
    load_dotenv()
    client = Groq(api_key=os.environ["GROQ_USER_API"])

    # Generate the text for the questions and answers
    answer = client.chat.completions.create(
        # Defining the parameters for the AI

        messages=[
            {
                "role": "system",
                "content": f'''
                You're a question generator you will generate only the text
                of {qtd_questions} questions, about the database
                modeling of the context and they should be multiple
                choice questions or true or false questions, with no items.

                The text of the questions is separated just by an ;
                There should not have any \n in the text

                if the context dosen't seem like a database
                modeling problem or it doesen't give enought context to
                create questions
                you should return nothing and just noithing
                '''

            },
            {
                "role": "user",
                "content": f'''
                    {context}
                    '''
            },


        ],
        model="llama-3.1-8b-instant",
    )
    return answer.choices[0].message.content


def exctracting_informations(problem: str):
    '''
        After generate the questions, this
        function will extract the important
        information in text
    '''
    original_text = define_data(problem)

    if original_text is not None:
        print(original_text)
        print("="*100)
        pprint(original_text.split('\n'))


if __name__ == '__main__':
    print(exctracting_informations(
        '''
            I have a bookstore
            '''
    ))
