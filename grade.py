#!/bin/python3

 # 定义ANSI颜色代码
color_reset = "\033[0m"  # 重置颜色
color_red = "\033[91m"   # 红色
color_green = "\033[92m"  # 绿色
color_yellow = "\033[93m"  # 黄色
color_blue = "\033[94m"   # 蓝色
color_magenta = "\033[95m"  # 洋红色
color_cyan = "\033[96m"   # 青色
color_white = "\033[97m"  # 白色

# !TODO: Fetch grades from the academic affairs website and clean the format. 

def Input(format: str) -> list:
    # To transform the string list to integer list
    # arguments: Input format for Users
    tmp = input(format)
    tmp_integer = [ float(x) for x in tmp.split() ]
    return tmp_integer

def calculating(date: list) -> list:
    length = len(date)
    summer = sum(date)
    average = summer / length
    return [summer, length, average]    

print(color_blue + "------------------------Div----------------------------" + color_reset)
print(color_magenta + "This is a script used for calculating composite grades!" + color_reset)
print(color_blue + "------------------------Div----------------------------" + color_reset)
# Input date
compulsory = Input("Enter your compulsory grade\n")
elective = Input("Enter your elective grade\n")
sports = float(input("The sports\n"))
actives = float(input("The sport's actives\n"))
# Process date
compulsory_sum, compulsory_len, compulsory_avg = calculating(compulsory)
elective_sum, elective_len, elective_avg = calculating(elective)
sports_grade = sports * 0.7 + actives * 0.3   
interim_grade = (compulsory_avg * 1.2 + elective_avg * 0.8) * 0.5 * 0.6
# The 25 is a fixed moral and ethical score
composite_grades= 25 + sports_grade * 0.1 + interim_grade
# Output date
print(color_blue + "------------------------Div----------------------------" + color_reset)
print(color_green + "The sports: ", sports, actives, color_reset)
print("The compulsory:",compulsory)
print("The elective:",elective)
print(color_cyan + "Length\tSum\tAverage\t\t\tKind" + color_reset)
print(f"{compulsory_len}\t{compulsory_sum}\t{compulsory_avg}\tCompulsory grades")
print(f"{elective_len}\t{elective_sum}\t{elective_avg}\tElective grades")
print(color_blue + "------------------------Div----------------------------" + color_reset)
print(color_red + "Interim grade", interim_grade, color_reset)
print(color_blue + "------------------------Div----------------------------" + color_reset)
print(color_red + "Composite grade: ", composite_grades, color_reset)
print(color_blue + "------------------------Div----------------------------" + color_reset)
