'''
created on Thu jul 13 02:29:00 2023
@auther: Arsalan Bakhtiar AB
Project no. 1 : Financial Data Extraction Tool Using OpenAI API
'''

# importing modules 
import openai 
from api_key import open_api_key
import json

# Pass the api key to openai.api_key
openai.api_key = open_api_key

# create a function for the extraction data

def extract_financial_data(text):
    prompt = get_prompt_financial()+text
    response  = openai.ChatCompletion.create(
        # Define the model which you want to used
        model = 'gpt-3.5-turbo'
        messages = [
            {'role':'user',
             'content':prompt
            }
        ]
    )
    content = response.choices[0]['message']['content']
    try:
        data = json.loads(content) # Convert String into Dictionary
        return pd.DataFrame(data.items(),columns=['Measure','Value'])
    except(json.JSONDecodeError, IndexError):
        pass
    return pd.DataFrame({
        "Measure":['Company Name','Stock Symbol','Revenue','Net Income','EPS'],
        "Values":["","","",""]

    })

# Function for prompt

def get_prompt_financial():
    return '''
    Please retrieve company name, revenue, net income and earnings per share aka 'EPS'
    from the following news article. if you can't find the information from this article then return ''.
    Do not make thing up.
    Then revice the stock symbolcorresponding to that company. for this you can use your general knowledge 
    (it dosen't have to be form this article). 
    Always return your respnce as a valid JSON string.
    The formate of the string should be this.
    {
        'Company Name' : 'Walmart',
        'Stock Symbol' : 'WMT',
        'Revenue'      : '12.34 million',
        'Net Income'   : '34.78 million',
        'EPS'          : '2.1 $'
    }
    '''

if __name__ == '__main__':
    text = '''
    Enter your Text
    '''
    extract_financial_data(text)