import streamlit as st
from streamlit_option_menu import option_menu
from subjects import chemistry, physics,maths,eee_sub
from mapps import papers

def app():
    # Check if a subject is already selected
    if "eee" not in st.session_state:
        st.session_state.eee = None

    # Show the menu only if no subject has been selected yet
    if st.session_state.eee is None:
        sub = option_menu(
            menu_title="Choose Subject here",
            options=["select","Chemistry", "Physics", "Maths", "Electrical","Previous Papers"],
            menu_icon="book-fill",
            default_index=0
        )

        if sub!="select":  # Update the session state when a subject is selected
            st.session_state.eee = sub

    # Based on the selected subject, display the corresponding app
    if st.session_state.eee == "Chemistry":
        chemistry.app()
    elif st.session_state.eee == "Physics":
        physics.app()
    elif st.session_state.eee == "Maths":
        maths.app()
    elif (st.session_state.eee== "Electrical"):
        eee_sub.app()
    elif st.session_state.eee=="Previous Papers":
        papers.eee()
    # Add a reset button to clear the selection and show the menu again
    if st.session_state.eee is not None:
        if st.button("Choose Another Subject"):
            st.session_state.eee = None


if __name__ == "__main__":
    app()

