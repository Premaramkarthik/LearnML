import streamlit as st
from pathlib import Path


#continue break and pass


st.set_page_config(layout="wide")

st.sidebar.title("Python Concepts")

# Initialize session state to store the selected page
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Overview"

# Sidebar selectbox for page navigation with session state
option = st.sidebar.selectbox(
    "Choose a concept", 
    ["Overview", "Variables", "Operators", "Strings","Lists", "Shallow copy and deep copy","Tuples", "Sets","Dictionary"
     ,"Conditional statements","Continue Break and Pass","Loops","Functions","Generator","Class and object",
     "Introduction to OOP",'pattern using for loop',"pattern using while loop","cipher decipher","String methods"],
    key="selected_page"
)

# Refresh the page when a new option is selected
if st.session_state.selected_page != option:
    st.session_state.selected_page = option
    st.experimental_rerun()



#option = st.sidebar.selectbox("Choose a concept", ["Overview", "Variables", "Operators", "Strings", "Lists", "Tuples", "Sets"])

if option == "Overview":
    with open(Path("pages/python/overview.py")) as f:
        exec(f.read())
        
elif option == "Variables":
    with open(Path("pages/python/variables.py")) as f:
        exec(f.read())
        
elif option == "Operators":
    with open(Path("pages/python/operators.py")) as f:
        exec(f.read())
        
elif option == "Strings":
    with open(Path("pages/python/strings.py")) as f:
        exec(f.read())
        
elif option == "Lists":
    with open(Path("pages/python/list.py")) as f:
        exec(f.read())
        
elif option == "Shallow copy and deep copy":
    with open(Path("pages/python/copy.py")) as f:
        exec(f.read())
        
elif option == "Tuples":
    with open(Path("pages/python/tuple.py")) as f:
        exec(f.read())
        
elif option == "Sets":
    with open(Path("pages/python/set.py")) as f:
        exec(f.read())
        
elif option == "Dictionary":
    with open(Path("pages/python/dictionary.py")) as f:
        exec(f.read())
    
elif option == "Conditional statements":
    with open(Path("pages/python/condition_statements.py")) as f:
        exec(f.read())
    
elif option == "Continue Break and Pass":
    with open(Path("pages/python/continue_break_and_pass.py")) as f:
        exec(f.read())

elif option == "Loops":
    with open(Path("pages/python/loops.py")) as f:
        exec(f.read())

elif option == "Functions":
    with open(Path("pages/python/functions.py")) as f:
        exec(f.read())

elif option == "Generator":
    with open(Path("pages/python/Generator.py")) as f:
        exec(f.read())   

elif option == "Class and object":
    with open(Path("pages/python/Class_and_object.py")) as f:
        exec(f.read())   
        
elif option == "Introduction to OOP":
    with open(Path("pages/python/Introduction_to_OOP.py")) as f:
        exec(f.read())   
        
elif option == "pattern using for loop":
    with open(Path("pages/python/pattern_using_for_loop.py")) as f:
        exec(f.read())   
        
elif option == "pattern using while loop":
    with open(Path("pages/python/patterns_using_while_loop.py")) as f:
        exec(f.read())  

elif option == "cipher decipher":
    with open(Path("pages/python/cipherdecipher.py")) as f:
        exec(f.read())  

elif option == "String methods":
    with open(Path("pages/python/String_method.py")) as f:
        exec(f.read())  
