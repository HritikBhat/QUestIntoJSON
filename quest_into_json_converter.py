from tkinter import *
from tkinter import messagebox

quest_count=0

def resetOP():
    global quest_count
    quest_count=0
    pr_txt.delete("1.0",END)
def checkType():
    one_counter=0
    lt=[]
    lt.append(opt1_val.get())
    lt.append(opt2_val.get())
    lt.append(opt3_val.get())
    lt.append(opt4_val.get())
    for i in range(len(lt)):
        if lt[i]==1:
            one_counter+=1
    if one_counter==1:
        return "SCQ"
    elif one_counter>1:
        return "MCQ"
    
def startConvert():
    try:
        quest_st="\"question\":\""+q_txt.get("1.0",END).rstrip("\n")+"\","
        #print(quest_st)

        type_st="\"type\":\""+checkType()+"\","
        #print(type_st)
        
        opt1_st="\""+opt1_txt.get("1.0",END).rstrip("\n")+"\""
        opt1_st.replace("\n","")
        opt2_st="\""+opt2_txt.get("1.0",END).rstrip("\n")+"\""
        opt3_st="\""+opt3_txt.get("1.0",END).rstrip("\n")+"\""
        opt4_st="\""+opt4_txt.get("1.0",END).rstrip("\n")+"\""
        opt_st="\"option\":["+opt1_st+","+opt2_st+","+opt3_st+","+opt4_st+"],"
        #print(opt_st)
        #e_txt.insert("1.0",opt_st)

        ans_st="\"answer\":"+"["+str(opt1_val.get())+","+str(opt2_val.get())+","+str(opt3_val.get())+","+str(opt4_val.get())+"],"
        #print(ans_st)

        exp_st="\"explain\":\""+e_txt.get("1.0",END).rstrip("\n")+"\""
        #print(exp_st)

        global quest_count
        if quest_count==0:
            json_st="{\n"+quest_st+"\n"+type_st+"\n"+opt_st+"\n"+ans_st+"\n"+exp_st+"\n"+"}"
            quest_count+=1
        else:
            json_st=",\n{\n"+quest_st+"\n"+type_st+"\n"+opt_st+"\n"+ans_st+"\n"+exp_st+"\n"+"}"
        #print(json_st)
        pr_txt.insert(END,json_st)

    except TypeError:
        messagebox.showwarning("Warning","Not Selected Choice/s")  
    

root = Tk()
root.geometry("900x800")
root.resizable(False, False)
root.title("Quest Into JSON Converter")
q_lbl=Label(root,text="Enter Question:")
q_lbl.place(x=20,y=50)

q_txt=Text(root,width=40,height=5)
q_txt.place(x=140,y=50)


opt1_val=IntVar()
opt1_chk = Checkbutton(
        root, variable=opt1_val,
        onvalue=1, offvalue=0)
opt1_chk.place(x=40,y=180)

opt1_txt=Text(root,width=40,height=3)
opt1_txt.place(x=100,y=180)

opt2_val=IntVar()
opt2_chk = Checkbutton(
        root, variable=opt2_val,
        onvalue=1, offvalue=0)
opt2_chk.place(x=40,y=270)

opt2_txt=Text(root,width=40,height=3)
opt2_txt.place(x=100,y=270)

opt3_val=IntVar()
opt3_chk = Checkbutton(
        root, variable=opt3_val,
        onvalue=1, offvalue=0)
opt3_chk.place(x=40,y=360)

opt3_txt=Text(root,width=40,height=3)
opt3_txt.place(x=100,y=360)

opt4_val=IntVar()
opt4_chk = Checkbutton(
        root, variable=opt4_val,
        onvalue=1, offvalue=0)
opt4_chk.place(x=40,y=450)

opt4_txt=Text(root,width=40,height=3)
opt4_txt.place(x=100,y=450)

e_lbl=Label(root,text="Enter Explanation:")
e_lbl.place(x=20,y=540)

e_txt=Text(root,width=40,height=5)
e_txt.place(x=140,y=540)

pr_txt=Text(root,width=40,height=35)
pr_txt.place(x=500,y=50)

mk_btn=Button(root,text="Convert into JSON",command=startConvert)
mk_btn.place(x=180,y=650)

rs_btn=Button(root,text="Reset Output",command=resetOP)
rs_btn.place(x=590,y=650)
root.mainloop()
