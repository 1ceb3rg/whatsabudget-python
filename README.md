# WHATSABUDGET

A Whatsapp group is an easy way to keep track of spending between a group of people. WhatsABudget will parse the exported text file and display the totals.

## Usage

```bash
whatsabudget.py [-h] [--startDate STARTDATE] [--endDate ENDDATE] <filename>
```

*Required Arguments*:

- filename  
  - .txt file from the exported chat

*Optional Arguments*:

- -h, --help
  - show the help message
- --startDate
  - the date to start calculating from
  - defaults to the 90's :)
- --endDate
  - the date to stop calculating at
  - defaults to datetime.now()

Create whatsapp group for the participants. participants only enter how much that paid. Currently only the same currency is supported. Only messages containing only numbers will be parsed.  

#### Example conversation

- person1: 30
- person2: 40
- person2: 24.20
- person1: 32.43
- person1: 30
- person2: 40
- person2: apples 4.0
  - not parsed
- person2: 24.20
- person1: 32.43

### Export the chat

1. Go to the settings for the group chat
2. Select export chat
3. Export the chat without images
4. Extract the zipped text file on your computer

### Checking the budget

```bash
python3 ./whatsabudget.py _chat.txt --endDate '01/05/2022' --startDate '11/01/2021'

Person1: 502.20
Person2: 123.20

```
