import multiprocessing
import random
import time

import streamlit as st


class Background(multiprocessing.Process):
    def __init__(self, shared_namespace):
        super().__init__()
        self.shared_namespace = shared_namespace

    def run(self):
        while True:
            time.sleep(10)
            self.shared_namespace.random = random.randint(1, 1000)


if __name__ == "__main__":
    shared_namespace = multiprocessing.Manager().Namespace()
    shared_namespace.random = random.randint(1, 1000)

    background = Background(shared_namespace)
    background.start()

    st.title('🔨 Streamlit Template')
    st.markdown("""
        This app is only a template for a new Streamlit project. <br>

        ---
        """, unsafe_allow_html=True)

    st.balloons()

    st.write(shared_namespace.random)
