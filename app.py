import streamlit as st
from expense import add_expense
from time_log import add_time
from analysis import load_data, productivity_score

st.set_page_config(page_title="Student Tracker", layout="centered")

st.title("🎓 Student Life Efficiency Tracker")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Add Expense","Log Time","Dashboard"]
)

# -------- ADD EXPENSE --------
if menu == "Add Expense":
    st.header("💸 Add Expense")
    item = st.text_input("Item name")
    amount = st.number_input("Amount", step=1.0)

    if st.button("Save Expense"):
        if item != "" and amount > 0:
            add_expense(item, amount)
            st.success("Expense saved!")
        else:
            st.warning("Enter valid details")

# -------- LOG TIME --------
elif menu == "Log Time":
    st.header("⏱ Log Activity Time")
    activity = st.text_input("Activity")
    hours = st.number_input("Hours", step=0.5)

    if st.button("Save Time"):
        if activity != "" and hours > 0:
            add_time(activity, hours)
            st.success("Time logged!")
        else:
            st.warning("Enter valid details")

# -------- DASHBOARD --------
elif menu == "Dashboard":
    st.header("📊 Dashboard")

    exp, time = load_data()

    st.subheader("Expenses")
    st.dataframe(exp)

    st.subheader("Time Logs")
    st.dataframe(time)

    score = productivity_score(exp, time)
    st.subheader(f"🎯 Productivity Score: {score}")

    import matplotlib.pyplot as plt

    if not exp.empty:
        st.subheader("📊 Expense Chart")
        fig, ax = plt.subplots()
        ax.bar(exp["item"], exp["amount"])
        st.pyplot(fig)

    if not time.empty:
        st.subheader("⏱ Time Usage")
        fig2, ax2 = plt.subplots()
        ax2.pie(time["hours"], labels=time["activity"], autopct="%1.1f%%")
        st.pyplot(fig2)

        