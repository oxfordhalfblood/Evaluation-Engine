from simpleeval import simple_eval
from simpleeval import SimpleEval
import ast
import operator
import time
import mysql.connector
import configparser
import os
from rules import demographic as d
import rules.postperformance as p
import pandas as pd 
import json
import calendar;
import time;

add_relevant = []
add_violated = []
add_feedback = []

post_id= 22200

funcDict =	{
  "accountlife": d.accountlife,
  "latest_ad_life": d.latest_ad_life,
  "postlife": p.postlife,
  "post_engagement": p.post_engagement,
  "post_ctr": p.post_ctr,
  "add": p.add,
  "display": d.display
}
engine = SimpleEval()
engine.functions = funcDict
engine.operators[ast.BitAnd] = operator.and_

def connection():
    config = configparser.ConfigParser()
    filename = "./expertsystem/config.cfg"

    if os.path.isfile(filename):
      config.read(filename)
      return mysql.connector.connect(host=config.get('mysqlDB', 'host'),   # your host, usually localhost
                          user=config.get('mysqlDB', 'user'),         # your username
                          passwd=config.get('mysqlDB', 'passwd'),  # your password
                          db=config.get('mysqlDB', 'db'),          # name of the data base
                          port=int(config.get('mysqlDB', 'port')),
                          auth_plugin=config.get('mysqlDB','auth_plugin')) 
    else:
      print("Config file not found")

def evaluate(userfunc):
  try:
    v = engine.eval(userfunc)
    return v

  except Exception as e:
    print("Sorry, Invalid input. Enter correct format.{}".format(e))
    return e


def input_rules(df):
  for index, row in df.iterrows():

        try:
            userfunc = row['relevant']
            print(userfunc)
            # input("Check relevant condition or Exit with CTRL+D: ")
            relevant_cond = evaluate(userfunc)
            #print(relevant_cond)

            if relevant_cond is True:
              relev_rules = row['id']
              add_relevant.append(relev_rules)
              #print(add_relevant)
              userfunc = row['satisfactory']
              print(userfunc)
              # input("Check satisfactory condition or Exit with CTRL+D:")
              satisfactory_cond = evaluate(userfunc)
              #print(satisfactory_cond)

              if satisfactory_cond is False :
                viol_rules = row['id']
                add_violated.append(viol_rules)
                # print("Released feedback: ", row['feedback'])
                add_feedback.append(row['feedback'])
                
              else:
                continue

            else:
              continue

            ts = calendar.timegm(time.gmtime())
            json_data = json.dumps({"timestamp": ts,"relevant": add_relevant, "violated": add_violated, "feedback": add_feedback})
            print("THE JSON: ")
            print(json_data)

        except EOFError:
            break


def main():

  obj_type = input("Select object Ad or Account:")
  df = pd.read_excel('domain.xlsx')
  df = df.sort_values(by ='priority')
  is_obj =  df['object']==obj_type
  df = df[is_obj]
  print(df)
  input_rules(df)

if __name__== "__main__":
  main()


# ==================  some backup code ===================

  # con = connection()
  # cur = con.cursor()
  # mySql_insert_query = """SELECT ruleid from domain ORDER BY priority"""
  # mySql_insert_query = """INSERT INTO rules (ruleid , , ) SELECT ruleid from domain ORDER BY domain.priority"""
  # cur.execute(mySql_insert_query)

  # rows = cur.fetchall()
  # sortedRules = [list(i) for i in rows]
  # print(sortedRules)
 
  # print('Total Row(s):', cur.rowcount)
  # for row in rows:
  #     print(row)

  # print("Record inserted successfully into rules table")

  # print(cur)
  # con.close()
  
        # except Exception as e:  
        #   print("Sorry, Invalid input. Enter correct format.{}".format(e))
          # continue
        


# userinputFunct = '5*(1-(x*1))'
# item = simple_eval(userinputFunct, names = {'x':4})

# s = SimpleEval(functions=funcDict)



# def boo(a):
#     print(a)
#     return a+'Boo!'

# print(s)


#print(item)

# c = simple_eval("print(3)", functions=funcDict)
# c = simple_eval("display(add(1,2))", functions=funcDict)
# c=simple_eval("add(1,2)", functions=funcDict)

# simple_eval("add(1,2)", functions=funcDict)

# c = simple_eval("display(add(1,2))", functions=funcDict)

# c = simple_eval("def add(x,y): return x", functions=funcDict)



# s.operators[ast.BitXor] = operator.xor
# print(str(c))

# relevant = ["postlife", "accountlife"]
# satisfactory = ["postengagement", "accountactivity"]
# feedback = ["target audience Y", "post more"]
# priority = [3,1]

# rule = zip(priority, relevant, satisfactory, feedback)
# Z = sorted(rule)
# print("sorted rules: ",Z)

# #Z = [x for _,x in sorted(zip(Y,X))]

