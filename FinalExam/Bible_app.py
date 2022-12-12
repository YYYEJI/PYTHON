# import Streamlit.
import streamlit as st

# import the Bible module.
from Bible import Bible

# create an instance of the Bible class.
b = Bible() 

# initialize the Bible module.
b.init()


# implement a Bible search app using Streamlit.
st.title("Handong Bible App")
selectedBible = st.selectbox("Book Name", ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job", "Psalm", "Proverbs", "Ecclesiastes", "Song of Songs", "Lsaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Chorinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"])
chapter = st.number_input("Chapter?", min_value=1, max_value=b.get_max_chapter(selectedBible), value=1)
verse = st.slider("Verse", min_value=1, max_value=b.get_max_verse(selectedBible, chapter), value=1)
text_area = st.text_area(label="Text", value=b.search(selectedBible, chapter, verse))

st.markdown(
    "*Copyright 2022 Jaeyoung Chun | School of Applied Artificial Intelligence | Handong Global University*"
)