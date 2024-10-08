import streamlit as st
from streamlit_option_menu import option_menu
from subjects import chemistry, physics,maths,computers
from mapps import papers

def app():
    # Check if a subject is already selected
    if "selected" not in st.session_state:
        st.session_state.selected = None

    # Show the menu only if no subject has been selected yet
    if st.session_state.selected is None:
        sub = option_menu(
            menu_title="Choose Subject here",
            options=["select","Chemistry", "Physics", "Maths", "Computers","Previous Papers"],
            menu_icon="book-fill",
            default_index=0
        )

        if sub!="select":  # Update the session state when a subject is selected
            st.session_state.selected = sub

    # Based on the selected subject, display the corresponding app
    if st.session_state.selected == "Chemistry":
        chemistry.app()
    elif st.session_state.selected == "Physics":
        physics.app()
    elif st.session_state.selected == "Maths":
        maths.app()
    elif st.session_state.selected == "Computers":
        computers.app()
    elif st.session_state.selected=="Previous Papers":
        papers.cse()        
    # Add a reset button to clear the selection and show the menu again
    if st.session_state.selected is not None:
        if st.button("Choose Another Subject"):
            st.session_state.selected = None


if __name__ == "__main__":
    app()

