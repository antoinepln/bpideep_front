import streamlit as st
import pages.search
import pages.performers
import pages.home
# ast.core.services.other.set_logging_format()

PAGES = {
    "Home": pages.home,
    "Search company": pages.search,
    "Monthly report": pages.performers,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        #ast.shared.components.write_page(page)
        page.write()


    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app was developped by [Antoine Planchon](https://fr.linkedin.com/in/antoine-planchon-57b422193), [Nicolas Rousselet](https://www.linkedin.com/in/nicolas-rousselet-188158b0/), [Nicolas Tournaud](https://www.linkedin.com/in/nicolastournaud) and [Alexandre Huet](https://www.linkedin.com/in/alexandre-huet-5a0563127/).\n
        This two-weeks project concludes a Data Science Bootcamp at [Le Wagon](https://www.lewagon.com/fr/data-science-course/full-time).\n
        Special thanks to [BPI France](https://www.bpifrance.fr/) for the ressources and great advices, and to the wonderful team of [Le Wagon](https://www.bpifrance.fr/).
    """
    )


if __name__ == "__main__":
    main()
