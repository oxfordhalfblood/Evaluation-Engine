import pandas as pd 

def test1(a):
    print("Test 1:your name is : {}".fromat(a))

def test2(a):
    print("Test 1:your name is : {}".fromat(a))

data = {'id':[1,2],
'object_id' :["7687", "827892"], 
'object_type' :["account", "account"],
'variable':["accountLife", "MEP"], 
'value' :["7898", "7332"]} 
globalVariables = pd.DataFrame(data=data)

def pullVariablesDef():
    data = {'id':[1,2],
    'variable_name':["postlife", "accountlife", ""], 
    'function':["test1", "test2", "test3"], 
    'description' :["target audience Y", "post more", "hbdweghv bdw"]
    } 
    globalVariableDef = pd.DataFrame(data=data)
    # globalVariableDef = df.sort_values(by ='priority')
    print(globalVariableDef)
    return(globalVariableDef)

def saveVariables(df):
    return(True)

def populateVariables(acc_id, ad_id = 0):    
    globalVariableDef = pullVariablesDef()
    globalVariableDef
    print("Done")

def main():
    populateVariables(2342)
        
if __name__== "__main__":
  main()