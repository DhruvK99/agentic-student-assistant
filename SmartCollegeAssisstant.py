from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

@tool
def Attendance_Calculator(total_classes:int,attended_classes:int)->str:
    """Calculate the Attendance Percentage and the Eligibility Status of a student"""
    Attendance_Percentage = (attended_classes/total_classes)*100
    if Attendance_Percentage >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible"
    return f"Your attendance percentage is {Attendance_Percentage:.2f}% and the you are {status} for the Exam"

@tool
def Result_Calculator(mark1:float,mark2:float,mark3:float,mark4:float,mark5:float)->str:
    """Calculate the Average marks and the Result Status of a student"""
    total= mark1+mark2+mark3+mark4+mark5
    average = total/5
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    if average >= 50:
        status = "Passed"
    else:
        status = "Failed"

    return f"Your Total Marks: {total}, Your average mark: {average:.2f}, Grade: {grade}, and you have {status}"

@tool
def Fee_Balance_Calculator(total_fee:float,paid_fee:float)->str:
    """Calculate the Fee Balance of a student"""
    balance = total_fee - paid_fee
    return f"Your Pending Fee Amount is: ₹{balance:.2f}"

@tool
def Library_Fine_Calculator(delayed_days:int)->str:
    """Calculate the Library Fine of a student"""
    fine_per_day = 5
    total_fine = delayed_days * fine_per_day
    return f"Your Library Fine is: ₹{total_fine:.2f}"

@tool
def Hostel_Fee_Calculator(monthly_fee:float,no_of_months:int)->str:
    """Calculate the Total Hostel Fee of a student"""
    total_fee = monthly_fee * no_of_months
    return f"Your Total Hostel Fee is: ₹{total_fee:.2f}"

student_database = {
    "S1": {"Name": "Alice Smith", "Age": 20, "Credits Earned": "110"},
    "S2": {"Name": "Bob Johnson", "Age": 19, "Credits Earned": "100"},
    "S3": {"Name": "Charles Davis", "Age": 18, "Credits Earned": "85"}
}

@tool
def Student_Information_Tool(student_id:str)->str:
    """Retrieve Information of Student like Name, Age and Credits Earned using Student ID from Student Database"""

    student = student_database.get(student_id.strip().upper())
    if student:
        return f"Student Record Found: {student}"
    else:
        return f"Error: No student found with ID {student_id}."

llm = ChatOllama(model="qwen2.5:3b", temperature=0)

tools = [Attendance_Calculator, Result_Calculator, Fee_Balance_Calculator, Library_Fine_Calculator, Hostel_Fee_Calculator, Student_Information_Tool]

prompt = ChatPromptTemplate.from_messages( [ ("system","""You are a College Student Assisstant. Use the availiable tools according to the requirement whenever possible. Give Clear and Concise Answers to the Student's Queries"""),("human", "{input}"), ("placeholder", "{agent_scratchpad}")])

agent = create_tool_calling_agent(llm=llm,tools=tools,prompt=prompt)

agent_executor = AgentExecutor(agent=agent,tools=tools, verbose=True)

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    try:
        response = agent_executor.invoke({"input":user_input})
        print("\nFinal Response:")
        print(response["output"])
    except Exception as e:
        print(f"An Error Occured: {e}")
